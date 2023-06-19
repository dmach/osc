BLOCK_MODES: tuple[str] = (
    "all",
    "local",
    "never",
)

BUILD_ARCH: tuple[str] = (
    "noarch",
    "aarch64",
    "aarch64_ilp32",
    "armv4l",
    "armv5l",
    "armv6l",
    "armv7l",
    "armv5el",
    "armv6el",
    "armv7el",
    "armv7hl",
    "armv8el",
    "hppa",
    "m68k",
    "i386",
    "i486",
    "i586",
    "i686",
    "athlon",
    "ia64",
    "k1om",
    "mips",
    "mipsel",
    "mips32",
    "mips64",
    "mips64el",
    "ppc",
    "ppc64",
    "ppc64p7",
    "ppc64le",
    "riscv64",
    "s390",
    "s390x",
    "sh4",
    "sparc",
    "sparc64",
    "sparc64v",
    "sparcv8",
    "sparcv9",
    "sparcv9v",
    "x86_64",
    "local",
)

BUILD_SANDBOX: tuple[str] = (
    "chroot",
    "lxc",
    "kvm",
    "xen",
    "secure",
)

GLOBAL_ROLE: tuple[str] = (
    "Admin",
    "User",
)

JOBSTATUS_RESULT: tuple[str] = (
    "succeeded",
    "failed",
    "unchanged",
)

LINKEDBUILD_MODES: tuple[str] = (
    "off",
    "localdep",
    "alldirect",
    "all",
)

LOCAL_ROLE: tuple[str] = (
    "maintainer",
    "bugowner",
    "reviewer",
    "downloader",
    "reader",
)

OBS_RATINGS: tuple[str] = (
    "low",
    "moderate",
    "important",
    "critical",
)

PACKAGE_CODE: tuple[str] = (
    "unresolvable",
    "succeeded",
    "failed",
    "broken",
    "disabled",
    "excluded",
    "blocked",
    "locked",
    "unknown",
    "scheduled",
    "building",
    "finished",
)

REBUILD_MODES: tuple[str] = (
    "transitive",
    "direct",
    "local",
)

RELEASE_TRIGGERS: tuple[str] = (
    "manual",
    "maintenance",
    "obsgendiff",
)

REPOSITORY_CODE: tuple[str] = (
    "unknown",
    "broken",
    "scheduling",
    "blocked",
    "building",
    "finished",
    "publishing",
    "published",
    "unpublished",
)

SERVICE_MODES: tuple[str] = (
    "trylocal",
    "localonly",
    "serveronly",
    "buildtime",
    "manual",
    "disabled",
)

SUPPORTSTATUS_CHOICES: tuple[str] = (
    "l3",
    "l2",
    "l1",
    "acc",
    "unsupported",
)

TOKEN_KIND: tuple[str] = (
    "rss",
    "rebuild",
    "release",
    "runservice",
)

