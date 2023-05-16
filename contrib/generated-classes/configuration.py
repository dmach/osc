from typing import List
from typing import Type

from . import _base


class Configuration(_base.ApiEndPointBase):
    pass

    _elements: List[str] = ['title', 'description', 'anonymous', 'change_password', 'disallow_group_creation', 'allow_user_to_create_home_project', 'default_access_disabled', 'registration', 'default_tracker', 'download_url', 'obs_url', 'api_url', 'http_proxy', 'no_proxy', 'name', 'download_on_demand', 'enforce_project_keys', 'cleanup_empty_projects', 'disable_publish_for_branches', 'ymp_url', 'bugzilla_url', 'tos_url', 'admin_email', 'theme', 'cleanup_after_days', 'gravatar', 'hide_private_options', 'unlisted_projects_filter', 'unlisted_projects_filter_description', 'schedulers']
# {'doc': 'short description of this OBS instance showed in the webui'}

    @property
    def title(self) -> str:
        """
        short description of this OBS instance showed in the webui
        """
        return self._get_element("title")

    @title.setter
    def title(self, value: str):
        self._set_element("title", value)

    @title.deleter
    def title(self):
        self._delete_element("title")
# {'doc': 'long description of this OBS instance showed in the webui on the main page'}

    @property
    def description(self) -> str:
        """
        long description of this OBS instance showed in the webui on the main page
        """
        return self._get_element("description")

    @description.setter
    def description(self, value: str):
        self._set_element("description", value)

    @description.deleter
    def description(self):
        self._delete_element("description")
# {'optional': '1', 'doc': 'The webui (or other sites) can show the content of this OBS instance to not logged in users too.', 'choices': {'values': ['on', 'off']}}

    _anonymous_is_optional: bool = True
    _anonymous_choices: List[str] = ['on', 'off']

    @property
    def anonymous(self) -> str:
        """
        The webui (or other sites) can show the content of this OBS instance to not logged in users too.
        """
        return self._get_element("anonymous")

    @anonymous.setter
    def anonymous(self, value: str):
        self._set_element("anonymous", value)

    @anonymous.deleter
    def anonymous(self):
        self._delete_element("anonymous")
# {'optional': '1', 'doc': 'Users can change their password. This may not work with ldap or proxy_auth mechanisms.', 'choices': {'values': ['on', 'off']}}

    _change_password_is_optional: bool = True
    _change_password_choices: List[str] = ['on', 'off']

    @property
    def change_password(self) -> str:
        """
        Users can change their password. This may not work with ldap or proxy_auth mechanisms.
        """
        return self._get_element("change_password")

    @change_password.setter
    def change_password(self, value: str):
        self._set_element("change_password", value)

    @change_password.deleter
    def change_password(self):
        self._delete_element("change_password")
# {'optional': '1', 'doc': 'Disallow group creation via the API. Useful when groups are provided via LDAP.', 'choices': {'values': ['on', 'off']}}

    _disallow_group_creation_is_optional: bool = True
    _disallow_group_creation_choices: List[str] = ['on', 'off']

    @property
    def disallow_group_creation(self) -> str:
        """
        Disallow group creation via the API. Useful when groups are provided via LDAP.
        """
        return self._get_element("disallow_group_creation")

    @disallow_group_creation.setter
    def disallow_group_creation(self, value: str):
        self._set_element("disallow_group_creation", value)

    @disallow_group_creation.deleter
    def disallow_group_creation(self):
        self._delete_element("disallow_group_creation")
# {'optional': '1', 'doc': "Users are allowed to create projects in their 'home:' namespace themselves.", 'choices': {'values': ['on', 'off']}}

    _allow_user_to_create_home_project_is_optional: bool = True
    _allow_user_to_create_home_project_choices: List[str] = ['on', 'off']

    @property
    def allow_user_to_create_home_project(self) -> str:
        """
        Users are allowed to create projects in their 'home:' namespace themselves.
        """
        return self._get_element("allow_user_to_create_home_project")

    @allow_user_to_create_home_project.setter
    def allow_user_to_create_home_project(self, value: str):
        self._set_element("allow_user_to_create_home_project", value)

    @allow_user_to_create_home_project.deleter
    def allow_user_to_create_home_project(self):
        self._delete_element("allow_user_to_create_home_project")
