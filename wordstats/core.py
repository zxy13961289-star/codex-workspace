"""Text statistics helpers."""

import re
from collections import Counter

_WORD_RE = re.compile(r"\b\w+\b")


def count_stats(text):
    """Return line, word, and character counts for ``text``."""
    if not text:
        return {"lines": 0, "words": 0, "characters": 0}

    lines = text.count("\n")
    if not text.endswith("\n"):
        lines += 1

    return {
        "lines": lines,
        "words": len(text.split()),
        "characters": len(text),
    }


def top_words(text, n=5):
    """Return the ``n`` most common words as ``(word, count)`` tuples.

    Matching is case-insensitive and ignores punctuation.
    """
    words = _WORD_RE.findall(text.lower())
    return Counter(words).most_common(n)
