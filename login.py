import json

while True:
    choice = int(input("Create an account, No / Yes (0/1): "))

    if choice == 1 or choice == 0:
        break
    else:
        print("Invalid choice: (0/1)")

while True:
    if choice == 0:
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        with open("accounts.json","r") as f:
            users = json.load(f)
            users[str(username)] = password

        if password and username in users:
            print("Succesfully logged in \n")
            break
        else:
            print("Invalid Username / password \n")



    if choice == 1:
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        with open("accounts.json","r") as f:
            users = json.load(f)

        if username in users:
            print(f"Username ({username}) is in use \n Try another.")
            f.close()
        else:
            users[str(username)] = password
            f.close()

            with open("accounts.json","w") as f:
                json.dump(users, f, indent=4)
            print("Account Saved")
            break

print(f"Login: {username} , {password}")
while True:
    cmd = str(input("=>"))
    print("THERE IS NOTHING HERE BYE")
    break
