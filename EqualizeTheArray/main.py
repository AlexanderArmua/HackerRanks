"""
HackerRank link: https://www.hackerrank.com/challenges/equality-in-a-array/problem
"""

def build_dict(array: iter(int, int)) -> dict[int, int]:
    """Given an array returns a dictionary where key is the array value and value is the number repetitions"""
    dic = {}

    for e in array:
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 1

    return dic


def search_max_repeated_value(dic: dict[int, int]) -> (int, int):
    """Given a dictionary[int, int] returns the maximum value with their key"""
    max_key = list(dic.keys())[0]
    max_value = dic[max_key]

    for key in dic:
        if dic[key] > max_value:
            max_key = key
            max_value = dic[key]

    return max_key, max_value


def equalize_array(array: list[int]) -> int:
    dic = build_dict(array)

    max_key, max_value = search_max_repeated_value(dic)

    keys_to_delete = len(array) - max_value

    return keys_to_delete
