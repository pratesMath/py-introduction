# int (integer) - whole numbers, positive or negative, without decimals, of unlimited length.
int_number = 3 # int

print(f"Integer: {int_number}") # or print("Integer: ", int_number)

# float (floating point) - numbers, positive or negative, containing one or more decimals.
float_number = 3.14 # float

print(f"Float: {float_number} ({type(float_number)})")

# type() - returns the type of the variable.
print(f"{float_number} is {type(float_number)}")

# Arithmetic operations with numbers
a = 4
b = 2
sum_numbers = a + b
subtract_numbers = a - b
multiply_numbers = a * b
divide_numbers = a / b
remainder_numbers = a % b

print(f"A: {a}, B: {b}")
print(f"Sum: {sum_numbers}")
print(f"Subtraction: {subtract_numbers}")
print(f"Multiplication: {multiply_numbers}")
print(f"Division: {divide_numbers}")
print(f"Remainder: {remainder_numbers}")

print(int(2.5) == 2)
print(float(2) == 2.0)