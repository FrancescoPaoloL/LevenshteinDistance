import unittest
from levenshtein_distance import levenshtein_distance

class TestLevenshteinDistance(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(levenshtein_distance("", ""), 0)

    def test_same_string(self):
        self.assertEqual(levenshtein_distance("hello", "hello"), 0)

    def test_different_length(self):
        self.assertEqual(levenshtein_distance("hello", "hi"), 4)

    def test_easy_case(self):
        self.assertEqual(levenshtein_distance("mentor", "centers"), 3)

    def test_normal_case(self):
        self.assertEqual(levenshtein_distance("algorithm", "logarithm"), 3)

    def test_hard_case(self):
        self.assertEqual(levenshtein_distance("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"), 26)

    def test_sentence_case(self):
        self.assertEqual(levenshtein_distance("The quick brown fox jumps over the lazy dog.", "Pack my box with five dozen liquor jugs."), 33)


if __name__ == '__main__':
    unittest.main()