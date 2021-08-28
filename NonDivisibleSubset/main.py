# Hackerank URL: https://www.hackerrank.com/challenges/non-divisible-subset/problem

import math


def get_module_dict(elems: list[int], k: int) -> iter(int, int):
    """Gets a list of integers and returns a list, where index is the division division_module and value is how many there are

        Parameters
        ----------
        elems : list[int]
            List of integers to divide
        k : int
            Integer used to divide by the list

        Returns
        -------
        list
            A list of [int]
    """
    module_list = [0] * k

    for v in elems:
        division_module = v % k
        module_list[division_module] += 1

    return module_list


def get_max_sublist_from_dict(modules: iter(int, int), k: int) -> int:
    """Given an iterable object, uses the key as division_module and value as how many there are
    and returns a maximum possible sub-list length of non-divisible numbers that can be created"""
    numbers = 0

    # If there are more than one element with module equals to 0. We cannot put them in the same list
    if modules[0] > 1:
        numbers += 1

    # Iterate on each element and test if the module [I] is greater than [K-I], if so we add [I] in other case [K-I]
    for i in range(1, math.ceil(k / 2)):
        if modules[i] > modules[k - i]:
            numbers += modules[i]
        else:
            numbers += modules[k - i]

    # If the list size is even and there are more than 2. We cannot put them in the same list
    is_even = k % 2 == 0
    if is_even:
        exists_a_module_equals_to_half = modules[int(k / 2)] > 0
        if exists_a_module_equals_to_half:
            numbers += 1

    return numbers


def non_divisible_subset(elems: list[int], k: int) -> int:
    # All numbers are divisible by 1, so it can only be a sublist of size 1
    if k == 1 or len(elems) == 1:
        return 1

    modules = get_module_dict(elems, k)

    numbers = get_max_sublist_from_dict(modules, k)

    return numbers
