def greeting(name):
  print(f"Hello, {name}!")

greeting("Alice")

# function w/ return

def square(num):
  return num ** 2 # or num * num

print("square = %d" % square(4))  # Output: 16

def sum(a,b):
  return a + b

print("sum = %d" % sum(3, 5))  # Output: 8