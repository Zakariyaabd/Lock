from lock import smart_lock

def main():
    password = {}

    pm = smart_lock()

    print(""" Hello, What would you like to do?
    Enter 1 to create a new Key (end key in .key)
    Enter 2 to load an existing key
    Enter 3 to create a new password file
    Enter 4 to load an existing password file
    Enter 5 to create a new password
    Enter 6 to get a pasword from a file 
    Enter 7 to quit. """)
    done = False

    while not done:

        mode = input("Enter your choice: ")
        if mode == "1":
            path = input("Generate key: ")
            pm.create_key(path)
        elif mode == "2":
            path = input("Load key: ")
            pm.load_key(path)
        elif mode == "3":
            path = input("Enter name for new file: ")
            pm.create_file(path, password)
        elif mode == "4":
            path = input("Enter name for existing file: ")
            pm.load_file(path)
        elif mode == "5":
            site = input("enter site:")
            password = input("enter password: ")
            pm.add_password(site, password)
        elif mode == "6":
            site = input("what site do you want: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif mode == "q":
            done = True
        else:
            print("invalid choice ")


if __name__ == "__main__":
    main()
