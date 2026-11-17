# dictionary declaration
person = { "name": "John", "age": 30, "city": "São Paulo" } # dictionary is a mutable collection of key-value pairs
print(f"My dictionary: {person}")
print(f"Length of my dictionary: {len(person)}")

# accessing values by key
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
# print(f"Last name: {person['last_name']}") # returns KeyError because "last_name" key does not exist in the dictionary

# Methods

## adding a new key-value pair
person["hair_color"] = "brown" # adding a new key-value pair to the dictionary
print(f"My dictionary after adding hair_color: {person}")

## updating an existing key-value pair
person["age"] = 25 # updating an existing key-value pair in the dictionary
print(f"My dictionary after updating age: {person}")

## del -> deleting a key-value pair from the dictionary
del person["hair_color"] # deleting a key-value pair from the dictionary
print(f"My dictionary after deleting hair_color: {person}")

## keys() -> getting all the keys in the dictionary
keys = person.keys() # or list(person.keys()) to get a list of keys
print("Keys in my dictionary:", keys)

## values() -> getting all the values in the dictionary
values = person.values() # or list(person.values()) to get a list of values
print("Values in my dictionary:", values)

## items() -> getting all the key-value pairs in the dictionary
items = person.items() # or list(person.items()) to get a list of key-value pairs
list_of_items = list(items) # converting the items view to a list of tuples
print("Items in my dictionary:", items)
print("First key-value %s = %s" % (list_of_items[0][0], list_of_items[0][1])) # printing the first key-value pair in the dictionary