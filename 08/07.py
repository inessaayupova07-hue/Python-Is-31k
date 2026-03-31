class Calculator:
    def calculate(self, x, y):
        return x + y

class SafeCalculator(Calculator):
    def calculate(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            return "Error"
        return x + y

calc = SafeCalculator()

print(calc.calculate(2, 3))
print(calc.calculate(2, "a"))
