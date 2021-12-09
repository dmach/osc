import importlib
import bz2
import base64
import codecs
import getpass
import subprocess
try:
    from urllib.parse import urlsplit
except ImportError:
    from urlparse import urlsplit
try:
    import keyring
except ImportError:
    keyring = None
try:
    import gnomekeyring
except ImportError:
    gnomekeyring = None


class AbstractCredentialsManagerDescriptor(object):
    def name(self):
        raise NotImplementedError()

    def description(self):
        raise NotImplementedError()

    def create(self, cp):
        raise NotImplementedError()

    def __lt__(self, other):
        return self.name() < other.name()


class AbstractCredentialsManager(object):
    config_entry = 'credentials_mgr_class'

    def __init__(self, cp, options):
        super(AbstractCredentialsManager, self).__init__()
        self._cp = cp
        self._process_options(options)

    @classmethod
    def create(cls, cp, options):
        return cls(cp, options)

    def get_password(self, url, user, defer=True):
        # If defer is True a callable can be returned
        # and the password is retrieved if the callable
        # is called. Implementations are free to ignore
        # defer parameter and can directly return the password.
        # If defer is False the password is directly returned.
        raise NotImplementedError()

    def set_password(self, url, user, password):
        raise NotImplementedError()

    def delete_password(self, url, user):
        raise NotImplementedError()

    def _qualified_name(self):
        return qualified_name(self)

    def _process_options(self, options):
        pass


class PlaintextConfigFileCredentialsManager(AbstractCredentialsManager):
    def get_password(self, url, user, defer=True):
        return self._cp.get(url, 'pass', raw=True)

    def set_password(self, url, user, password):
        self._cp.set(url, 'pass', password)
        self._cp.set(url, self.config_entry, self._qualified_name())

    def delete_password(self, url, user):
        self._cp.remove_option(url, 'pass')

    def _process_options(self, options):
        if options is not None:
            raise RuntimeError('options must be None')


class PlaintextConfigFileDescriptor(AbstractCredentialsManagerDescriptor):
    def name(self):
        return 'Config file credentials manager'

    def description(self):
        return 'Store the credentials in the config file (plain text)'

    def create(self, cp):
        return PlaintextConfigFileCredentialsManager(cp, None)


class ObfuscatedConfigFileCredentialsManager(
        PlaintextConfigFileCredentialsManager):
    def get_password(self, url, user, defer=True):
        if self._cp.has_option(url, 'passx', proper=True):
            passwd = self._cp.get(url, 'passx', raw=True)
        else:
            passwd = super(self.__class__, self).get_password(url, user)
        return self.decode_password(passwd)

    def set_password(self, url, user, password):
        compressed_pw = bz2.compress(password.encode('ascii'))
        password = base64.b64encode(compressed_pw).decode("ascii")
        super(self.__class__, self).set_password(url, user, password)

    def delete_password(self, url, user):
        self._cp.remove_option(url, 'passx')
        super(self.__class__, self).delete_password(url, user)

    @classmethod
    def decode_password(cls, password):
        compressed_pw = base64.b64decode(password.encode("ascii"))
        return bz2.decompress(compressed_pw).decode("ascii")


class ObfuscatedConfigFileDescriptor(AbstractCredentialsManagerDescriptor):
    def name(self):
        return 'Obfuscated Config file credentials manager'

    def description(self):
        return 'Store the credentials in the config file (obfuscated)'

    def create(self, cp):
        return ObfuscatedConfigFileCredentialsManager(cp, None)


class TransientCredentialsManager(AbstractCredentialsManager):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self._password = None

    def _process_options(self, options):
        if options is not None:
            raise RuntimeError('options must be None')

    def get_password(self, url, user, defer=True):
        if defer:
            return self
        return self()

    def set_password(self, url, user, password):
        self._password = password
        self._cp.set(url, self.config_entry, self._qualified_name())

    def delete_password(self, url, user):
        self._password = None

    def __call__(self):
        if self._password is None:
            self._password = getpass.getpass('Password: ')
        return self._password


class TransientDescriptor(AbstractCredentialsManagerDescriptor):
    def name(self):
        return 'Transient password store'

    def description(self):
        return 'Do not store the password and always ask for the password'

    def create(self, cp):
        return TransientCredentialsManager(cp, None)


