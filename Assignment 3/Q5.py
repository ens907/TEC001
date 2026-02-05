attempts = 0

while True:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    username = str("python")
    password = str("rules")

    attempts = attempts + 1

    if username_input == username and password_input == password:
        print("Welcome")
        break
    if attempts >= 5:
        print("Access denied")
        break
    