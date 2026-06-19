import hashlib

print("=" * 30)
print("SECURE NOTES SYSTEM")
print("=" * 30)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Enter username: ").strip()

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()

        for user in users:
            stored_username = user.strip().split(":")[0]

            if username == stored_username:
                print("Username already exists.")
                return

    except FileNotFoundError:
        pass

    if len(username) < 3:
        print("Username must be at least 3 characters long.")
        return

    password = input("Enter password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return

    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return

    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return

    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
        return

    hashed_password = hash_password(password)

    with open("users.txt", "a") as file:
        file.write(f"{username}:{hashed_password}\n")

    print("User registered successfully!")

def add_note(username):
    note = input("Enter your note: ")

    with open("notes_data.txt", "a") as file:
        file.write(f"{username}|{note}\n")

    print("Note added successfully!")

def view_notes(username):
    print("\nYour Notes:")

    try:
        with open("notes_data.txt", "r") as file:
            notes = file.readlines()

        for note in notes:
            stored_username, user_note = note.strip().split("|")

            if stored_username == username:
                print("-", user_note)

    except FileNotFoundError:
        print("No notes found.")

def user_dashboard(username):
    while True:
        print("\n===== USER DASHBOARD =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note(username)

        elif choice == "2":
            view_notes(username)

        elif choice == "3":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice.")

def login_user():
    username = input("Enter username: ").strip()
    
    password = input("Enter password: ")

    entered_hash = hash_password(password)

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        stored_username, stored_hash = user.strip().split(":")

        if username == stored_username and entered_hash == stored_hash:
            print("Login Successful")
            user_dashboard(username)
            return

    print("Invalid Username or Password")
    
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register_user()

    elif choice == "2":
        login_user()

    elif choice == "3":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Please try again.")

add_note("nutan")

  