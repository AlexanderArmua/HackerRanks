from unittest import TestCase
from main import non_divisible_subset


class TestNonDivisibleSubset(TestCase):
    def test_non_divisible_subset_works_with_short_lists(self):
        elements = [1, 7, 2, 4]
        k = 3

        self.assertAlmostEqual(non_divisible_subset(elements, k), 3)

    def test_non_divisible_subset_works_with_large_lists(self):
        elements = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
        k = 7

        self.assertAlmostEqual(non_divisible_subset(elements, k), 11)

    def test_non_divisible_subset_k_equals_to_1_must_be_1(self):
        elements = [1, 2, 3, 4, 5]
        k = 1

        self.assertAlmostEqual(non_divisible_subset(elements, k), 1)

    def test_non_divisible_subset_list_size_0_must_be_0(self):
        elements = []
        k = 9

        self.assertAlmostEqual(non_divisible_subset(elements, k), 0)

    def test_non_divisible_subset_list_size_1_must_be_1(self):
        elements = [99]
        k = 5

        self.assertAlmostEqual(non_divisible_subset(elements, k), 1)

