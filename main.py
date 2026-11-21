#!/usr/bin/env python3
"""Copy the bundled front-page image to /output/entry.png and verify it."""
import hashlib
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"
EXPECTED_SHA256 = "6d01a76f95fcc5d6c20bd58c0e66257bcf51cb4a0c47100dd8d71f34a6c8d025"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    got = sha256_of(DST)
    if got != EXPECTED_SHA256:
        print("sha256 mismatch: got %s expected %s" % (got, EXPECTED_SHA256),
              file=sys.stderr)
        return 1
    print("entry.png copied to /output/entry.png sha256 %s" % got)
    return 0


if __name__ == "__main__":
    sys.exit(main())
