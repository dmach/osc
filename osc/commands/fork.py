import sys
import urllib.parse

import osc.commandline
import osc.commandline_git


class ForkCommand(osc.commandline.OscCommand):
    """
    Fork a project or a package with sources managed in Gitea
    """

    name = "fork"

    # inject some git-obs methods to avoid duplicating code
    add_argument_new_repo_name = osc.commandline_git.GitObsCommand.add_argument_new_repo_name
    post_parse_args = osc.commandline_git.GitObsMainCommand.post_parse_args
    print_gitea_settings = osc.commandline_git.GitObsCommand.print_gitea_settings

    def init_arguments(self):
        # inherit global options from the main git-obs command
        osc.commandline_git.GitObsMainCommand.init_arguments(self)

        self.add_argument(
            "project",
            help="Name of the project",
        )

        self.add_argument(
            "package",
            nargs="?",
            help="Name of the package",
        )

        self.add_argument(
            "--target-project",
            help="Name of the target project (defaults to home:$user:branches)",
        )

        self.add_argument(
            "--target-package",
            help="Name of the package (defaults to $package)",
        )

        self.add_argument_new_repo_name()

    def run(self, args):
        from osc import conf as osc_conf
        from osc import gitea_api
        from osc import obs_api
        from osc.output import tty

        is_package = args.package is not None

        if not is_package and args.target_package:
            self.parser.error("The '--target-package' option requires the 'package' argument to be set")

        if is_package:
            # get the package meta from the OBS API first
            package = obs_api.Package.from_api(args.apiurl, args.project, args.package)
            if not package.scmsync:
                raise RuntimeError(
                    "Forking is possible only with packages managed in Git (the <scmsync> element must be set in the package meta)"
                )
        else:
            # get the project meta from the OBS API first
            project = obs_api.Project.from_api(args.apiurl, args.project)
            if not project.scmsync:
                raise RuntimeError(
                    "Forking is possible only with projects managed in Git (the <scmsync> element must be set in the project meta)"
                )

        # parse gitea url, owner, repo and branch from the scmsync url
        if is_package:
            parsed_scmsync_url = urllib.parse.urlparse(package.scmsync, scheme="https")
        else:
            parsed_scmsync_url = urllib.parse.urlparse(project.scmsync, scheme="https")
        url = urllib.parse.urlunparse((parsed_scmsync_url.scheme, parsed_scmsync_url.netloc, "", "", "", ""))
        owner, repo = parsed_scmsync_url.path.strip("/").split("/")
        branch = parsed_scmsync_url.fragment or None

        # find a credentials entry for url and OBS user (there can be multiple users configured for a single URL in the config file)
        gitea_conf = gitea_api.Config(args.gitea_config)
        gitea_login = gitea_conf.get_login_by_url_user(url=url, user=osc_conf.get_apiurl_usr(args.apiurl))
        gitea_conn = gitea_api.Connection(gitea_login)

        # store the attributes for self.print_gitea_settings()
        self.gitea_conf = gitea_conf
        self.gitea_login = gitea_login
        self.gitea_conn = gitea_conn

        self.print_gitea_settings()
        print(f"Forking git repo {owner}/{repo} ...", file=sys.stderr)

        # the branch was not specified, fetch the default branch from the repo
        if branch:
            fork_branch = branch
        else:
            repo_data = gitea_api.Repo.get(gitea_conn, owner, repo).json()
            branch = repo_data["default_branch"]
            fork_branch = branch

        # check if the scmsync branch exists in the source repo
        parent_branch_data = gitea_api.Branch.get(gitea_conn, owner, repo, fork_branch).json()

        try:
            repo_data = gitea_api.Fork.create(gitea_conn, owner, repo, new_repo_name=args.new_repo_name).json()
            fork_owner = repo_data["owner"]["login"]
            fork_repo = repo_data["name"]
            print(f" * Fork created: {fork_owner}/{fork_repo}")
        except gitea_api.ForkExists as e:
            fork_owner = e.fork_owner
            fork_repo = e.fork_repo
            print(f" * Fork already exists: {fork_owner}/{fork_repo}")

        # XXX: implicit branch name should be forbidden; assumptions are bad
        fork_scmsync = urllib.parse.urlunparse(
            (parsed_scmsync_url.scheme, parsed_scmsync_url.netloc, f"{fork_owner}/{fork_repo}", "", "", fork_branch)
        )

        print()
        if is_package:
            print(f"Forking OBS package {args.project}/{args.package} ...")
        else:
            print(f"Forking OBS project {args.project} ...")
        print(f" * OBS apiurl: {args.apiurl}")
        # we use a single API endpoint for forking both projects and packages (project requires setting package to "_project")
        status = obs_api.Package.cmd_fork(
            args.apiurl,
            args.project,
            args.package if is_package else "_project",
            scmsync=fork_scmsync,
            target_project=args.target_project,
            target_package=args.target_package if is_package else None,
        )
        # XXX: the current OBS API is not ideal; we don't get any info whether the new package exists already; 404 would be probably nicer
        target_project = status.data["targetproject"]
        if is_package:
            target_package = status.data["targetpackage"]
            print(f" * Fork created: {target_project}/{target_package}")
        else:
            print(f" * Fork created: {target_project}")
        print(f" * scmsync URL: {fork_scmsync}")

        # check if the scmsync branch exists in the forked repo
        fork_branch_data = gitea_api.Branch.get(gitea_conn, fork_owner, fork_repo, fork_branch).json()

        parent_commit = parent_branch_data["commit"]["id"]
        fork_commit = fork_branch_data["commit"]["id"]
        if parent_commit != fork_commit:
            print()
            print(f"{tty.colorize('ERROR', 'red,bold')}: The branch in the forked repo is out of sync with the parent")
            print(f" * Fork: {fork_owner}/{fork_repo}#{fork_branch}, commit: {fork_commit}")
            print(f" * Parent: {owner}/{repo}#{fork_branch}, commit: {parent_commit}")
            print(" * If this is not intentional, please clone the fork and fix the branch manually")
            sys.exit(1)
