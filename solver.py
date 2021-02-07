from operators import *
from minusController import minusSign
from excptions import OverFlow


def solve(lst):
    """
    !solving function!
    recursive function which gets the exercise in a list and finally
    returns the solved exercise
    """
    # puts into problem False if none of the list's cells are complex
    # or infinity. Elsewhere it puts a string of one of them
    problem = infinity_complex(lst)
    if problem is not False:
        raise OverFlow(problem + " number... try again")

    # if the list has only one cell which is the solution
    if len(lst) == 1:  # the solution
        return lst

    # sends to a function that handles the deeper solution in the
    # brackets and updates the list
    bracketsHandler(lst)

    # if after handling the brackets, the list has only one cell which
    # is the solution
    if len(lst) == 1:  # the solution
        return lst

    # returns the index of the strongest operator in the exercise
    max_op = max_operator(lst)

    # handles the sign-minus in the next index before doing
    # the calculating
    minusSign(lst, max_op)

    # if after handling the minuses, the list has only one cell which
    # is the solution.
    if len(lst) == 1:
        return lst

    # after the minussign function, there might be a new max operator.
    # returns the index of the strongest operator in the exercise.
    max_op = max_operator(lst)

    # max_op will be -1 if there is no operators in the exercise
    # so we won't have to calculate something which is not exist.
    if max_op != -1:
        # sends the list and the index of the max operand to a
        # dictionary of the signs and then, in the value, first cell,
        # a delegate to the right calculating function which calculates
        # and updates the list with the solution
        Operators().signs[lst[max_op]][0](lst, max_op)

    # recursion
    return solve(lst)


def infinity_complex(lst):
    # function that goes through all the list and checks every cell if
    # it is an infinity or complex number.
    # if true, it returns the name of the problem, otherwise false
    for i in range(len(lst)):
        if lst[i] == float('inf') or lst[i] == float('-inf'):
            return "infinity"
        if type(lst[i]) is complex:
            return "complex"
    return False


def bracketsHandler(lst):
    # func that founds the deepest starting bracket and then its closing
    # bracket and calls the solver with the content between them
    secondPair = -1  # ending bracket

    # finding the deepest starting bracket by going back from the end.
    # first_pair - index of the opening bracket.
    # bracket - power of the bracket
    first_pair, bracket = max_brackets(lst)

    # finding the suitable ending bracket by going forward
    # from the starting bracket till we find the )
    if first_pair == -1:
        return
    second = first_pair
    while second < len(lst):

        # if the current cell is a closing bracket
        if lst[second] in Operators().close_brackets:

            # if the power of the closing bracket is equal to the
            # opening bracket's power
            if Operators().close_brackets[lst[second]] == bracket:
                secondPair = second
                break
        second += 1

    # if we find some brackets
    if secondPair != -1:
        # return the solution of the exercise between the brackets
        # instead the whole field
        lst[first_pair] = solve(lst[first_pair + 1:secondPair])[0]
        del lst[first_pair + 1:secondPair + 1]
        solve(lst)


def max_brackets(lst):
    # finding the deepest starting bracket by going back from the end.
    # returns:
    # first_pair - index of the opening bracket.
    # bracket - power of the bracket

    power = 1000  # power of the bracket. most little is the most strong.
    index_of_max_bracket = -1
    # going from the end to the start
    for cell in reversed(range(len(lst))):
        # if cell is opening bracket
        if lst[cell] in Operators().open_brackets:
            temp = lst[cell]
            temp_power = Operators().open_brackets[temp]  # power
            if temp_power < power:
                power = temp_power
                index_of_max_bracket = cell
    return index_of_max_bracket, power


def max_operator(lst):
    """
    function that finds the max operator in the list.
    if the operand place is LEFT, and there is a concatenation (with
    minuses), it will take the rightest operand (same operand)
    """
    max_operator_ = 0
    index = -1  # max operator index
    for cell in range(len(lst)):
        # if the current cell is a sign
        if lst[cell] in Operators().signs:
            s = lst[cell]
            power = Operators().signs[s][1]  # power
            if power > max_operator_:
                max_operator_ = power
                index = cell
    # index got the biggest operand's index

    # if the place's sign is LEFT
    if Operators().signs[lst[index]][2] is "LEFT":
        new_index = index
        cell = index + 1
        while cell < len(lst) - 1:
            # no concatenation or end of the concatenation
            if type(lst[cell]) is int or type(lst[cell]) is float:
                return new_index
            else:
                # concatenation
                if lst[cell] is lst[index]:
                    new_index = cell
                elif lst[cell] is '-':
                    if lst[cell + 1] is lst[index]:
                        new_index = cell + 1
                        cell += 1
            cell += 1
        return new_index  # LEFT operand
    return index  # no LEFT operand
