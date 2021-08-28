from unittest import TestCase
from main import time_in_words


class Test(TestCase):
    def test_time_in_words_o_clock(self):
        self.assertEqual(time_in_words(1, 0), "one o' clock")

        self.assertEqual(time_in_words(5, 0), "five o' clock")

    def test_time_in_words_past(self):
        self.assertEqual(time_in_words(5, 1), "one minute past five")

        self.assertEqual(time_in_words(5, 10), "ten minutes past five")

        self.assertEqual(time_in_words(5, 15), "quarter past five")

        self.assertEqual(time_in_words(5, 28), "twenty eight minutes past five")

        self.assertEqual(time_in_words(5, 30), "half past five")

    def test_time_in_words_to(self):
        self.assertEqual(time_in_words(6, 40), "twenty minutes to seven")

        self.assertEqual(time_in_words(6, 45), "quarter to seven")

        self.assertEqual(time_in_words(6, 47), "thirteen minutes to seven")
