from operators import Operators
from excptions import *


class Valid:
    """
    A class that checks the validation of the list.
    If everything is ok, it won't return or change nothing.
    And if there is a problem, it will raise an exception with specific
    message.
    """

    def __init__(self, lst):
        self.op = Operators()
        self.lst = lst
        self.correct()
        self.no_mistakes()
        self.brackets()
        self.operators()

    def correct(self):
        # makes sure there are no mistakes

        # -----------------------empty input----------------------------
        if len(self.lst) is 0:
            raise Validation("Error Input : Empty Input")

        # -----------------------too long input----------------------------
        if len(self.lst) > 100000:
            raise Validation("Error Input : Too Long Input")

        # --------------------------------------------------------------
        # ------------------brackets adder validation-------------------

        # ---------Non equal number of open and close brackets----------
        if len(self.op.open_brackets) is not len(self.op.close_brackets):
            raise Validation("Error in Code : Non equal number of open and"
                             " close brackets")

        # -------------------same brackets to itself or a sign----------
        for key in self.op.open_brackets:
            if key in self.op.close_brackets:
                raise Validation("Error in code : Open bracket equal to "
                                 "close bracket")
            if key in self.op.signs:
                raise Validation("Error in code : Open bracket equal to sign")

        for key in self.op.close_brackets:
            if key in self.op.signs:
                raise Validation("Error in code : close bracket equal to sign")

        # -------------------same power to opening brackets-------------
        count = 0
        for key in self.op.open_brackets:
            for another_key in self.op.open_brackets:
                if self.op.open_brackets[key] is \
                        self.op.open_brackets[another_key]:
                    count += 1
        if count is not len(self.op.open_brackets):
            raise Validation("Error in Code : All types of opening brackets"
                             " need  to have a different power")

        # -------------------same power to closing brackets-------------
        count = 0
        for key in self.op.close_brackets:
            for another_key in self.op.close_brackets:
                if self.op.close_brackets[key] is \
                        self.op.close_brackets[another_key]:
                    count += 1
        if count is not len(self.op.close_brackets):
            raise Validation("Error in Code : All types of closing brackets"
                             " need  to have a different power")

        # --------------------------------------------------------------

    def no_mistakes(self):

        # ---------checks every cell if its an valid character----------
        for cell in range(len(self.lst)):
            if self.lst[cell] in self.op.signs:
                continue
            if type(self.lst[cell]) is float or type(self.lst[cell]) is int:
                continue
            if self.lst[cell] in self.op.brackets:
                if cell < len(self.lst) - 1 and \
                        self.lst[cell] in self.op.open_brackets and \
                        self.lst[cell + 1] in self.op.close_brackets:
                    # empty brackets
                    raise Validation("Error Input : Brackets are empty")
                elif cell < len(self.lst) - 1 and \
                        self.lst[cell] in self.op.close_brackets and \
                        self.lst[cell + 1] in self.op.open_brackets:
                    # no operand between the brackets
                    raise Validation("Error Input : Missing an operand " +
                                     "between the brackets ")
                continue
            raise Validation("Error Input : InValid character  '" +
                             str(self.lst[cell]) + "'")

    def brackets(self):
        stack = []
        # a stack that push only opening brackets.
        # if there is a closing bracket and the stack is empty, opening
        # brackets is missing and if the stack is not empty at the end,
        # opening bracket is missing
        for cell in range(len(self.lst)):
            if self.lst[cell] in self.op.brackets:
                if self.lst[cell] in self.op.open_brackets:
                    stack.append(self.lst[cell])
                elif len(stack) is 0:
                    raise Validation("Error Input : Missing opening bracket"
                                     " for : '" + str(self.lst[cell]) + "'")
                else:
                    sug = stack.pop()
                    if self.op.close_brackets[self.lst[cell]] is \
                            self.op.open_brackets[sug]:
                        pass
                    else:
                        # not equal power as the opening bracket
                        raise Validation("Error Input : Missing closing "
                                         "bracket for : '" + str(sug) + "'")
        if len(stack) is not 0:
            raise Validation("Error Input : Missing closing bracket for : '" +
                             stack.pop() + "'")

        # -----------------------UnNecessary Brackets ((5+5))-----------
        # stack that push any cell except closing bracket
        # when there is a closing bracket, if the last cell in the stack
        # is opening bracket, there is nothing between them.
        cell = 0
        stack = []
        while cell < len(self.lst):
            # if the cell isn't a closing bracket, push it into the stack
            if self.lst[cell] not in self.op.close_brackets:
                stack.append(self.lst[cell])
            else:  # the cell is a closing bracket
                bracket = self.op.close_brackets[self.lst[cell]]
                check = stack.pop()
                if check in self.op.open_brackets:
                    raise Validation("Error Input : unNecessary brackets")
                while check not in self.op.open_brackets:
                    check = stack.pop()
                # i=0
            cell += 1

    def operators(self):
        # Validation for every operand and bracket in the list

        # --------------------Validation for first index----------------
        if type(self.lst[0]) is float or type(self.lst[0]) is int or \
                self.lst[0] in self.op.open_brackets or \
                self.lst[0] in self.op.signs and \
                (self.lst[0] is '-' or
                 self.op.signs[self.lst[0]][2] is "LEFT"):
            pass
        else:
            raise Validation("Error Input : InValid first index")
        # --------------------------------------------------------------
        # --------------------Validation for last index-----------------
        last = len(self.lst) - 1
        if type(self.lst[last]) is float or type(self.lst[last]) is int or \
                self.lst[last] in self.op.close_brackets or \
                (self.lst[last] in self.op.signs and
                 self.op.signs[self.lst[last]][2] is "RIGHT"):
            pass
        else:
            raise Validation("Error Input : InValid last index")
        # ~!
        if len(self.lst) == 2 and (type(self.lst[0]) is not float and
                                   type(self.lst[1]) is not float):
            raise Validation("Error input : No operand found")
        # --------------------------------------------------------------
        # ----------------Validation for missing an operator -----------

        for i in range(1, len(self.lst) - 1):
            # ------------------------------------------------
            previous_ = self.lst[i - 1]  # previous cell
            current_ = self.lst[i]  # current cell
            next_ = self.lst[i + 1]  # next cell
            # ------------------------------------------------
            #  current cell is a number
            if type(current_) is float or type(current_) is int:
                continue
            # ----------------------------------------------------------
            #  current cell is an opening bracket
            elif current_ in self.op.open_brackets:
                #  (---next---
                if next_ in self.op.open_brackets or \
                        type(next_) is float or \
                        type(next_) is int:
                    pass
                elif next_ is '-' or \
                        (next_ in self.op.signs and
                         self.op.signs[next_][2] is "LEFT"):
                    pass
                else:
                    raise Validation("Error Input : Invalid character '"
                                     + str(next_) +
                                     "' after bracket '" + str(current_))

                # ---previous---(
                if previous_ in self.op.open_brackets:
                    pass
                elif previous_ in self.op.signs and \
                        self.op.signs[previous_][2] is not "RIGHT":
                    pass
                else:
                    raise Validation("Error Input : Invalid character '"
                                     + str(previous_) +
                                     "' before bracket '" + str(current_) +
                                     "'")
            # ----------------------------------------------------------
            #  current cell is a closing bracket
            elif current_ in self.op.close_brackets:
                # )---next---
                if next_ in self.op.close_brackets:
                    pass
                elif next_ in self.op.signs and \
                        self.op.signs[next_][2] is not "LEFT":
                    pass
                else:
                    raise Validation("Error Input : Invalid character '"
                                     + str(next_) +
                                     "' after bracket '" + str(current_) +
                                     "'")

                # ---previous---)
                if previous_ in self.op.close_brackets \
                        or type(previous_) is float \
                        or type(previous_) is int:
                    pass
                elif previous_ in self.op.signs and \
                        self.op.signs[previous_][2] is "RIGHT":
                    pass
                else:
                    raise Validation("Error Input : Invalid character '"
                                     + str(previous_) +
                                     "' before bracket '" + str(current_) +
                                     "'")
            # ----------------------------------------------------------
            # operators
            elif current_ in self.op.signs:
                place = self.op.signs[current_][2]
                # ------------------------------------------------------
                # !
                if place is "RIGHT":
                    # !next
                    if next_ in self.op.signs and \
                            (self.op.signs[next_][2] is "MIDDLE"
                             or (self.op.signs[next_][2] is "RIGHT"
                                 and self.op.signs[current_][1] >=
                                 self.op.signs[next_][1])):
                        pass
                    elif next_ in self.op.close_brackets:
                        pass
                    else:
                        raise Validation("Error Input : Invalid character "
                                         "after the operand : " +
                                         str(current_))

                    # previous!
                    if previous_ in self.op.close_brackets \
                            or type(previous_) is float \
                            or type(previous_) is int:
                        pass
                    elif previous_ in self.op.signs and \
                            (self.op.signs[previous_][2] is "RIGHT" and
                             self.op.signs[current_][1] <=
                             self.op.signs[previous_][1]):
                        pass
                    else:
                        raise Validation("Error Input : Invalid character "
                                         "before the operand : " +
                                         str(current_))
                # ------------------------------------------------------
                # ~
                elif place is "LEFT":
                    # ~next
                    if next_ in self.op.open_brackets \
                            or type(next_) is float \
                            or type(next_) is int:
                        pass
                    elif next_ in self.op.signs and \
                            (next_ is '-' or
                             (self.op.signs[next_][2] is "LEFT" and
                              self.op.signs[current_][1] <=
                              self.op.signs[next_][1])):
                        pass
                    else:
                        raise Validation("Error Input : Invalid character "
                                         "after the operand : '" +
                                         str(current_) + "'")

                    # previous~
                    if previous_ in self.op.open_brackets:
                        pass
                    elif previous_ in self.op.signs and \
                            (previous_ is '-' or
                             (self.op.signs[previous_][2] is "LEFT" and
                              self.op.signs[current_][1] <=
                              self.op.signs[previous_][1])):
                        pass
                    elif previous_ in self.op.signs and \
                            self.op.signs[previous_][2] is not "RIGHT" \
                            and (self.op.signs[current_][1] >
                                 self.op.signs[previous_][1]):
                        pass
                    else:
                        raise Validation("Error Input : Invalid character "
                                         "before the operand : '" +
                                         str(current_) + "'")
                # ------------------------------------------------------
                # *
                elif place is "MIDDLE":
                    # *next
                    if next_ in self.op.open_brackets or \
                            type(next_) is int \
                            or type(next_) is float:
                        pass
                    elif next_ in self.op.signs and \
                            (next_ is '-' or
                             (self.op.signs[next_][2] is "LEFT" and
                              self.op.signs[current_][1] <
                              self.op.signs[next_][1])):
                        pass
                    elif next_ in self.op.close_brackets:
                        raise Validation("Error Input : Missing number between"
                                         " an operator '" + str(current_) +
                                         "' and bracket '" +
                                         str(next_) + "'")
                    else:
                        raise Validation("Error Input :Operators in sequence '"
                                         + str(current_) + "' '" + str(next_) +
                                         "'")

                    # previous*
                    if previous_ in self.op.close_brackets or \
                            previous_ == '-' or \
                            type(previous_) is int \
                            or type(previous_) is float:
                        pass

                    elif previous_ in self.op.signs and \
                            (self.op.signs[previous_][2] is "RIGHT" and
                             self.op.signs[current_][1] <=
                             self.op.signs[previous_][1]):
                        pass

                    elif current_ is '-' and previous_ in \
                            self.op.signs and \
                            self.op.signs[current_][1] <= \
                            self.op.signs[previous_][1]:
                        pass
                    elif current_ is '-' and \
                            previous_ in self.op.brackets:
                        pass
                    elif previous_ in self.op.open_brackets:
                        raise Validation("Error Input : Missing number between"
                                         "an operator '" + str(current_) +
                                         "' and bracket '" +
                                         str(previous_) +
                                         "'")
                    else:
                        raise Validation("Error Input :Operators in sequence '"
                                         + str(previous_) + "' '"
                                         + str(current_) + "'")
                # ------------------------------------------------------
