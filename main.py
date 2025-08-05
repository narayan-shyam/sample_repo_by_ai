def add_numbers(a, b):
    return a + b

# Simulate correct usage
num1 = 5
num2 = 10
result = add_numbers(num1, num2)
print("Addition Result:", result)

# Simulate error (passing string instead of number)
try:
    error_result = add_numbers("5", 10)  # This will raise a TypeError
    print("This won't be printed:", error_result)
except TypeError as e:
    print("Caught an error:", e)
