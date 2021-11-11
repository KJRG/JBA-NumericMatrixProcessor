import math


def format_number(number):
    result = 0.0
    if number > 0.0:
        result = round_down(number, 2)
    elif number < 0.0:
        result = round_up(number + 0, 2)
    return str(round(result, 2))


def round_up(number, digits):
    factor = 10 ** digits
    return math.ceil(number * factor) / factor


def round_down(number, digits):
    factor = 10 ** digits
    return math.floor(number * factor) / factor
