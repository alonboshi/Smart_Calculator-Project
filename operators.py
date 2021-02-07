from excptions import *


class Operators:

    def __init__(self):
        # [operator][0] = function , [operator][1] = power  ,
        # [operator][2] = place
        # dictionary of the operators and its power
        # most little power is the stronger ....
        # place means where the operator is located according
        # to the operand
        self.signs = {
            # key: (delegate,power,place)
            '+': (plus, 1, "MIDDLE"),
            '-': (sub, 1, "MIDDLE"),
            '*': (mul, 2, "MIDDLE"),
            '/': (div, 2, "MIDDLE"),
            '^': (pow, 3, "MIDDLE"),
            '%': (modulu, 4, "MIDDLE"),
            '@': (avg, 5, "MIDDLE"),
            '$': (max, 5, "MIDDLE"),
            '&': (min, 5, "MIDDLE"),
            '!': (factorial, 6, "RIGHT"),
            '~': (tilde, 7, "LEFT")
            # """
            # ,'#': (example, 8, "LEFT")
            # """
        }

        # dictionary of the opening bracket and its power
        # most little power is the stronger ....
        self.open_brackets = {
            '(': 3
            # ,'[': 2
            # for example you can add an opening bracket and its power
            # and the suitable closing bracket with the same power
        }

        # dictionary of the closing bracket and its power
        # most little power is the stronger ....
        self.close_brackets = {
            ')': 3
            # ,']': 2
        }

        # combining those two dictionaries into one of all the opening
        # and closing brackets
        self.brackets = self.open_brackets.copy()
        self.brackets.update(self.close_brackets)


"""
def example(lst, i):
    del lst[i]
    lst[i] *= 2
"""


# +
def plus(lst, i):
    try:
        res = lst[i - 1] + lst[i + 1]
    except OverflowError:
        raise OverFlow("Error ! : Adding result is too big")
    del lst[i + 1]
    del lst[i]
    lst[i - 1] = res


# -
def sub(lst, i):
    try:
        res = lst[i - 1] - lst[i + 1]
    except OverflowError:
        raise OverFlow("Error ! : Sub result is too big")
    del lst[i + 1]
    del lst[i]
    lst[i - 1] = res


# *
def mul(lst, i):
    try:
        res = lst[i - 1] * lst[i + 1]
    except OverflowError:
        raise OverFlow("Error ! : Multiply result is too big")
    del lst[i + 1]
    del lst[i]
    lst[i - 1] = res


# /
def div(lst, i):
    if lst[i + 1] == 0:
        raise Operators_ex("ERROR ! : It is illegal to divide by 0")
    try:
        res = lst[i - 1] / float(lst[i + 1])
    except OverflowError:
        raise OverFlow("Error ! : Divide result is too big")
    del lst[i + 1]
    del lst[i]
    lst[i - 1] = res


# ^
def pow(lst, i):
    try:
        res = lst[i - 1] ** lst[i + 1]
    except OverflowError:
        raise OverFlow("Error ! : Power result is too big")
    del lst[i + 1]
    del lst[i]
    lst[i - 1] = res


# ~
def tilde(lst, i):
    if i is len(lst) - 1:
        raise Operators_ex("Error ! : Missing a number after the operand '~'")
    try:
        res = lst[i + 1] * (-1)
    except OverflowError:
        raise OverFlow("Error ! : Multiply result is too big")
    del lst[i]
    lst[i] = res


# %
def modulu(lst, i):
    if lst[i + 1] == 0:
        raise Operators_ex("ERROR ! : It is illegal to modulu by 0")
    res = lst[i - 1] % lst[i + 1]
    del lst[i + 1]
    del lst[i]
    lst[i - 1] = res


# !
def factorial(lst, i):
    if i is 0:
        raise Operators_ex("Error ! : Missing a number before the operand '!'")

    # there is no answer for factorial to a negative number
    if lst[i - 1] < 0:
        raise Factorial_minus("Error ! : No factorial for negative number")

    # there is no answer for factorial to a float number
    if type(lst[i - 1]) is int or lst[i - 1].is_integer():
        a = int(lst[i - 1])
    else:
        raise Factorial_float("Error ! : No factorial for float number")

    factor = 1
    num = int(lst[i - 1])
    for num in range(1, num + 1):
        try:
            factor *= num
        except OverflowError:
            raise OverFlow("Error ! : Factorial result is too big")
    del lst[i - 1]
    lst[i - 1] = factor


# @
def avg(lst, i):
    try:
        res = (lst[i - 1] + lst[i + 1]) / 2
    except OverflowError:
        raise OverFlow("Error ! : Average result is too big")
    del lst[i + 1]
    del lst[i]
    lst[i - 1] = res


# $
def max(lst, i):
    res = lst[i - 1] if (lst[i - 1] > lst[i + 1]) else lst[i + 1]
    del lst[i + 1]
    del lst[i]
    lst[i - 1] = res


# &
def min(lst, i):
    res = lst[i - 1] if (lst[i - 1] < lst[i + 1]) else lst[i + 1]
    del lst[i + 1]
    del lst[i]
    lst[i - 1] = res
