# string declaration
greeting = "Hello, World!"

print(f"Text : {greeting}")

string_with_quotes = 'John "Doe"'
print(f"String with quotes: {string_with_quotes}")

string_with_apostrophe = "John's book"
print(f"String with apostrophe: {string_with_apostrophe}")

string_with_escape = "John\'s book"
print(f"String with escape character: {string_with_escape}")

string_with_newline = "Hello\nWorld"
print(f"String with newline: {string_with_newline}")

string_with_tab = "Hello\tWorld"
print(f"String with tab: {string_with_tab}")

string_with_multiline = """This is a
multiline string."""
print(f"String with multiline: {string_with_multiline}")

# formatting strings
name = "James"
last_name = "Bond"

full_name = f"{name} {last_name}"
print(f"Full name: {full_name}")

print("My name is", last_name + ".", name, last_name)
# or (f-strings)
print(f"My name is {last_name}. {name} {last_name}")
# or ( % formatting )
print("My name is %s. %s %s" % (last_name, name, last_name))
# or ( .format() method )
print("My name is {}. {} {}".format(last_name, name, last_name))

# more used string methods
upper_name = name.upper() # returns a new string with all characters in uppercase
print(f"Uppercase name: {upper_name}")

lower_name = name.lower() # returns a new string with all characters in lowercase
print(f"Lowercase name: {lower_name}")

length_name = len(name) # returns the length of the string
print(f"Length of name: {length_name}")

first_character = name[0] # returns the first character of the string
print(f"First character of name: {first_character}")

last_character = name[-1] # returns the last character of the string
print(f"Last character of name: {last_character}")

count_a = name.count("a") # returns the number of occurrences of a substring in the string
print(f"Count of 'a' in name: {count_a}")

find_a = name.find("a") # returns the index of the first occurrence of a substring in the string
print(f"Index of first occurrence of 'a' in name: {find_a}")

name_in_bytes = name.encode() # returns a bytes object representing the string
print(f"Name in bytes: {name_in_bytes}")

name_in_bytes_decoded = name_in_bytes.decode() # returns a string decoded from the bytes object
print(f"Name decoded from bytes: {name_in_bytes_decoded}")

name_replaced = full_name.replace("a", "o") # returns a new string with all occurrences of a substring replaced
print(f"Name with 'a' replaced by 'o': {name_replaced}")

phone_number = "(11) 12345-6789"
replaced_phone_number = phone_number.replace("(", "").replace(")", "").replace("-", "").replace("+", "").replace(" ", "")

print(f"Phone number with special characters removed: {replaced_phone_number}")

name_joined = "-".join(name) # returns a new string with the elements of the iterable joined by the specified separator
print(f"Name joined with '-': {name_joined}")

name_split = full_name.split() # returns a list of substrings split by the specified separator
print(f"Name split by ' ': {name_split}")

name_stripped = "   James   ".strip() # returns a new string with leading and trailing whitespace removed
print(f"Name stripped of whitespace: '{name_stripped}'")
name_lstripped = "   James   ".lstrip() # returns a new string with leading whitespace removed
print(f"Name left stripped of whitespace: '{name_lstripped}'")
name_rstripped = "   James   ".rstrip() # returns a new string with trailing whitespace removed
print(f"Name right stripped of whitespace: '{name_rstripped}'")

name_startswith = name.startswith("J") # returns True if the string starts with the specified prefix
print(f"Does name start with 'J'? {name_startswith}")
name_endswith = name.endswith("s") # returns True if the string ends with the specified suffix
print(f"Does name end with 's'? {name_endswith}")

name_with_in = "James" in full_name # returns True if the substring is found in the string
print(f"Is 'James' in full name? {name_with_in}")

name_with_not_in = "James" not in full_name # returns True if the substring is not found in the string
print(f"Is 'James' not in full name? {name_with_not_in}")