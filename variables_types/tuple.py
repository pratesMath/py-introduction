# tuple declaration
my_tuple = (1, 2, 2, 3, 4, 5) # tuple is an immutable collection of items in a particular order

print(f"My tuple: {my_tuple}")
print(f"Length of my tuple: {len(my_tuple)}")
print(f"First item in my tuple: {my_tuple[0]}")
print(f"Last item in my tuple: {my_tuple[-1]}")

# methods

## count -> counting the number of occurrences of an item in the tuple
count_of_2 = my_tuple.count(2)
print(f"Count of 2 in my tuple: {count_of_2}")

## index -> getting the index of an item in the tuple
idx_of_3 = my_tuple.index(3)
print(f"Index of 3 in my tuple: {idx_of_3}")