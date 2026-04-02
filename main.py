import os

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as f:
        data = f.read()
        tasks = eval(data)
else:
    tasks = {}

def add_task(tasks):
    title = input("Enter the task title: ")
    note = input("Enter the task note (If any): ")

    if tasks:
        new_id = max(tasks.keys()) + 1
    else:
        new_id = 1

    tasks[new_id] = {
        "title": title,
        "status": "Pending",
        "note": note
    }

    print("Task added successfully")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return

    for id, task in tasks.items():
        print("ID:", id)
        print("Title:", task["title"])
        print("Status:", task["status"])
        print("Note:", task["note"])
        print("------------------")

def delete_task(tasks):
    task_id = int(input("Enter the ID for the task you want to DELETE: "))

    if task_id in tasks:
        del tasks[task_id]
        print("Task Deleted Successfully")
    else:
        print("Task not found")

def change_status(tasks):
    task_id = int(input("Enter the task you want to change status: "))

    if task_id in tasks:
        tasks[task_id]["status"] = "Completed"
        print("Task marked as completed")
    else:
        print("Task not found")

while True:
   
    print("1. Add a task")
    print("2. View a task")
    print("3. Delet a task")
    print("4. Change the Status to Completed")
    print("5. Exit")
    choice=int(input("Enter your choice : "))
    

    if choice == 1:
        add_task(tasks)
    elif choice == 2:
        view_tasks(tasks)
    elif choice == 3:
        delete_task(tasks)
    elif choice == 4:
        change_status(tasks)
    elif choice == 5:
        print("Exiting...")
        break


with open("tasks.txt", "w") as f:
    f.write(str(tasks))
