import unittest
from my_awesome_lib.text_processing import reverse_text, count_vowels

class TestTextProcessing(unittest.TestCase):
    def test_reverse_text(self):
        self.assertEqual(reverse_text("hello"), "olleh")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)

if __name__ == '__main__':
    unittest.main()
