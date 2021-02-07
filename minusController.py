from operators import Operators


def minusSign(lst, index_operator):
    """
    The function gets from the solver function the list and the index
    in the list of the max operator.
    The function checks if there is a minus as sign of the operand for
    the given operator and includes the minus in the operand.
    :param lst: the list
    :param index_operator: the index of the operator
    """
    if not (index_operator < len(lst) - 1):
        return
    # if the operand is "MIDDLE" or "LEFT" and the next index is '-'
    # it will include the '-' into the operand after and delete the '-'
    if lst[index_operator + 1] == \
            '-' and Operators().signs[lst[index_operator]][2] is not "RIGHT":
        lst[index_operator + 2] *= -1
        del lst[index_operator + 1]

    # if the index is 0 and it is '-' or the previous cell is an open
    # bracket it includes the minus in the next cell which is an
    # operand and deletes the minus
    elif index_operator is 0 and lst[0] is '-' or \
            lst[index_operator - 1] in Operators().open_brackets:
        lst[index_operator + 1] *= -1
        del lst[index_operator]


def minusHandler(lst):
    """
    A function that handles all the sequences of minus.
    Separates the minus between an operator and a sign.
    """
    cell = 0
    # while cell is before the list's length
    while cell < len(lst) - 1:
        sequence_of_minus = 0  # counter of minuses in sequence
        sequence_after_cell = cell
        # while the list isn't over or there is no more minuses in the
        # sequence it counts the num of minuses in a sequence
        while sequence_after_cell < len(lst) and \
                lst[sequence_after_cell] == '-':
            sequence_of_minus += 1  # counter of minuses +=1
            sequence_after_cell += 1
        # if there is more than one minus and the number is even
        if sequence_of_minus > 1 and sequence_of_minus % 2 == 0:
            # delete all the occurrences in the current sequence
            del lst[cell:sequence_after_cell]
            # if before the sequence there is an open brackets or the
            # cell is in index 0, it will continue. elsewhere it will
            # insert an '+' before the sequence
            if cell == 0:
                pass
            elif lst[cell - 1] in Operators().open_brackets:
                pass
            elif lst[cell - 1] in Operators().signs and \
                    Operators().signs[lst[cell - 1]][2] != "RIGHT":
                pass
            else:
                lst.insert(cell, '+')
        # there is more than one minus and the number is not even
        elif sequence_of_minus > 1:
            # deletes all the sequence except the first '-'
            del lst[cell + 1:sequence_after_cell]
        cell += 1
