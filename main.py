from listMaker import Into_list
from solver import solve
from prints import start
from excptions import *


def main():
    start()
    while True:
        try:
            # gets the input from the user
            input_str = input(
                "\nenter an exercise, for exit type \"exit\" :\n")
            print("")
        except BaseException as e:
            print(e)
            # if there is an exception, the while loop will start again
            continue
            # delete all the white spaces in the string
        input_str = input_str.replace(' ', '').replace('\t', ''). \
        replace('\n', '')
        if input_str.lower() == "exit":
            # end of the program
            print("\nThank you for using my calculator program!!")
            break

        try:
            # turns the user's string into a list
            lst = Into_list(input_str)
        # if there is an exception, the while loop will start again
        except Validation as e:
            print(e)
            continue
        try:
            # function that changes the list into its result
            solve(lst.list)
        # if there is an exception, the while loop will start again
        except RecursionError as e:
            print("maximum recursion depth, try again")
            continue
        except KeyError as er:
            print("error :" + str(er))
            continue
        except OverFlow as e:
            print(e)
            continue
        except Operators_ex as e:
            print(e)
            continue

        # prints the result
        if len(lst.list) == 1:
            print("The answer is :\n", lst.list[0])


if __name__ == '__main__':
    main()
