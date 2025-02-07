class BasicCalc:
    def add(self, num1, num2):
        if ((isinstance(num1, int) or isinstance(num1, float)) and
                (isinstance(num2, int) or isinstance(num2, float))):
            return num1+num2
        return None

    def subtract(self, num1,num2):
        if ((isinstance(num1, int) or isinstance(num1, float)) and
                (isinstance(num2, int) or isinstance(num2, float))):
            return num1 - num2
        return None

    def multiply(self, num1, num2):
        if ((isinstance(num1, int) or isinstance(num1, float)) and
                (isinstance(num2, int) or isinstance(num2, float))):
            return num1 * num2
        return None

    def divide(self, num1, num2):
        if ((isinstance(num1, int) or isinstance(num1, float)) and
                (isinstance(num2, int) or isinstance(num2, float))):
            return num1 / num2
        return None

if __name__ == '__main__':
    basic_calc = BasicCalc()
    num1 = int(input("First numba: "))
    num2 = int(input("Second numba: "))
    print(f"{num1} + {num2} = {basic_calc.divide(num1, num2)}")