"""Text statistics helpers."""


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
