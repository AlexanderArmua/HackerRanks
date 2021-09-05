from unittest import TestCase
from main import repeated_string


class Test(TestCase):
    def test_larrys_array(self):
        self.assertEqual(repeated_string("abcac", 10, "a"), 4)

        self.assertEqual(repeated_string("aba", 10, "a"), 7)

        self.assertEqual(repeated_string("a", 1000000000000, "a"), 1000000000000)

        self.assertEqual(repeated_string("qwe", 10, "a"), 0)
