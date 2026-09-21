import unittest

from wordstats.core import count_stats, top_words


class CountStatsTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(
            count_stats(""),
            {"lines": 0, "words": 0, "characters": 0},
        )

    def test_single_line(self):
        self.assertEqual(
            count_stats("hello world"),
            {"lines": 1, "words": 2, "characters": 11},
        )

    def test_multiple_lines(self):
        self.assertEqual(
            count_stats("a\nbb\n"),
            {"lines": 2, "words": 2, "characters": 5},
        )

    def test_trailing_newline(self):
        self.assertEqual(
            count_stats("a\n"),
            {"lines": 1, "words": 1, "characters": 2},
        )


class TopWordsTests(unittest.TestCase):
    def test_most_common(self):
        self.assertEqual(
            top_words("apple banana apple cherry banana apple", 2),
            [("apple", 3), ("banana", 2)],
        )

    def test_case_insensitive(self):
        self.assertEqual(
            top_words("Hello hello HELLO", 1),
            [("hello", 3)],
        )

    def test_ignores_punctuation(self):
        self.assertEqual(
            top_words("hello, world! hello.", 1),
            [("hello", 2)],
        )


if __name__ == "__main__":
    unittest.main()
