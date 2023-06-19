from . import xmlmodel


class IssueTracker(xmlmodel.Model):
    TAG_NAME = "issue-tracker"

    name = xmlmodel.TextNodeField(
        "name",
    )

    label = xmlmodel.TextNodeField(
        "label",
    )

    kind = xmlmodel.TextNodeField(
        "kind",
    )

    description = xmlmodel.TextNodeField(
        "description",
    )

    enable_fetch = xmlmodel.TextNodeField(
        "enable-fetch",
        optional=True,
    )

    publish_issues = xmlmodel.TextNodeField(
        "publish-issues",
        optional=True,
    )

    issues_updated = xmlmodel.TextNodeField(
        "issues-updated",
        optional=True,
    )

    user = xmlmodel.TextNodeField(
        "user",
        optional=True,
    )

    password = xmlmodel.TextNodeField(
        "password",
        optional=True,
    )

    url = xmlmodel.TextNodeField(
        "url",
    )

    show_url = xmlmodel.TextNodeField(
        "show-url",
    )

    regex = xmlmodel.TextNodeField(
        "regex",
    )
