import task_manager as tm


def show_menu():
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task Completed")
    print("5. Exit")


def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            tm.add_task()

        elif choice == "2":
            tm.view_tasks()

        elif choice == "3":
            tm.remove_task()

        elif choice == "4":
            tm.mark_completed()

        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()