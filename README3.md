## Intro

`osc` is written in Python, and in addition to the command-line
interface, it also provides a Python module for use by other Python
programs.

`osc` is a client with a command-line interface and network behavior in
the style of Subversion. It serves as client for the source code
repository component of the Build Service, and it is used to edit
metadata or query about build results.


## Downloading and installing

`osc` is included in recent versions of the openSUSE Linux distribution.
Just run

    sudo zypper in osc

to get hold of it. Newer versions, if you really deem it necessary, may
be found at [openSUSE tools
repository](http://download.opensuse.org/repositories/openSUSE:/Tools/),
where there are also packages for various other distributions (SLES,
Fedora, Mandriva, Debian, etc.). If you want to check out even more
recent code, you can do so with Git:

    git clone git://github.com/openSUSE/osc

For `osc` to work,
[python-xml](http://software.opensuse.org/search?q=python-xml) is
required and if it is not already pulled in by way of zypper (such as
when going the git route directly), you may need to install it
afterward.


## Walk-through


### Authentication

You need an openSUSE account for <https://build.opensuse.org>. It is the
same account for all this sites:

-   <https://build.opensuse.org>
-   <https://events.opensuse.org>
-   <https://features.opensuse.org>
-   <https://progress.opensuse.org>

If you already have an account for one of these sites, you can use it.
If not, you need to create one by clicking on *Sign Up* or in the
[idp-portal](https://idp-portal.suse.com/).

`osc` will ask you for your credentials when you use it for the first
time, and will store them in `~/.config/osc/oscrc`. The password is
stored in plain text. Protect your `~/.config/osc/oscrc` file and your
filesystem appropriately. (In older versions it was stored in `~/.oscrc`)

1</code> in file \~/.config/osc/oscrc `[general]` section (depending
from your osc version).}}

There have been reports that with `python-keyring` and the changes above
in the `~/.config/osc/oscrc` the authentication with Gnome keyring is not
working. In such cases it helped to uninstall `python-keyring` and add
solely the line `gnome_keyring=1` instead of `keyring=1` to the server
section.


### Recommended starter configuration

If you are new using osc, try this configuration.

Edit the file `~/.config/osc/oscrc`, find, uncomment and set this
values:

    # compile with N jobs (default: "getconf _NPROCESSORS_ONLN")
    build-jobs = 2

    # extra packages to install when building packages locally (osc build)
    # this corresponds to osc build's -x option and can be overridden with that
    # -x '' can also be given on the command line to override this setting, or
    # you can have an empty setting here.
    extra-pkgs = gdb less mc strace tmux tree unzip vim

    # Skip signature verification of packages used for build.
    no_verify = 1

    [https://api.opensuse.org]
    user = your_user
    pass = your-password
    email = your@mail.com
    aliases = obs

Edit your \~/.bashrc, add as the last line:

    export COMP_WORDBREAKS=${COMP_WORDBREAKS/:/}

Edit your `~/.alias` (this file may not exist, simply create it), add
these aliases:

    alias oscb="osc build --ccache"
    alias oscsd="osc service runall download_files"


### Usage examples

Introductory usage examples are shown below.
Note the [Build Service Tutorial](https://en.opensuse.org/openSUSE:Build_Service_Tutorial),
which gives a more systematic introduction.

Show usage info on a command

    osc help
    osc help <cmd>

List existing content on the server

    osc ls                          # list projects
    osc ls Apache                   # list packages in a project
    osc ls Apache subversion        # list files of package of a project

Check out content

    osc co Apache                   # entire project
    osc co Apache subversion        # a package
    osc co Apache subversion foo    # single file

Update a working directory

    osc up
    osc up <directory>
    osc up *                        # from within a project dir, update all packages
    osc up                          # from within a project dir, update all packages
                                      AND check out all newly added packages

Upload changed content

    osc ci                          # current dir
    osc ci <file1> <file2>          # only specific files
    osc ci <dir1> <dir2> ...        # multiple packages
    osc ci -m "updated foobar"      # specify a commit message

See the commit log

    osc log

Show the status (which files have been changed locally)

    osc st
    osc st <directory>

If an update cannot be merged automatically, a file is in 'C' (conflict)
state, and conflicts are marked with special `<<<<<<<` and `>>>>>>>`
lines. After manually resolving the problem, use

    osc resolved <file>

Mark files to be added or removed on the next 'checkin'

    osc add foo
    osc rm foo

Add all new files in local copy and removes all disappeared files.

    osc addremove

Generate a diff to view the changes

    osc diff [file]

Show the build results of the package

    osc results
    osc results <platform>

Show the log file of a package (you need to be inside a package
directory)

    osc buildlog <platform> <arch>

Show the URLs of .repo files which are packages sources for
Yum/YaST/smart

    osc repourls [dir]

Trigger a package rebuild for all repositories/architectures of a
package

    osc rebuildpac [dir]

Build a package on your local plattform

    osc build <platform> <arch> <specfile> [--clean|--noinit|...]

Show the configured platforms/build targets.

    osc platforms [project]

Show the possible build targets for your project.

    osc repos

Show meta information

    osc meta prj <project>
    osc meta pkg <project> <package>
    osc meta user <username>
    osc meta prjconf <project>

Edit meta information. Creates new package/project if it doesn't exist.
It will open an Editor with the raw XML metadata. If unsure about XML,
you can use the [web client](http://build.opensuse.org) instead.

    osc meta prj -e <project>
    osc meta pkg -e <project> <package>
    osc meta prjconf -e <project>

(The project configuration (prjconf) may well be empty. It is needed in
special cases only.)

Update package meta data with metadata taken from spec file

    osc updatepacmetafromspec <dir>

Download files referenced via source URL in the specfile.

    osc service runall download_files


## Package tracking

With osc it is also possible to manage packages in a svn like way. This
feature is called package tracking and has to be enabled in `~/.oscrc`'s
\[general\] section

    # manage your packages in a svn like way
    do_package_tracking = 1

Add a new package to a project

    osc mkpac <package>

Add an already existing directory and its files to a project

    osc add <directory>

Remove a package and its files from a project

    osc deletepac <package>

All the commands above only change your local working copy. To submit
your changes to the buildservice you have to commit them

    osc ci -m <message>

The `status` command also displays the state of the packages

    osc st


## Documentation

Besides a manual page for osc, a [cheat sheet](Media:Obs-cheat-sheet.pdf "wikilink") is available as well.

How to fix a none factory package?

Check out the package of your choice:

Fix it and after you have verified that the package builds submit it:


## Extending osc via plugins

osc is [extensible](openSUSE:OSC_plugins "wikilink"). You can modify the
behavior or write your own commands. See [openSUSE:OSC
plugins](openSUSE:OSC_plugins "wikilink") for more information.


## Configuration migration

Version 0.114 got some cleanups for the configfile handling and
therefore some options are now deprecated, namely:

-   apisrv
-   scheme

One new option was added:

-   apiurl = <protocol>://<somehost> # use this as the default apiurl. If this option isn't specified the default (https://api.opensuse.org) is used.

So far osc still has some backward compatibility for these options but
it might get removed in the future that's why it issues a deprecation
warning in case one of those options is still in use. The new
configuration scheme looks like the following:

    # entry for an apiurl
    [<protocol>://<apiurl>]
    user = <username>
    password = <password>
    ...

**Before starting the migration please save your \~/.oscrc file!**

If the migration doesn't work for whatever reason feel free to send me
an email or ask on the opensuse-buildservice mailinglist or in the
#opensuse-buildservice irc channel.


### Migration case I (apisrv only)

The apisrv option is used to specify the default apihost. If apisrv
isn't specified at all the default ("api.opensuse.org") is used. The
current \[general\] section looks like this:

    [general]
    ...
    apisrv = <somehost>
    # or
    apisrv = <protocol>://<somehost>

apisrv got superseded by the new apiurl option which looks like this:

    [general]
    ...
    apiurl = <protocol>://<somehost>

If apisrv has no "<protocol>" https is used. Make sure all apiurl
sections have the new format which is described above. Afterwards apisrv
can be removed.


### Migration case II (scheme only)

The current \[general\] section looks like this:

    [general]
    ...
    scheme = <protocol>

This means every apiurl section which don't have the new format which is
described above for instance

    [<somehost>]
    user = <username>
    password = <password>
    ...

has to be converted to

    [<protocol>://<somehost>]
    user = <username>
    password = <password>
    ...

Afterwards the scheme option can be removed from the \[general\] section
(it might be the case that some sections already have the correct
format).


### Migration case III (apisrv and scheme)

The current \[general\] section looks like this:

    [general]
    ...
    apisrv = <somehost>
    scheme = <protocol>

Both options can be removed if all apiurl sections have the new format
which is described above. So basically just adjust all apiurl sections
(it might be the case that some sections already have the correct
format).


## osc build with xen

You'll need to have xen packages and xen kernel installed and booted to
proceed. To activate local builds with xen, you'll have to add these
lines to section \[general\] of your \~/.oscrc:

    build-type=xen
    build-device=/tmp/FILE.root
    build-swap=/tmp/FILE.swap
    build-memory=512

Then create the 2 files:

    dd if=/dev/zero of=/tmp/FILE.root bs=1M count=4096  # 4GB partition for / . On big projects 8GB should be used.
    mkfs.ext3 /tmp/FILE.root                            # Hit (y) if it complains about the file not being a device node.
    dd if=/dev/zero of=/tmp/FILE.swap bs=1M count=512   # use other sizes as needed
    mkswap /tmp/FILE.swap

If you change the size or filesystem type of the files you may also need
to update the build-vmdisk-\* options.

If you want to use the cross-compilation feature, you'll have to add to
your /etc/sysconfig/kernel:

-   binfmt_misc to INITRD_MODULES
-   binfmt_misc to DOMU_INITRD_MODULES
-   binfmt_misc to MODULES_LOADED_ON_BOOT

Recreate the initrd's with mkinitrd.

Run osc build.


## Configuration cheatsheet for \~/.config/osc/oscrc (in older versions \~/.oscrc)

### The \[general\] section

Storage:

    # Downloaded packages are cached here. Must be writable by you.
    # default:
    packagecachedir = /var/tmp/osbuild-packagecache

    # rootdir to setup the chroot environment
    # can contain %(repo)s and/or %(arch)s for replacement
    # /<path>/%(repo)s-%(arch)s-%(project)s-%(package)s
    # default:
    build-root = /var/tmp/build-root/

API communication:

    # use this API server (hostname[:port])
    # (it needs a section [api.opensuse.org] with the credentials)
    # default:
    apisrv = api.opensuse.org

    # use this protocol to access the API server (http or https)
    # default:
    scheme = https

API host:

    # API hosts can be referenced by aliases, e.g. 'osc -A alias ...'
    # List aliases for API hosts under the API host section.
    # [https://api.opensuse.org](https://api.opensuse.org)
    # user=jdoe
    # aliases=

Local build:

    # Wrapper to call build as root (sudo, su -, ...)
    # default:
    su-wrapper = su -c
    # no password required with:
    #su-wrapper = sudo
    #with entry in sudoers file:
    # <username> ALL = NOPASSWD: /usr/bin/build

    # For convenience/debugging, osc adds internally vim gdb strace to
    # the packages installed in the build chroot if extra-pkgs is not set to:
    #extra-pkgs=

    # build type - possibe values:
    #  * empty -> chroot
    #  * xen -> xen VM
    #  * kvm -> kvm VM (testing needed)
    # default: not set/chroot
    #build-type=xen

    # build-device - root filesystem to use for VM
    # default: not set
    #build-device=/tmp/FILE.root

    # build-swap - swap filesystem to use for VM
    # default: not set
    #build-swap=/tmp/FILE.swap

    # build-memory - amount of memory for VM
    # default: not set
    #build-memory=512


## Contributing: bug reports, development etc.

Development happens at: <https://github.com/openSUSE/osc>

Please file new issues at: <https://github.com/openSUSE/osc/issues/new>