class KeyringCredentialsManager(AbstractCredentialsManager):
    def _process_options(self, options):
        if options is None:
            raise RuntimeError('options may not be None')
        self._backend_cls_name = options

    def _load_backend(self):
        keyring_backend = keyring.core.load_keyring(self._backend_cls_name)
        keyring.set_keyring(keyring_backend)

    @classmethod
    def create(cls, cp, options):
        if not has_keyring_support():
            return None
        return super(cls, cls).create(cp, options)

    def get_password(self, url, user, defer=True):
        self._load_backend()
        return keyring.get_password(urlsplit(url)[1], user)

    def set_password(self, url, user, password):
        self._load_backend()
        keyring.set_password(urlsplit(url)[1], user, password)
        config_value = self._qualified_name() + ':' + self._backend_cls_name
        self._cp.set(url, self.config_entry, config_value)

    def delete_password(self, url, user):
        self._load_backend()
        keyring.delete_password(urlsplit(url)[1], user)


r"""
keyctl cheat sheet
------------------

Show all keyrings.
Please note that the last column is a tree hierarchy.
$ keyctl show

    111 --alswrv   1000   100  keyring: _ses
    222 --alswrv   1000   100   \_ keyring: osc
    333 --alswrv   1000   100       \_ user: <user>@<host>:<port>


List keyrings in session keyring.
$ keyctl list @s

    222: --alswrv  1000   100 keyring: osc


Remove a key or a keyring from a parent.
$ keyctl unlink <id> <parent-id>


Create a new keyring under session keyring.
WARNING: Do not run this more than once, because it replaces any existing keyring with the same name.
$ keyctl newring osc @s


Resolve keyring name to ID.
$ keyctl request keyring osc

    222


Store a password.
$ echo -n "<password>" | keyctl padd user <user>@<host>:<port> <osc keyring id>
$ echo -n "opensuse" | keyctl padd user Admin@api.opensuse.org:443 222


Retrieve password id from a keyring.
$ keyctl request user <user>@<host>:<port> <osc keyring id>
$ keyctl request user Admin@api.opensuse.org:443 222

    444


Resolve retrieved password id to actual string.
$ keyctl print <password id>
$ keyctl print 444

    opensuse
"""


class KeyctlCredentialsManager(AbstractCredentialsManager):
    def __init__(self, cp, options):
        super(self.__class__, self).__init__(cp, options)

        # resolve keyring with name "osc" to ID
        cmd = ["keyctl", "request", "keyring", "osc"]
        returncode, stdout, _ = self._run(cmd)
        if returncode == 0:
            self.osc_keyring_id = stdout.strip()
            return

        # the previous command failed, let's create osc keyring under session keyring
        cmd = ["keyctl", "newring", "osc", "@s"]
        returncode, stdout, stderr = self._run(cmd)
        if returncode == 0:
            self.osc_keyring_id = stdout.strip()
            return

        raise RuntimeError("Unable to create 'osc' keyring: {}".format(stderr))

    def _get_key_desc(self, url, user):
        """
        Construct key description (which identifies the key in the keyring)
        based on apiurl (host, port) and user, because we want to store
        different credentials for each OBS instance.
        """
        splitted_url = urlsplit(url)
        scheme = splitted_url.scheme
        host = splitted_url.netloc
        port = splitted_url.port

        if not port:
            # always use port as part of key description
            if scheme == "http":
                port = 80
            else:
                port = 443

        return "{}@{}:{}".format(user, host, port)

    def _run(self, cmd, stdin=None):
        popen_kwargs = {}
        if stdin:
            stdin = stdin.encode("utf-8")
            popen_kwargs["stdin"] = subprocess.PIPE
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **popen_kwargs)
        stdout, stderr = proc.communicate(stdin)
        return proc.returncode, stdout.decode("utf-8"), stderr.decode("utf-8")

    def get_password(self, url, user, defer=True):
        if defer:
            def func():
                return self._get_password(url, user)
            return func
        return self._get_password(url, user)

    def _get_password(self, url, user):
        # get key_id for given key type and description
        cmd = ["keyctl", "request", "user", self._get_key_desc(url, user), self.osc_keyring_id]
        returncode, stdout, _ = self._run(cmd)

        if returncode != 0:
            # password not found in the keyring, ask user to provide one and then save it in the keyring
            password = getpass.getpass('Password for {}@{}: '.format(user, url))
            self.set_password(url, user, password)
            return password

        # password found in the keyring, use it
        key_id = stdout.strip()

        # resolve key_id into an actual password
        cmd = ["keyctl", "print", key_id]
        _, stdout, _ = self._run(cmd)
        password = stdout.strip()

        hex_prefix = ":hex:"
        if password.startswith(hex_prefix):
            # convert :hex:<hex-encoded-password> to utf-8 text
            hex_decoder = codecs.getdecoder("hex_codec")
            password = hex_decoder(password[len(hex_prefix):])[0].decode('utf-8')
        return password

    def set_password(self, url, user, password):
        cmd = ["keyctl", "padd", "user", self._get_key_desc(url, user), self.osc_keyring_id]
        # securely pass password through stdin
        self._run(cmd, stdin=password)

        # set credentials manager class in the config
        self._cp.set(url, self.config_entry, self._qualified_name())

    def delete_password(self, url, user):
        # get key_id for given key type and description
        cmd = ["keyctl", "request", "user", self._get_key_desc(url, user), self.osc_keyring_id]
        returncode, stdout, _ = self._run(cmd)

        if returncode != 0:
            # password not found in the keyring, nothing to delete
            return

        # password found in the keyring, use the id
        key_id = stdout.strip()

        # remove password from the 'osc' keyring
        cmd = ["keyctl", "unlink", "user", key_id, self.osc_keyring_id]
        self._run(cmd)


