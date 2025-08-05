def add_numbers(a, b):
    return a + b

# Correct usage
num1 = 5
num2 = 10
result = add_numbers(num1, num2)
print("Addition Result:", result)

# 1. Simulate TypeError
try:
    error_result = add_numbers("5", 10)  # string + int = TypeError
except TypeError as e:
    print("TypeError caught:", e)

# 2. Simulate ZeroDivisionError
try:
    division_result = 100 / 0  # Cannot divide by zero
except ZeroDivisionError as e:
    print("ZeroDivisionError caught:", e)

# 3. Simulate NameError
try:
    print(undefined_variable)  # This variable is not defined
except NameError as e:
    print("NameError caught:", e)
