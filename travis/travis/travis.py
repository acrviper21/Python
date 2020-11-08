# By: Erik Sistos
# 11/07/2020
# Description: This program creates a list of users and the security system compares
# the users to the list and asks if they want to be removed from the system or added
# if they're not in the system

# Create list of known users
known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
choice = "n"

# System keeps running until user wants to exit
while choice == "n":
    # Print security name and ask user for their name
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    # If user in known_users then asks if they want to be removed
    if name in known_users:
        print(f"Hello {name}")
        remove = input("Would you like to be removed from the system (Y/N)?: ").strip().lower()
        
        # If user wants to be removed then the system removes user from list
        if remove == "y":
            known_users.remove(name)

        # If user doesn't want to be removed then the program keeps running
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")

        # Ask user if they want to exit the program
        choice = input("Would you like to exit the system now (Y/N)?: ").strip().lower()
        print()
    else:
        # If name not in list ask user if they want to be added to list
        print(f"Hmmm I don't think I have met you yet {name}")
        add_me = input("Would you like to be added to the system (Y/N)?: ").strip().lower()

        # Add user to list if they want to be added
        if add_me == "y":
            known_users.append(name)

        # If user doesn't want to be removed then the program keeps running
        elif add_me == "n":
            print("No worries, see you around!")

        # Ask user if they want to exit the program
        choice = input("Would you like to exit the system now (Y/N)?: ").strip().lower()
        print()
            

