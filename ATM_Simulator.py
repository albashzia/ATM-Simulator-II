def main_menu():
    print("\n======WELCOME TO ATM======")
    print("1. Account Holder")
    print("2. General User")
    choice = input("Enter choice: ")
    if choice == "1":
        print("Call account holder login")
    elif choice == "2":
        print("Call main menu for general user")
    else:
        print("Invalid Option")

#=========== Program Start ==============
main_menu()