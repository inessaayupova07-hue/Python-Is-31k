def process_data(a, b):
    try:
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            return "Conversion error"

        return a / b
    except ZeroDivisionError:
        return "Division by zero"


print(process_data("10", "2"))
print(process_data("10", "0"))
print(process_data("a", "2"))
