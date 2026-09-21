"""Command line entry point for wordstats."""

import argparse
import sys

from .core import count_stats


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="wordstats",
        description="Count lines, words, and characters in a file.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="File to read; reads standard input when omitted.",
    )
    args = parser.parse_args(argv)

    if args.path:
        with open(args.path, "r", encoding="utf-8") as handle:
            text = handle.read()
    else:
        text = sys.stdin.read()

    stats = count_stats(text)
    print(
        f"{stats['lines']} lines, "
        f"{stats['words']} words, "
        f"{stats['characters']} characters"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
