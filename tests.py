import pytest
from listMaker import Into_list
from solver import solve
from excptions import *


# function that gets the invalid exercise, and the expected
# error message.
# assert true if the error from the exercise is equal to the
# expected message, elsewhere false
def valid_test(exercise, expected):
    with pytest.raises(Validation) as error:
        Into_list(exercise)
    assert error.value.args[0] == expected


# function that gets the exercise, and the expected solution
# assert true if the solution from the exercise is equal to the
# expected message, elsewhere false
def solving_test(exercise, expected):
    lst = Into_list(exercise)
    solve(lst.list)
    assert lst.list[0] == expected


# syntax mistakes

def test_syntax1():
    valid_test("3^*2",
               "Error Input :Operators in sequence '^' '*'")


def test_syntax2():
    valid_test("3+*2",
               "Error Input :Operators in sequence '+' '*'")


def test_syntax3():
    valid_test("(3@)&2", "Error Input : Missing number between an "
                         "operator '@' and bracket ')'")


def test_syntax4():
    valid_test("3-(!5)*2",
               "Error Input : Invalid character '!' after bracket '(")


def test_syntax5():
    valid_test("3-(8)---!2",
               "Error Input :Operators in sequence '-' '!'")


def test_syntax6():
    valid_test("3~2",
               "Error Input : Invalid character before the operand : '~'")


def test_syntax7():
    valid_test("((3*2))-8",
               "Error Input : unNecessary brackets")


def test_syntax8():
    valid_test("3-(2*8)(8-0)",
               "Error Input : Missing an operand between the brackets ")


def test_syntax9():
    valid_test("3+()+2",
               "Error Input : Brackets are empty")


def test_syntax10():
    valid_test("3+k-~2",
               "Error Input : InValid character  'k'")


# gibberish
def test_gibberish():
    valid_test("hack ish656546jnl*($%",
               "Error Input : InValid character  'h'")


# empty
def test_empty():
    valid_test("", "Error Input : Empty Input")


# white spaces
def test_white_spaces():
    valid_test("  \t  \n  "
               "            ", "Error Input : Empty Input")


# simple exercises
def test_good_ex1():
    solving_test("5+6", 11)


def test_good_ex2():
    solving_test("5*-6", -30)


def test_good_ex3():
    solving_test("5%6*2", 10)


def test_good_ex4():
    solving_test("5&6", 5)


def test_good_ex5():
    solving_test("3!+9", 15)


def test_good_ex6():
    solving_test("-5+~6", -11)


def test_good_ex7():
    solving_test("---~~~-~5+6", 11)


def test_good_ex8():
    solving_test("5$6", 6)


def test_good_ex9():
    solving_test("72/5", 14.4)


def test_good_ex10():
    solving_test("(6^2)", 36)


def test_good_ex11():
    solving_test("5@6", 5.5)


def test_good_ex12():
    solving_test("5!@6-~1", 64)


def test_good_ex13():
    solving_test("5/5/6*12", 2)


def test_good_ex14():
    solving_test("5----(10^2/10)", 15)


def test_good_ex15():
    solving_test("(30$99)", 99)


def test_good_ex16():
    solving_test("8*8.878@6", 59.512)


def test_good_ex17():
    solving_test("--~-~~~~~-~7&7*4", -28)


def test_good_ex18():
    solving_test("3!-~(3!)", 12)


def test_good_ex19():
    solving_test("(6^1)@(200%80)", 23)


def test_good_ex20():
    solving_test("(--(7+7))", 14)


# hard exercises
def test_long_ex1():
    solving_test("(-1--1-1-1-1)--2-24/(4*2)+3.100+4!+(~1)", 22.1)


def test_long_ex2():
    solving_test("(8^3%2&66@45%((22%4$2^2)+7*6)^~2 *60*10^8)%1", 0.18359375)


def test_long_ex3():
    solving_test("7&8*22  ^3!-7^3+( (22  %2 * 7)+3$5^3&~7)", 793658985.0000128)


def test_long_ex4():
    solving_test(" 24%12^2-7*9&(2+3-4+6$22--8--~((9+8)!))%30", -7)


def test_long_ex5():
    solving_test("---~4+67 * 2-4522/221+(2&23 * 22%3^2)-7*2@4+2%77",
                 100.53846153846155)


def test_long_ex6():
    solving_test("(123 @ ((145*2/4%6-6/7) @ (3^5 - 9000)))",
                 -2109.839285714286)


def test_long_ex7():
    solving_test("87^3  %2&66@4   *~5%((22%4$2^2)+7 *6!)^2 *6",
                 152349126)


def test_long_ex8():
    solving_test("----(8*--8)$5+2%456+9*9*~(6+6)+2^(-(1+1))", -905.75)


def test_long_ex9():
    solving_test("14$5%2&4+4+4-7.7 + ~(5*3$2)", -14.7)


def test_long_ex10():
    solving_test("005*2^2&2-7&88+224@26-(43 -44+66&2----45*(321&2))", 47)


def test_long_ex11():
    solving_test("87^3  %2&66@4   *~5%((22%4$2^2)+7 *6!)^2 *6", 152349126.0)


def test_long_ex12():
    solving_test("~ ( (88/23*2.2)^ 3&(5!+ --- 6^3) )", -1.5239066784713154e-89)


def test_long_ex13():
    solving_test("( (1+(3+(5*7)-9)@4.56) * (2.5) ) / ~(-5.12)", 8.681640625)


def test_long_ex14():
    solving_test("87^3  %2&66@4   *~5%((22%4$2^2)+7 *6!)^2 *6", 152349126.0)


def test_long_ex15():
    solving_test("18- 6^2+5%4 $ 3+2+4+5+6 ------- 9+7& 5/3.2 % 4.2", -7.4375)


def test_long_ex16():
    solving_test("24%12^2-7*9&(2+3-4+6$22--8--~((9+8)!))", 2489811996671783.0)


def test_long_ex17():
    solving_test("7&(88*9)---4^5@2!+(65^0.5)-787878/5050", -268.9531877962559)


def test_long_ex18():
    solving_test("~(123@((145*2/4%6-6/7)@(3^5-9000)))", 2109.839285714286)


def test_long_ex19():
    solving_test("~(~((576&969)-60+5%3)@333+7!-8^3)", -4435.5)


def test_long_ex20():
    solving_test("55%66$78^2+5----65^2*((3$5^7@555)+6^2&12^2)-2",
                 1.0874215407751212e+200)
