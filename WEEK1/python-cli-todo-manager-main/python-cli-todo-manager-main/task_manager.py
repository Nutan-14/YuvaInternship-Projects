tasks = []
def add_task():
    title = input("Enter task: ")

    if title.strip() == "":
        print("❌ Task cannot be empty!")
        return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print("✅ Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("📭 No tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for task in tasks:
        status = "✔ Done" if task["completed"] else "❌ Not Done"

        print(f"{task['id']}. {task['title']} - {status}")

    print("======================\n")

def remove_task():
    if len(tasks) == 0:
        print("📭 No tasks to remove.")
        return

    try:
        task_id = int(input("Enter Task ID to remove: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("🗑️ Task removed successfully!")
            return

    print("❌ Task ID not found.")

def mark_completed():
    if len(tasks) == 0:
        print("📭 No tasks available.")
        return

    try:
        task_id = int(input("Enter Task ID to mark as completed: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("✅ Task marked as completed!")
            return

    print("❌ Task ID not found.")