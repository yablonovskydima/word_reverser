import unittest
from reverse_words_package.reverse_words import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(reverse_words("abcd"), "dcba")

    def test_multiple_words(self):
        self.assertEqual(reverse_words("abcd efgh"), "dcba hgfe")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_words_with_numbers_and_symbols(self):
        self.assertEqual(reverse_words("a1bcd efg!h"), "d1cba hgf!e")

    def test_only_numbers(self):
        self.assertEqual(reverse_words("12345"), "12345")

    def test_mixed_words(self):
        self.assertEqual(reverse_words("a1b cd2"), "b1a dc2")

if __name__ == "__main__":
    unittest.main()
