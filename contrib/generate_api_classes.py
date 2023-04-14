#!/usr/bin/python3


import os
import sys


DIR = os.path.abspath(os.path.dirname(__file__))
OBS_DIR = os.path.join(DIR, "open-build-service")


if not os.path.exists(OBS_DIR):
    print(f"ERROR: The Open Build Service checkout doesn't exist: {OBS_DIR}", file=sys.stderr)
    print(f"Run the following commands first:", file=sys.stderr)
    print(f"  cd {DIR}", file=sys.stderr)
    print(f"  git clone https://github.com/openSUSE/open-build-service.git", file=sys.stderr)
    sys.exit(1)


def main():
    pass


if __name__ == "__main__":
    main()
