# exception that handles the error of factorial to a float number
class Factorial_float(Exception):
    def __init__(self, message):
        self.message = message
        raise Operators_ex(self.message)


# exception that handles the error of factorial to a negative number
class Factorial_minus(Exception):
    def __init__(self, message):
        self.message = message
        raise Operators_ex(self.message)


# exception that handles the error of over flow with a specific message
class OverFlow(Exception):
    def __init__(self, message):
        self.message = message


# exception that handles the error in the validation of the exercise
class Validation(Exception):
    def __init__(self, message):
        self.message = message


# exception that handles the error in some operators' calculations
class Operators_ex(Exception):
    def __init__(self, message):
        self.message = message
