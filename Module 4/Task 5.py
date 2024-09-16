username = "python"
password = "rules"


i = 0
attempts = 0
while i < 5:

    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    if input_username == username and input_password ==password:
        print("login successful")
        break
    else:
        attempts += 1
        if attempts < 5:
            print("login failed")
        else:
            print("access denied")
            i = i + 1
