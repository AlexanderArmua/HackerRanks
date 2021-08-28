# HackerRank URL: https://www.hackerrank.com/challenges/the-time-in-words/problem


def build_numbers(numbers: list[int], pre: str, init: int, end: int) -> list[str]:
    new_numbers = []

    for i in range(init, end + 1):
        new_numbers.append(f"{pre} {numbers[i]}".rstrip())

    return new_numbers


def get_numbers() -> list[str]:
    numbers = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
               'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    for i in ['twenty', 'thirty', 'forty', 'fifty']:
        numbers += build_numbers(numbers, i, 0, 9)

    return numbers


def get_time_past(numbers: list[str], h: int, m: int) -> str:
    hour = numbers[h]
    minutes = numbers[m]

    if m == 0:
        return f"{hour} o' clock"

    text = ""

    if m == 1:
        text += f"{minutes} minute "
    elif 1 < m < 30 and m != 15:
        text += f"{minutes} minutes "
    elif m == 15:
        text += f"{minutes} "
    elif m == 30:
        text += "half "

    text += f"past {hour}"

    return text


def get_time_to(numbers: list[str], h: int, m: int) -> str:
    minutes_to_int = 60 - m
    minutes_to = numbers[minutes_to_int]

    hours_to_int = 1
    if h < 12:
        hours_to_int = h + 1

    hour_next = numbers[hours_to_int]

    text = f"{minutes_to} "
    if minutes_to_int == 1:
        text += "minute "
    elif 1 < minutes_to_int < 15 or 15 < minutes_to_int:
        text += "minutes "

    text += f"to {hour_next}"

    return text


def time_in_words(h: int, m: int) -> str:
    numbers = get_numbers()

    if m <= 30:
        return get_time_past(numbers, h, m)

    return get_time_to(numbers, h, m)
