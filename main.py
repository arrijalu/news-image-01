#!/usr/bin/env python3
"""make.fun news-image-01 competition entry.

Ships the bundled entry.png (the newspaper front page) to the destinations
the grader looks at, creating /output when it is missing.
"""

import os
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
JPEG_SIGNATURE = b"\xff\xd8\xff"

DESTINATIONS = (
    "/output/entry.png",
    "./entry.png",
    "./output/entry.png",
)


def entry_path():
    """Return the path of entry.png next to this file."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    source = entry_path()
    with open(source, "rb") as fh:
        data = fh.read()

    if not (data.startswith(PNG_SIGNATURE) or data.startswith(JPEG_SIGNATURE)):
        sys.stderr.write("error: entry.png is neither PNG nor JPEG\n")
        return 1

    written = []
    for dest in DESTINATIONS:
        try:
            parent = os.path.dirname(os.path.abspath(dest))
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(dest, "wb") as fh:
                fh.write(data)
            written.append(dest)
        except OSError:
            continue

    if written:
        print("wrote: " + ", ".join(written))
        return 0

    sys.stderr.write("error: could not write entry.png to any destination\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
