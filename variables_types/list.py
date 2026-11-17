# list declaration
my_list = [1, 2, "three", 4, "rocks", True] # list is a mutable collection of items in a particular order

print(f"My list: {my_list}")
print(f"Length of my list: {len(my_list)}")
print(f"First item in my list: {my_list[0]}")
print(f"Last item in my list: {my_list[-1]}")

my_list_target = my_list[1:5] # slicing the list to get a sublist
my_list_from_zero_to_target = my_list[:5] # slicing the list to get a sublist from the start to index 5
my_list_from_target_to_end = my_list[1:] # slicing the list to get a sublist from index 1 to the end
print(f"Target list: {my_list_target}")
print(f"List from zero to target: {my_list_from_zero_to_target}")
print(f"List from target to end: {my_list_from_target_to_end}")


# list methods
my_list[0] = "John"
print(f"my_list: {my_list}")

## append -> adding an item to the end of the list
my_list.append("Doe") 
print(f"my_list after append: {my_list}")

## index -> getting the index of an item in the list
idx = my_list.index("three")
print(f"Index of 'three': {idx}")

## insert -> inserting an item at a specific index
my_list.insert(2, "inserted") 
print(f"my_list after insert: {my_list}")

## pop -> removing an item at a specific index and returning it
popped_item = my_list.pop(2)
print(f"Popped item: {popped_item}")
print(f"my_list after pop: {my_list}")

## remove -> removing an item by value
my_list.remove("rocks")
print(f"my_list after remove: {my_list}")

## sort -> sorting the list in ascending order
my_list_numbers = [5, 2, 9, 1, 5]
print(f"my_list_numbers before sort: {my_list_numbers}")
my_list_numbers.sort()
print(f"my_list_numbers after sort: {my_list_numbers}")