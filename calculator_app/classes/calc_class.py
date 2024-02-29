class Calculator:
    """Models a calculator"""

    def __init__(self, num1, operator, num2):

        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def addition(self):
        result = self.num1 + self.num2
        return result

    def subtraction(self):
        result = self.num1 - self.num2
        return result

    def multiplication(self):
        result = self.num1 * self.num2
        return result

    def division(self):
        result = self.num1 / self.num2
        return result

    def calculation(self):
        if self.operator == "+":
            return self.addition()
        elif self.operator == "-":
            return self.subtraction()
        elif self.operator == "*":
            return self.multiplication()
        elif self.operator == "/":
            return self.division()
        else:
            return "Invalid operation."


if __name__ == "__main__":
    pass
