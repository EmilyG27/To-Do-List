tasks = []

def add_task():
    task = input("please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")

def view_task():
    if not tasks:
        print("There are no tasks.")
    else:
        print("Current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task number {index}. {task}")
    for i in range ( len(tasks)):
        if " Incomplete" != task:
            tasks[i] = tasks[i] + " Incomplete"
        else:
            break

def mark_completed():
    view_task()
    try:
        complete_input = int(input("Enter the number of the task you completed: "))
        if complete_input < len(tasks):
            tasks[complete_input] = tasks[complete_input].replace(" Incomplete", " Completed")
            print(f"Task {complete_input} marked as completed.")
        else:
            print("Task not found.")
    except ValueError:
            print("Invalid input. Please enter a number.")

def delete_task():
    view_task()
    try:
        task_to_delete = int(input("Enter the number of the task to delete: "))
        if task_to_delete < len(tasks):
            tasks.pop(task_to_delete)
            print(f"Task {task_to_delete} was deleted")
        else:
            print(f" Task {task_to_delete} was not found")
    except:
        print("Invalid input.")

while True:
    choose = int(input("1. Add a task\n2. View tasks\n3. Mark a task as completed\n4. Delete a task\n5. Quit\nPlease choose a number:"))

    if choose == 1:
        add_task()
    elif choose == 2:
       view_task()
    elif choose == 3:
        mark_completed()
    elif choose == 4:
        delete_task()
    elif choose == 5:
       quit
    else:
       print("Please enter a number from the list.")
    