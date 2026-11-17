my_list = [1,2,3,4,5]

print("Iterating through a list:")
for item in my_list:
  print(item)

print("\nIterating through a tuple:")
my_tuple = (1,2,3,4,5)

for item in my_tuple:
	print(item)

print("\nIterating through a dictionary:")
my_dict = {'name': "John", 'age': 25, 'country': "USA"}

print("Keys:")
for key in my_dict.keys():
	print(key)

print("Values:")
for value in my_dict.values():
	print(value)

print("Items:")
for key, value in my_dict.items():
	print(f"{key}: {value}")


print("\nUsing range() function:")
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]

print("\nIterating through a range:")
for n in range(5): # or for n in range(0,5):
	print("Number:",n)

print("\nIterating through a range with len:")
my_list = [1,2,3,4,5]

for i in range(0, len(my_list)):
	print("Index:", i, "Value:", my_list[i])
	if my_list[i] % 2 == 0:
		print("Even value found:", my_list[i])

print("\nIterating through a range with enumerate:")

for i, value in enumerate(my_list):
	print("Index:", i, "Value:", value)
	if value % 2 != 0:
		print("Odd value found:", value)