# {'optional': '1', 'doc': 'Newly created projects have access disabled by default.', 'choices': {'values': ['on', 'off']}}

    _default_access_disabled_is_optional: bool = True
    _default_access_disabled_choices: List[str] = ['on', 'off']

    @property
    def default_access_disabled(self) -> str:
        """
        Newly created projects have access disabled by default.
        """
        return self._get_element("default_access_disabled")

    @default_access_disabled.setter
    def default_access_disabled(self, value: str):
        self._set_element("default_access_disabled", value)

    @default_access_disabled.deleter
    def default_access_disabled(self):
        self._delete_element("default_access_disabled")
# {'optional': '1', 'doc': 'New user can register themselves (allow) or they need approval after registration (confirmation) or accounts can only be created by the admin (deny).', 'choices': {'values': ['allow', 'confirmation', 'deny']}}

    _registration_is_optional: bool = True
    _registration_choices: List[str] = ['allow', 'confirmation', 'deny']

    @property
    def registration(self) -> str:
        """
        New user can register themselves (allow) or they need approval after registration (confirmation) or accounts can only be created by the admin (deny).
        """
        return self._get_element("registration")

    @registration.setter
    def registration(self, value: str):
        self._set_element("registration", value)

    @registration.deleter
    def registration(self):
        self._delete_element("registration")
# {'optional': '1', 'doc': 'Defines the default issue tracker to be used'}

    _default_tracker_is_optional: bool = True

    @property
    def default_tracker(self) -> str:
        """
        Defines the default issue tracker to be used
        """
        return self._get_element("default_tracker")

    @default_tracker.setter
    def default_tracker(self, value: str):
        self._set_element("default_tracker", value)

    @default_tracker.deleter
    def default_tracker(self):
        self._delete_element("default_tracker")
# {'optional': '1', 'doc': "Base URL of the published repositories.\nThis url points to the root of the published repositories, all projects appear underneath it as follows: '$download_url/Foo:/Subproj:/repository_name'"}

    _download_url_is_optional: bool = True

    @property
    def download_url(self) -> str:
        """
        Base URL of the published repositories.
        This url points to the root of the published repositories, all projects appear underneath it as follows: '$download_url/Foo:/Subproj:/repository_name'
        """
        return self._get_element("download_url")

    @download_url.setter
    def download_url(self, value: str):
        self._set_element("download_url", value)

    @download_url.deleter
    def download_url(self):
        self._delete_element("download_url")
# {'optional': '1', 'doc': 'The URL to this OBS instances webui as seen from outside.'}

    _obs_url_is_optional: bool = True

    @property
    def obs_url(self) -> str:
        """
        The URL to this OBS instances webui as seen from outside.
        """
        return self._get_element("obs_url")

    @obs_url.setter
    def obs_url(self, value: str):
        self._set_element("obs_url", value)

    @obs_url.deleter
    def obs_url(self):
        self._delete_element("obs_url")
# {'optional': '1', 'doc': 'API URL to be used by services.'}

    _api_url_is_optional: bool = True

    @property
    def api_url(self) -> str:
        """
        API URL to be used by services.
        """
        return self._get_element("api_url")

    @api_url.setter
    def api_url(self, value: str):
        self._set_element("api_url", value)

    @api_url.deleter
    def api_url(self):
        self._delete_element("api_url")
# {'optional': '1', 'doc': 'May be used if external hosts, like remote OBS instances, gravatar or to download from external sides'}

    _http_proxy_is_optional: bool = True

    @property
    def http_proxy(self) -> str:
        """
        May be used if external hosts, like remote OBS instances, gravatar or to download from external sides
        """
        return self._get_element("http_proxy")

    @http_proxy.setter
    def http_proxy(self, value: str):
        self._set_element("http_proxy", value)

    @http_proxy.deleter
    def http_proxy(self):
        self._delete_element("http_proxy")
# {'optional': '1', 'doc': 'A filter that specifies URLs that should be excluded from proxying.\n\nThis should be a coma separated list like the environment variable \'NO_PROXY\', e.g.: NO_PROXY="*.foo.com,bar.org,.startup.io"'}

    _no_proxy_is_optional: bool = True

    @property
    def no_proxy(self) -> str:
        """
        A filter that specifies URLs that should be excluded from proxying.

        This should be a coma separated list like the environment variable 'NO_PROXY', e.g.: NO_PROXY="*.foo.com,bar.org,.startup.io"
        """
        return self._get_element("no_proxy")

    @no_proxy.setter
    def no_proxy(self, value: str):
        self._set_element("no_proxy", value)

    @no_proxy.deleter
    def no_proxy(self):
        self._delete_element("no_proxy")
