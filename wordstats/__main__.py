"""Command line entry point for wordstats."""

import argparse
import sys

from .core import count_stats, top_words


def _print_stats(label, stats, text, top_n):
    line = (
        f"{stats['lines']} lines, "
        f"{stats['words']} words, "
        f"{stats['characters']} characters"
    )
    print(f"{label}: {line}" if label else line)

    if top_n and top_n > 0:
        for word, count in top_words(text, top_n):
            print(f"  {word}: {count}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="wordstats",
        description="Count lines, words, and characters in one or more files.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files to read; reads standard input when omitted.",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=0,
        metavar="N",
        help="Show the N most common words (default: disabled).",
    )
    args = parser.parse_args(argv)

    if not args.paths:
        text = sys.stdin.read()
        _print_stats(None, count_stats(text), text, args.top)
        return 0

    totals = {"lines": 0, "words": 0, "characters": 0}
    for path in args.paths:
        with open(path, "r", encoding="utf-8") as handle:
            text = handle.read()
        stats = count_stats(text)
        totals["lines"] += stats["lines"]
        totals["words"] += stats["words"]
        totals["characters"] += stats["characters"]
        _print_stats(path, stats, text, args.top)

    if len(args.paths) > 1:
        print(
            "total: "
            f"{totals['lines']} lines, "
            f"{totals['words']} words, "
            f"{totals['characters']} characters"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
