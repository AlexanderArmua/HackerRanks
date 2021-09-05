from unittest import TestCase
from main import equalize_array


class Test(TestCase):
    def test_equalize_array(self):

        self.assertEqual(equalize_array([1, 2, 2, 3]), 2)

        self.assertEqual(equalize_array([3, 3, 2, 1, 3]), 2)