# {'optional': '1', 'doc': "This OBS instances' name. It is exposed as the '%DISTURL' macro when building rpms."}

    _name_is_optional: bool = True

    @property
    def name(self) -> str:
        """
        This OBS instances' name. It is exposed as the '%DISTURL' macro when building rpms.
        """
        return self._get_element("name")

    @name.setter
    def name(self, value: str):
        self._set_element("name", value)

    @name.deleter
    def name(self):
        self._delete_element("name")
# {'optional': '1', 'doc': 'EXPERIMENTAL: allows admins to use external package repositories in project repositories', 'choices': {'values': ['on', 'off']}}

    _download_on_demand_is_optional: bool = True
    _download_on_demand_choices: List[str] = ['on', 'off']

    @property
    def download_on_demand(self) -> str:
        """
        EXPERIMENTAL: allows admins to use external package repositories in project repositories
        """
        return self._get_element("download_on_demand")

    @download_on_demand.setter
    def download_on_demand(self, value: str):
        self._set_element("download_on_demand", value)

    @download_on_demand.deleter
    def download_on_demand(self):
        self._delete_element("download_on_demand")
# {'optional': '1', 'doc': 'Always create a signing key when a project is created and no parent project has a key. Key removal is prohibited in that case.', 'choices': {'values': ['on', 'off']}}

    _enforce_project_keys_is_optional: bool = True
    _enforce_project_keys_choices: List[str] = ['on', 'off']

    @property
    def enforce_project_keys(self) -> str:
        """
        Always create a signing key when a project is created and no parent project has a key. Key removal is prohibited in that case.
        """
        return self._get_element("enforce_project_keys")

    @enforce_project_keys.setter
    def enforce_project_keys(self, value: str):
        self._set_element("enforce_project_keys", value)

    @enforce_project_keys.deleter
    def enforce_project_keys(self):
        self._delete_element("enforce_project_keys")
# {'optional': '1', 'doc': "If the last package in a project is cleaned up via 'sourceupdate=cleanup', delete the whole project too?", 'choices': {'values': ['on', 'off']}}

    _cleanup_empty_projects_is_optional: bool = True
    _cleanup_empty_projects_choices: List[str] = ['on', 'off']

    @property
    def cleanup_empty_projects(self) -> str:
        """
        If the last package in a project is cleaned up via 'sourceupdate=cleanup', delete the whole project too?
        """
        return self._get_element("cleanup_empty_projects")

    @cleanup_empty_projects.setter
    def cleanup_empty_projects(self, value: str):
        self._set_element("cleanup_empty_projects", value)

    @cleanup_empty_projects.deleter
    def cleanup_empty_projects(self):
        self._delete_element("cleanup_empty_projects")
# {'optional': '1', 'doc': 'When a user creates a new project by branching a package, disable publishing for that project. The default is "on" to save disk space and bandwidth.', 'choices': {'values': ['on', 'off']}}

    _disable_publish_for_branches_is_optional: bool = True
    _disable_publish_for_branches_choices: List[str] = ['on', 'off']

    @property
    def disable_publish_for_branches(self) -> str:
        """
        When a user creates a new project by branching a package, disable publishing for that project. The default is "on" to save disk space and bandwidth.
        """
        return self._get_element("disable_publish_for_branches")

    @disable_publish_for_branches.setter
    def disable_publish_for_branches(self, value: str):
        self._set_element("disable_publish_for_branches", value)

    @disable_publish_for_branches.deleter
    def disable_publish_for_branches(self):
        self._delete_element("disable_publish_for_branches")
# {'optional': '1', 'doc': 'URL prefix for one-click installation files (software.opensuse.org)'}

    _ymp_url_is_optional: bool = True

    @property
    def ymp_url(self) -> str:
        """
        URL prefix for one-click installation files (software.opensuse.org)
        """
        return self._get_element("ymp_url")

    @ymp_url.setter
    def ymp_url(self, value: str):
        self._set_element("ymp_url", value)

    @ymp_url.deleter
    def ymp_url(self):
        self._delete_element("ymp_url")
# {'optional': '1', 'doc': 'Default bugzilla instance for reporting to bugowners'}

    _bugzilla_url_is_optional: bool = True

    @property
    def bugzilla_url(self) -> str:
        """
        Default bugzilla instance for reporting to bugowners
        """
        return self._get_element("bugzilla_url")

    @bugzilla_url.setter
    def bugzilla_url(self, value: str):
        self._set_element("bugzilla_url", value)

    @bugzilla_url.deleter
    def bugzilla_url(self):
        self._delete_element("bugzilla_url")
