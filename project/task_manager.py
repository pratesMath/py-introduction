def add_task(tasks, task_name=""):
  task_dict = {"name": task_name, "is_completed": False}

  tasks.append(task_dict)

  print(f"Task '{task_name}' added successfully!")  
  return

def view_tasks(tasks):
  if not tasks:
    print("No tasks available.")
    return

  print("\nTasks:")
  for index, task in enumerate(tasks, start=1):
    task_name = task["name"]
    status = "Completed" if task["is_completed"] == True else "Pending"
    
    print(f"{index}. {task_name} - Status: {status}")

def update_task(tasks, task_index, new_task_name):
  index_adjusted = task_index - 1  # Adjust for 0-based indexing
  
  if index_adjusted < 0 or index_adjusted >= len(tasks):
    print("Invalid task index.")
    return
  
  tasks[index_adjusted]["name"] = new_task_name

  print(f"Task '{new_task_name}' updated successfully!")

def complete_task(tasks, task_index):
  index_adjusted = task_index - 1  # Adjust for 0-based indexing
  
  if index_adjusted < 0 or index_adjusted >= len(tasks):
    print("Invalid task index.")
    return
  
  tasks[index_adjusted]["is_completed"] = True

  print(f"Task '{tasks[index_adjusted]['name']}' marked as completed!")

def delete_task(tasks, task_index):
  index_adjusted = task_index - 1  # Adjust for 0-based indexing
  
  if index_adjusted < 0 or index_adjusted >= len(tasks):
    print("Invalid task index.")
    return
  
  deleted_task = tasks.pop(index_adjusted)

  print(f"Task '{deleted_task['name']}' deleted successfully!")

def delete_completed_tasks(tasks):
  for task in tasks:
    if task["is_completed"]: # or task["is_completed"] == True
      tasks.remove(task)
  print(f"Completed tasks deleted successfully!")
  return

tasks = []
while True:
  print("\nTask manager menu")
  print("1. Add task")
  print("2. View tasks")
  print("3. Update task")
  print("4. Complete task")
  print("5. Delete task")
  print("6. Delete completed tasks")
  print("7. Exit")

  choice = int(input("Enter your choice (1-7): "))

  if choice == 1:
    task_name = input("Enter the task name: ")
    add_task(tasks=tasks, task_name=task_name)
  elif choice == 2:
    view_tasks(tasks)
  elif choice == 3:
    view_tasks(tasks)
    task_index = int(input("Enter the task index to update: "))
    new_task_name = input("Enter the new task name: ")
    update_task(tasks, task_index, new_task_name)
  elif choice == 4:
    view_tasks(tasks)
    task_index = int(input("Enter the task index to complete: "))
    complete_task(tasks, task_index)
  elif choice == 5:
    view_tasks(tasks)
    task_index = int(input("Enter the task index to delete: "))
    delete_task(tasks, task_index)
    view_tasks(tasks)
  elif choice == 6:
    delete_completed_tasks(tasks)
    view_tasks(tasks)
  elif choice == 7:
    print("Exiting the task manager. Goodbye!")
    break