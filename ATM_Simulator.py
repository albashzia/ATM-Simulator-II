#Default accounts holding data which can be manipulated and accessed by account holders
accounts = [
    {"name": "Ahmed",  "account_no": "49217385", "pin": "1234", "balance": 12000, "initial_balance": 12000},
    {"name": "Fatima", "account_no": "83726149", "pin": "6789", "balance": 18000, "initial_balance": 18000},
    {"name": "Sara",   "account_no": "59102836", "pin": "1111", "balance": 25000, "initial_balance": 25000},
    {"name": "Bilal",  "account_no": "74839215", "pin": "2222", "balance": 5000,  "initial_balance": 5000},
    {"name": "Ayesha", "account_no": "36581942", "pin": "3333", "balance": 15000, "initial_balance": 15000},
    {"name": "Ali",    "account_no": "91427638", "pin": "4444", "balance": 20000, "initial_balance": 20000},
    {"name": "Hassan", "account_no": "28637491", "pin": "5555", "balance": 3000,  "initial_balance": 3000},
    {"name": "Fatima", "account_no": "67358214", "pin": "6666", "balance": 40000, "initial_balance": 40000},
    {"name": "Zain",   "account_no": "15983726", "pin": "7777", "balance": 8000,  "initial_balance": 8000},
    {"name": "Maria",  "account_no": "42819573", "pin": "8888", "balance": 22000, "initial_balance": 22000}
]

#function that works for both general users and account holders
def Pay_UtilityBills(balance):
    global transaction_history
    while True:
        print("\n----- PAY UTILITY BILLS -----")
        print("1. Electricity Bill")
        print("2. Gas Bill")
        print("3. Water Bill")
        print("4. Internet/Wifi Bill")
        print("5. Telephone/Mobile Bill")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice in ["1", "2", "3", "4", "5"]:
            while True:
                amount = input("Enter bill amount: ")
                if amount.isdigit():
                    amount = int(amount)
                    if amount <= balance:
                        balance -= amount
                        print("Bill paid successfully")
                        print("Remaining Balance:", balance)
                        bill_types = {
                            "1": "Electricity",
                            "2": "Gas",
                            "3": "Water",
                            "4": "Internet/Wifi",
                            "5": "Telephone/Mobile"
                        }
                        current_bill = bill_types[choice]
                        transaction_history.append("Paid " + str(current_bill) + " bill: Rs " + str(amount))
                        break
                    else:
                        print("Balance is insufficient. Try again.")
                else:
                    print("Invalid bill amount. Try again.")
            break  # exit main choice loop after successful bill payment
        elif choice == "6":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Try again.")
    return balance


#function to change pin
def change_Pin(current_Pin):
    global transaction_history
    print("\n== Change PIN ==")
    old_pin = input("Enter old PIN: ")
    if old_pin != current_Pin:
        print("Incorrect PIN")
        return current_Pin
    new_pin = input("Enter new PIN: ")
    confirm_pin = input("Re-enter new PIN: ")
    if new_pin != confirm_pin:
        print("PINs do not match")
        return current_Pin
    print("PIN changed successfully!")
    transaction_history.append("PIN changed successfully")

    return new_pin

#function to check if an account exists for the account number entered by the user
def find_account(account_no):
    for acc in accounts:
        if acc["account_no"] == account_no:
            return acc
    return None

#function to login to accounts by accepting pins and allowing only 3 attempts 
def account_holder_login():
    acc_no = input("Enter account number: ")
    acc = find_account(acc_no)
    if acc is None:
        print("Account not found")
        main_menu()
        return
    global transaction_history
    transaction_history = []   # reset for each session

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
    global transaction_history
    print("Account Holder: ",acc["name"])
    print("Balance :",acc["balance"])
    transaction_history.append("Viewed balance: Rs " + str(acc["balance"]))

def deposit_money_member(acc):
    global transaction_history
    while True:
        amount = input("Enter amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                acc["balance"] += amount
                print("Deposit Successful")
                print("New balance: ", acc["balance"])
                transaction_history.append("Deposited Rs " + str(amount))
                break
            else:
                print("Amount must be positive. Try again.")
        else:
            print("Invalid Amount. Try again.")


def withdraw_money_member(acc):
    global transaction_history
    while True:
        amount = input("Enter amount to withdraw: ")
        if amount.isdigit():
            amount = int(amount)
            if amount <= acc["balance"]:
                acc["balance"] -= amount
                print("Withdraw Successful!")
                print("New Balance :", acc["balance"])
                transaction_history.append("Withdrew Rs " + str(amount))
                break
            else:
                print("Insufficient Balance. Try again.")
        else:
            print("Invalid Amount. Try again.")


#function to generate receipt upon completion of actions by the user
def generate_receipt_member(acc): 
    print("\n====== RECEIPT =======")
    print(acc["name"])           
    print("Starting Balance = ", acc["initial_balance"]) 
    print("Closing Balance = ", acc["balance"])
    print("\n--- Transaction History ---")
    if not transaction_history:
        print("No actions performed.")
    else:
        for t in transaction_history:
            print("-", t)

def member_menu(acc):
    while True:
        print("\n--- ATM Menu (Account Holder) ---")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Pay Utility Bills")
        print("5. Change PIN")
        print("6. Exit")
        print("7. Return to Main Menu")
        choice = input("Enter Choice: ")
        if choice == "1":
            view_balance_member(acc)
        elif choice == "2":
            deposit_money_member(acc)
        elif choice == "3":
            withdraw_money_member(acc)
        elif choice == "4":
            acc["balance"] = Pay_UtilityBills(acc["balance"])
        elif choice == "5":
            acc["pin"] = change_Pin(acc["pin"])
        elif choice == "6":
            generate_receipt_member(acc)
            print("Session ended.")
            break
        elif choice == "7":
            main_menu()
            break
        else:
            print("Invalid Choice")
            member_menu(acc)

def main_menu():
    while True:
        print("\n===========================")
        print("====== WELCOME TO ATM =====")
        print("===========================\n")
        print("1. Perform an Operation")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            account_holder_login()
        elif choice == "2":
            print("Exiting program... Goodbye!")
            exit()   # terminates the program
        else:
            print("Invalid choice. Try again.")


#=========== Program Start ==============
main_menu()