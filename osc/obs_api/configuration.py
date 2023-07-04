# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel
from .configuration_schedulers import ConfigurationSchedulers


class Configuration(xmlmodel.Model):
    TAG_NAME = "configuration"

    title: str = xmlmodel.TextNodeField(
        "title",
        help_text=(
            "short description of this OBS instance showed in the webui",
        ),
    )

    description: str = xmlmodel.TextNodeField(
        "description",
        help_text=(
            "long description of this OBS instance showed in the webui on the main page",
        ),
    )

    anonymous: Optional[str] = xmlmodel.TextNodeField(
        "anonymous",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "The webui (or other sites) can show the content of this OBS instance to not logged in users too.",
        ),
    )

    change_password: Optional[str] = xmlmodel.TextNodeField(
        "change_password",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "Users can change their password. This may not work with ldap or proxy_auth mechanisms.",
        ),
    )

    disallow_group_creation: Optional[str] = xmlmodel.TextNodeField(
        "disallow_group_creation",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "Disallow group creation via the API. Useful when groups are provided via LDAP.",
        ),
    )

    allow_user_to_create_home_project: Optional[str] = xmlmodel.TextNodeField(
        "allow_user_to_create_home_project",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "Users are allowed to create projects in their 'home:' namespace themselves.",
        ),
    )

    default_access_disabled: Optional[str] = xmlmodel.TextNodeField(
        "default_access_disabled",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "Newly created projects have access disabled by default.",
        ),
    )

    registration: Optional[str] = xmlmodel.TextNodeField(
        "registration",
        choices=('allow', 'confirmation', 'deny'),
        optional=True,
        help_text=(
            "New user can register themselves (allow) or they need approval after registration (confirmation) or accounts can only be created by the admin (deny).",
        ),
    )

    default_tracker: Optional[str] = xmlmodel.TextNodeField(
        "default_tracker",
        optional=True,
        help_text=(
            "Defines the default issue tracker to be used",
        ),
    )

    download_url: Optional[str] = xmlmodel.TextNodeField(
        "download_url",
        optional=True,
        help_text=(
            "Base URL of the published repositories.",
            "This url points to the root of the published repositories, all projects appear underneath it as follows: '$download_url/Foo:/Subproj:/repository_name'",
        ),
    )

    obs_url: Optional[str] = xmlmodel.TextNodeField(
        "obs_url",
        optional=True,
        help_text=(
            "The URL to this OBS instances webui as seen from outside.",
        ),
    )

    api_url: Optional[str] = xmlmodel.TextNodeField(
        "api_url",
        optional=True,
        help_text=(
            "API URL to be used by services.",
        ),
    )

    http_proxy: Optional[str] = xmlmodel.TextNodeField(
        "http_proxy",
        optional=True,
        help_text=(
            "May be used if external hosts, like remote OBS instances, gravatar or to download from external sides",
        ),
    )

    no_proxy: Optional[str] = xmlmodel.TextNodeField(
        "no_proxy",
        optional=True,
        help_text=(
            "A filter that specifies URLs that should be excluded from proxying.",
            "",
            "This should be a coma separated list like the environment variable 'NO_PROXY', e.g.: NO_PROXY="*.foo.com,bar.org,.startup.io"",
        ),
    )

    name: Optional[str] = xmlmodel.TextNodeField(
        "name",
        optional=True,
        help_text=(
            "This OBS instances' name. It is exposed as the '%DISTURL' macro when building rpms.",
        ),
    )

    download_on_demand: Optional[str] = xmlmodel.TextNodeField(
        "download_on_demand",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "EXPERIMENTAL: allows admins to use external package repositories in project repositories",
        ),
    )

    enforce_project_keys: Optional[str] = xmlmodel.TextNodeField(
        "enforce_project_keys",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "Always create a signing key when a project is created and no parent project has a key. Key removal is prohibited in that case.",
        ),
    )

    cleanup_empty_projects: Optional[str] = xmlmodel.TextNodeField(
        "cleanup_empty_projects",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "If the last package in a project is cleaned up via 'sourceupdate=cleanup', delete the whole project too?",
        ),
    )

    disable_publish_for_branches: Optional[str] = xmlmodel.TextNodeField(
        "disable_publish_for_branches",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "When a user creates a new project by branching a package, disable publishing for that project. The default is "on" to save disk space and bandwidth.",
        ),
    )

    ymp_url: Optional[str] = xmlmodel.TextNodeField(
        "ymp_url",
        optional=True,
        help_text=(
            "URL prefix for one-click installation files (software.opensuse.org)",
        ),
    )

    bugzilla_url: Optional[str] = xmlmodel.TextNodeField(
        "bugzilla_url",
        optional=True,
        help_text=(
            "Default bugzilla instance for reporting to bugowners",
        ),
    )

    tos_url: Optional[str] = xmlmodel.TextNodeField(
        "tos_url",
        optional=True,
        help_text=(
            "URL to link to a Terms of Service page",
        ),
    )

    admin_email: Optional[str] = xmlmodel.TextNodeField(
        "admin_email",
        optional=True,
        help_text=(
            "Email address to contact the admin of this OBS instance.",
        ),
    )

    theme: Optional[str] = xmlmodel.TextNodeField(
        "theme",
        optional=True,
        help_text=(
            "The webui theme",
        ),
    )

    cleanup_after_days: Optional[str] = xmlmodel.TextNodeField(
        "cleanup_after_days",
        optional=True,
        help_text=(
            "Enables delete requests for branched projects after given number of days.",
        ),
    )

    gravatar: Optional[str] = xmlmodel.TextNodeField(
        "gravatar",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "Load user's profile pictures from Gravatar.",
        ),
    )

    hide_private_options: Optional[str] = xmlmodel.TextNodeField(
        "hide_private_options",
        choices=('on', 'off'),
        optional=True,
        help_text=(
            "Do not show the options to hide projects or packages.",
        ),
    )

    unlisted_projects_filter: Optional[str] = xmlmodel.TextNodeField(
        "unlisted_projects_filter",
        optional=True,
        help_text=(
            "Regular expression for projects that should be hidden (e.g.: '^home:.*').",
        ),
    )

    unlisted_projects_filter_description: Optional[str] = xmlmodel.TextNodeField(
        "unlisted_projects_filter_description",
        optional=True,
        help_text=(
            "The description that will appear in the project list explaining the exclusion filter.",
        ),
    )

    schedulers: ConfigurationSchedulers = xmlmodel.ModelField(
        "schedulers",
        model_class=ConfigurationSchedulers,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
