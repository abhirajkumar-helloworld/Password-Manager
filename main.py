import random
import string
from getpass import getpass
accounts = []
try:
    with open("passwords.txt", "r") as f:
        accounts = [line.strip() for line in f]
except:
    pass
while True:
    print("1. Add account")
    print("2. View account")
    print("3. Search account")
    print("4. Delete account")
    print("5. Update password")
    print("6. Generate random password")
    print("7. Exit")
    try:
        choice = input("Enter your choice : ")
    except:
        continue
    
    if choice == "7":
        print("exiting......")
        break
    
    elif choice == "1":
        website = input("Website : ")
        username = input("Username : ")
        password = getpass("Password :")
        data = f"{website} | {username} | {password}"
        accounts.append(data)
        with open("passwords.txt", "a") as f:
            f.write(data + "\n")
        print ("Data saved")
    
    elif choice == "2":
        if len(accounts) == 0:
            print("No user account")
        else:
            for i, account in enumerate(accounts, start=1):
                print (i, account)
    
    elif choice == "3":
        if len(accounts) == 0:
            print("No user accounts")
        else:
            keyword = input("Search website : ").lower()
            found = False
            for account in accounts:
                if keyword in account.lower():
                    print(account)
                    found = True
            if not found:
                print ("No account found")
    
    elif choice == "4":
        if len(accounts) == 0:
            print("No account")
        else:
            try:
                delete = int(input("Which account you want to delete : "))
                if delete > len(accounts) or delete <= 0:
                    print("Enter a valid num.")
                else: 
                    accounts.pop(delete - 1)
                    print("account deleted")
                    with open("passwords.txt", "w") as f:
                        for account in accounts:
                            f.write(account + "\n")
            except ValueError:
                print("Enter a valid num.")

    elif choice == "5":
        if len(accounts) == 0:
            print("No user account")
        else:
            try:
                upd = int(input("which account no. to update : "))
                if upd > len(accounts) or upd <= 0:
                    print("Invalid account number")
                else:
                    new_password = getpass("new_password : ")
                    parts = accounts[upd - 1].split(" | ")
                    parts[2] = new_password
                    accounts[upd - 1] = " | ".join(parts)
                    with open ("passwords.txt", "w") as f:
                        for account in accounts:
                            f.write(account + "\n")
                    print ("Password updated successfully")
            except ValueError:
                print("Enter a valid number")
    
    elif choice == "6":
        password = ""
        chars = string.ascii_letters + string.digits + string.punctuation
        try:
            passlen = int(input("Password length : "))
        except ValueError:
            print("enter a valid number")
            continue
        if passlen < 6 or passlen > 12:
            print ("Password length should be between 6-12")
        else:
            for i in range(passlen):
                password += random.choice(chars)
            print("Generated Password :", password)

    print("-----------------------------")