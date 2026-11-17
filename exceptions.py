while True:
  try:
    number = int(input("Enter a number: "))
    result = 10 / number
  except ValueError as e:
    print(f"Value Error: {e}")
    raise ValueError("Invalid input. Please enter a valid number.")
  except ZeroDivisionError as e:
    print(f"Zero Division Error: {e}")
  except Exception as e:
    print(f"Unexpected Error: {e}")
  else:
    print(f"Result: {result}")
  finally:
    print("Execution completed.")