class KeyctlCredentialsDescriptor(AbstractCredentialsManagerDescriptor):
    def name(self):
        return 'Keyctl'

    def description(self):
        return 'Securely store keys in kernel keyring (in-memory, per user session)'

    def create(self, cp):
        return KeyctlCredentialsManager(cp, None)


class KeyringCredentialsDescriptor(AbstractCredentialsManagerDescriptor):
    def __init__(self, keyring_backend):
        self._keyring_backend = keyring_backend

    def name(self):
        if hasattr(self._keyring_backend, 'name'):
            return self._keyring_backend.name
        else:
            return self._keyring_backend.__class__.__name__

    def description(self):
        return 'Backend provided by python-keyring'

    def create(self, cp):
        qualified_backend_name = qualified_name(self._keyring_backend)
        return KeyringCredentialsManager(cp, qualified_backend_name)


class GnomeKeyringCredentialsManager(AbstractCredentialsManager):
    @classmethod
    def create(cls, cp, options):
        if gnomekeyring is None:
            return None
        return super(cls, cls).create(cp, options)

    def get_password(self, url, user, defer=True):
        gk_data = self._keyring_data(url, user)
        if gk_data is None:
            return None
        return gk_data['password']

    def set_password(self, url, user, password):
        scheme, host, path = self._urlsplit(url)
        gnomekeyring.set_network_password_sync(
            user=user,
            password=password,
            protocol=scheme,
            server=host,
            object=path)
        self._cp.set(url, self.config_entry, self._qualified_name())

    def delete_password(self, url, user):
        gk_data = self._keyring_data(url, user)
        if gk_data is None:
            return
        gnomekeyring.item_delete_sync(gk_data['keyring'], gk_data['item_id'])

    def get_user(self, url):
        gk_data = self._keyring_data(url, None)
        if gk_data is None:
            return None
        return gk_data['user']

    def _keyring_data(self, url, user):
        scheme, host, path = self._urlsplit(url)
        try:
            entries = gnomekeyring.find_network_password_sync(protocol=scheme,
                                                              server=host,
                                                              object=path)
        except gnomekeyring.NoMatchError:
            return None

        for entry in entries:
            if 'user' not in entry or 'password' not in entry:
                continue
            if user is None or entry['user'] == user:
                return entry
        return None

    def _urlsplit(self, url):
        splitted_url = urlsplit(url)
        return splitted_url.scheme, splitted_url.netloc, splitted_url.path


class GnomeKeyringCredentialsDescriptor(AbstractCredentialsManagerDescriptor):
    def name(self):
        return 'GNOME Keyring Manager (deprecated)'

    def description(self):
        return 'Deprecated GNOME Keyring Manager. If you use \
                this we will send you a Dial-In modem'

    def create(self, cp):
        return GnomeKeyringCredentialsManager(cp, None)


def get_credentials_manager_descriptors():
    if has_keyring_support():
        backend_list = keyring.backend.get_all_keyring()
    else:
        backend_list = []
    descriptors = []
    for backend in backend_list:
        descriptors.append(KeyringCredentialsDescriptor(backend))
    descriptors.sort()
    if gnomekeyring:
        descriptors.append(GnomeKeyringCredentialsDescriptor())
    descriptors.append(PlaintextConfigFileDescriptor())
    descriptors.append(ObfuscatedConfigFileDescriptor())
    descriptors.append(TransientDescriptor())
    descriptors.append(KeyctlCredentialsDescriptor())
    return descriptors


def get_keyring_credentials_manager(cp):
    keyring_backend = keyring.get_keyring()
    return KeyringCredentialsManager(cp, qualified_name(keyring_backend))


def create_credentials_manager(url, cp):
    config_entry = cp.get(url, AbstractCredentialsManager.config_entry)
    if ':' in config_entry:
        creds_mgr_cls, options = config_entry.split(':', 1)
    else:
        creds_mgr_cls = config_entry
        options = None
    mod, cls = creds_mgr_cls.rsplit('.', 1)
    return getattr(importlib.import_module(mod), cls).create(cp, options)


def qualified_name(obj):
    return obj.__module__ + '.' + obj.__class__.__name__


def has_keyring_support():
    return keyring is not None
