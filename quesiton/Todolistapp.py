tasks = {}

while True:
    print("\nFeatures of To-Do List")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Mark as Done")
    print("4. Delete a Task")
    print("5. Exit")

    choice = int(input("Choose an option from 1 to 5: "))

    if choice == 1:
        task_desc = input("\nEnter your task: ")
        task_id = len(tasks) + 1
        tasks[task_id] = {"task": task_desc, "status": "Pending"}
        print(f"Task added successfully with ID {task_id}")

    if choice == 2:
        if not tasks:
            print("\nNo tasks available!")
        else:
            for task_id, details in tasks.items():
                print(f"{task_id}. {details['task']} - {details['status']}")

    if choice == 3:
        task_id = int(input("\nEnter task ID to mark as done: "))
        if task_id in tasks:
            tasks[task_id]["status"] = "Done"
            print("Task marked as done ")
        else:
            print("Invalid task ID!")

    if choice == 4:
        task_id = int(input("\nEnter task ID to delete: "))
        if task_id in tasks:
            del tasks[task_id]
            print("Task deleted successfully ")
        else:
            print("Invalid task ID!")

    if choice == 5:
        break
