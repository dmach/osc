from typing import Tuple


BLOCK_MODES: Tuple[str] = (
    "all",
    "local",
    "never",
)

BUILD_ARCH: Tuple[str] = (
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

LINKEDBUILD_MODES: Tuple[str] = (
    "off",
    "localdep",
    "alldirect",
    "all",
)

LOCAL_ROLE: Tuple[str] = (
    "maintainer",
    "bugowner",
    "reviewer",
    "downloader",
    "reader",
)

OBS_RATINGS: Tuple[str] = (
    "low",
    "moderate",
    "important",
    "critical",
)

REBUILD_MODES: Tuple[str] = (
    "transitive",
    "direct",
    "local",
)

RELEASE_TRIGGERS: Tuple[str] = (
    "manual",
    "maintenance",
    "obsgendiff",
)

REQUEST_STATES: Tuple[str] = (
    "review",
    "new",
    "accepted",
    "declined",
    "revoked",
    "superseded",
    "deleted",
)
