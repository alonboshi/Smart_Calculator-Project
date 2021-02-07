from minusController import minusHandler
from validation import Valid
from excptions import *


def isDigit(var):
    """
    a func that checks if the var is a digit
    :param var: a char
    :return: True if the char in the set,
             and False if not
    """
    DIGITS = set('0123456789')
    return var in DIGITS


class Into_list:
    """
    class that converts a string to a list divided by numbers
    and operators
    """

    def __init__(self, str):
        self.str = str  # the user's string
        self.list = []  # the list
        self.stringToList()  # converts the string into the list
        Valid(self.list)  # does nothing if the list is valid
        #                   if not valid, raises an exception
        minusHandler(self.list)  # handles the sequences of minus

    def stringToList(self):
        """
        the main function that converts the string into a list and
        returns the list
        :return: list after conversion
        """
        # delete all the white spaces in the string
        self.str = self.str.replace(' ', '').replace('\t', ''). \
            replace('\n', '')

        character = 0
        while character < len(self.str):
            sequence = 0  # how
            dots = 0    # dots in the current number
            # if self.str[character] is a digit
            if isDigit(self.str[character]):
                # while the string isn't over and self.str[character]
                # is a digit or a dot
                while character < len(self.str) and \
                        (isDigit(self.str[character]) or self.str[character]
                         is '.'):
                    # if self.str[character] is dot and there are more
                    # than one dot, raises an exception
                    if self.str[character] is '.':
                        dots += 1
                        if dots > 1:
                            raise Validation("Error! : Too many dots")
                    sequence += 1
                    character += 1
                # adds to the list a float of the sequence of characters
                if self.str[character-1] == '.':
                    raise Validation("Error ! : Number don't end with a dot")
                self.list.append(float(self.str[character -
                                                sequence:character]))
            else:
                # adds to the the list a character which isn't number
                self.list.append(self.str[character])
                character += 1
