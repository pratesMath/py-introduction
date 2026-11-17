# Boolean values
true = True
false = False

print(f"Is true? {true}")
print(f"Is false? {false}")

if True:
    print("This will always execute because the condition is True.")
else:
    print("This will never execute because the condition is True.")

# logical operators

## and
if True and True:
    print("Both conditions are True.")
elif True and False:
    print("This will not execute because one condition is False.")

## or
if True or True:
    print("Both conditions are True.")
if True or False:
    print("This will not execute because one condition is False.")