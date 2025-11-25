accounts = [
    {"name": "Ahmed",  "account_no": "49217385", "pin": "1234", "balance": 12000},
    {"name": "Fatima", "account_no": "83726149", "pin": "6789", "balance": 18000},
    {"name": "Sara",   "account_no": "59102836", "pin": "1111", "balance": 25000},
    {"name": "Bilal",  "account_no": "74839215", "pin": "2222", "balance": 5000},
    {"name": "Ayesha", "account_no": "36581942", "pin": "3333", "balance": 15000},
    {"name": "Ali",    "account_no": "91427638", "pin": "4444", "balance": 20000},
    {"name": "Hassan", "account_no": "28637491", "pin": "5555", "balance": 3000},
    {"name": "Fatima", "account_no": "67358214", "pin": "6666", "balance": 40000},
    {"name": "Zain",   "account_no": "15983726", "pin": "7777", "balance": 8000},
    {"name": "Maria",  "account_no": "42819573", "pin": "8888", "balance": 22000}
]

def find_account(account_no):
    for acc in accounts:
        if acc["account_no"] == account_no:
            return acc
    return None

def account_holder_login():
    acc_no = input("Enter account number: ")
    acc = find_account(acc_no)
    if acc is None:
        print("Account not found")
        return
    attempts = 3
    while attempts > 0:
        pin = input("Enter pin:")
        if pin == acc["pin"]:
            print("Welcome",acc["name"])
            member_menu(acc)
            return
        else:
            attempts = attempts - 1
            print("Incorrect Pin! Attempts left",attempts)
    print("Too many failed attempts. Account Locked!")

def view_balance_member(acc):
    print("Account Holder: ",acc["name"])
    print("Balance :",acc["balance"])

def member_menu(acc):
    while True:
        print("\n--- ATM Menu (Account Holder) ---")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Pay Utility Bills")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("Enter Choice: ")
        if choice == "1":
            view_balance_member(acc)
        elif choice == "2":
            print("Call deposit money member function") # call a function here
        elif choice == "3":
            print("Call withraw money member function") # call a function here
        elif choice == "4":
            print=("Call pay utility bills method here") # call a function here 
        elif choice == "5":
            print=("Call change pin function here")
        elif choice == "6":
            print("Session ended.")
            break
        else:
            print("Invalid Choice")

def main_menu():
    print("\n======WELCOME TO ATM======")
    print("1. Account Holder")
    print("2. General User")
    choice = input("Enter choice: ")
    if choice == "1":
        account_holder_login()
    elif choice == "2":
        print("Call main menu for general user") # function to be called
    else:
        print("Invalid Option")

#=========== Program Start ==============
main_menu()