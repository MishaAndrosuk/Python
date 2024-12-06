users = {"Misha": "qwerty", "Sasha": "asdfgh", "Dasha": "zxcvb3n", "Pasha": "weqpriu34"}

def add_user(username, password):
    if username in users:
        print("The user is already in the dictionary")
    users[username] = password
    print("User added successfully")


def remove_user(user):
    if user in users:
        del users[user]
        print("User removed successfully")
    else:
        print("The user is not in the dictionary")


def change_user_password(username, new_password):
    if username in users:
        if users[username] != new_password:
            users[username] = new_password
            print("Password changed successfully")
        else:
            print("New password must be different from the old password")
    else:
        print("User not found")


def get_user_password(username):
    if username in users:
        return  users[username]
    else:
        return "User not found"


def is_weak_password(password):
    if len(password) < 6 or password.isalpha():
        return True
    else:
        return False

while True:
    print("Menu:")
    print("1. Print all users")
    print("2. Add user")
    print("3. Remove user")
    print("4. Change password")
    print("5. Check passwords")
    print("6. Get information about password")
    print("7. Save users to file")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(users)
    elif choice == "2":
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        add_user(username, password)
    elif choice == "3":
        user = input("Enter the user to remove: ")
        remove_user(user)
    elif choice == "4":
        username = input("Enter the user to change: ")
        new_password = input("Enter the new password: ")
        change_user_password(username, new_password)
    elif choice == "5":
        for username, password in users.items():
            if is_weak_password(password):
                print(f"User: {username}, has week password")
    elif choice == "6":
        username = input("Enter the username: ")
        print(get_user_password(username))
    elif choice == "7":
        with open("users.txt", "w") as file:
            for username, password in users.items():
                file.write(f"{username}: {password}\n")   
        file.close()             
        print("Users saved to file")         
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")








