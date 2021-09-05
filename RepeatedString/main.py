"""
HackerRank link: https://www.hackerrank.com/challenges/repeated-string/problem
"""


def repeated_string(word: str, max_length: int, char: str) -> int:
    chars_in_one_word = word.count(char)

    if chars_in_one_word == 0:
        return 0

    word_length = len(word)

    max_completed_words = int(max_length / word_length)
    module_last_word = max_length % word_length

    counter = chars_in_one_word * max_completed_words

    counter += word.count(char, 0, module_last_word)

    return counter
