# if, elif, else statements
age = 21

if age < 0:
	print("Invalid age!")
elif age > 0 and age < 13:
	print("You are a child.")
elif age >= 13 and age < 18:
	print("You are a teenager.")
elif age >= 18 and age < 65:
  print("You are an adult.")
else:
  print("You are a senior citizen.")

# inline if statement
message = "You are a minor." if age < 18 else "You are an adult."
print(message)