# {'optional': '1', 'doc': 'URL to link to a Terms of Service page'}

    _tos_url_is_optional: bool = True

    @property
    def tos_url(self) -> str:
        """
        URL to link to a Terms of Service page
        """
        return self._get_element("tos_url")

    @tos_url.setter
    def tos_url(self, value: str):
        self._set_element("tos_url", value)

    @tos_url.deleter
    def tos_url(self):
        self._delete_element("tos_url")
# {'optional': '1', 'doc': 'Email address to contact the admin of this OBS instance.'}

    _admin_email_is_optional: bool = True

    @property
    def admin_email(self) -> str:
        """
        Email address to contact the admin of this OBS instance.
        """
        return self._get_element("admin_email")

    @admin_email.setter
    def admin_email(self, value: str):
        self._set_element("admin_email", value)

    @admin_email.deleter
    def admin_email(self):
        self._delete_element("admin_email")
# {'optional': '1', 'doc': 'The webui theme'}

    _theme_is_optional: bool = True

    @property
    def theme(self) -> str:
        """
        The webui theme
        """
        return self._get_element("theme")

    @theme.setter
    def theme(self, value: str):
        self._set_element("theme", value)

    @theme.deleter
    def theme(self):
        self._delete_element("theme")
# {'optional': '1', 'doc': 'Enables delete requests for branched projects after given number of days.'}

    _cleanup_after_days_is_optional: bool = True

    @property
    def cleanup_after_days(self) -> str:
        """
        Enables delete requests for branched projects after given number of days.
        """
        return self._get_element("cleanup_after_days")

    @cleanup_after_days.setter
    def cleanup_after_days(self, value: str):
        self._set_element("cleanup_after_days", value)

    @cleanup_after_days.deleter
    def cleanup_after_days(self):
        self._delete_element("cleanup_after_days")
# {'optional': '1', 'doc': "Load user's profile pictures from Gravatar.", 'choices': {'values': ['on', 'off']}}

    _gravatar_is_optional: bool = True
    _gravatar_choices: List[str] = ['on', 'off']

    @property
    def gravatar(self) -> str:
        """
        Load user's profile pictures from Gravatar.
        """
        return self._get_element("gravatar")

    @gravatar.setter
    def gravatar(self, value: str):
        self._set_element("gravatar", value)

    @gravatar.deleter
    def gravatar(self):
        self._delete_element("gravatar")
# {'optional': '1', 'doc': 'Do not show the options to hide projects or packages.', 'choices': {'values': ['on', 'off']}}

    _hide_private_options_is_optional: bool = True
    _hide_private_options_choices: List[str] = ['on', 'off']

    @property
    def hide_private_options(self) -> str:
        """
        Do not show the options to hide projects or packages.
        """
        return self._get_element("hide_private_options")

    @hide_private_options.setter
    def hide_private_options(self, value: str):
        self._set_element("hide_private_options", value)

    @hide_private_options.deleter
    def hide_private_options(self):
        self._delete_element("hide_private_options")
# {'optional': '1', 'doc': "Regular expression for projects that should be hidden (e.g.: '^home:.*')."}

    _unlisted_projects_filter_is_optional: bool = True

    @property
    def unlisted_projects_filter(self) -> str:
        """
        Regular expression for projects that should be hidden (e.g.: '^home:.*').
        """
        return self._get_element("unlisted_projects_filter")

    @unlisted_projects_filter.setter
    def unlisted_projects_filter(self, value: str):
        self._set_element("unlisted_projects_filter", value)

    @unlisted_projects_filter.deleter
    def unlisted_projects_filter(self):
        self._delete_element("unlisted_projects_filter")
# {'optional': '1', 'doc': 'The description that will appear in the project list explaining the exclusion filter.'}

    _unlisted_projects_filter_description_is_optional: bool = True

    @property
    def unlisted_projects_filter_description(self) -> str:
        """
        The description that will appear in the project list explaining the exclusion filter.
        """
        return self._get_element("unlisted_projects_filter_description")

    @unlisted_projects_filter_description.setter
    def unlisted_projects_filter_description(self, value: str):
        self._set_element("unlisted_projects_filter_description", value)

    @unlisted_projects_filter_description.deleter
    def unlisted_projects_filter_description(self):
        self._delete_element("unlisted_projects_filter_description")
# {'elements': {'arch': {'list': '0+', 'ref': 'build-arch'}}}

    _schedulers_elements: List[str] = ['arch']

    @property
    def schedulers(self) -> str:
        return self._get_element("schedulers")

    @schedulers.setter
    def schedulers(self, value: str):
        self._set_element("schedulers", value)

    @schedulers.deleter
    def schedulers(self):
        self._delete_element("schedulers")
