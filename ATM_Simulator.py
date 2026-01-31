# This list stores default bank account records that can be accessed
#  and modified by account holders during ATM operations.
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
"""
    This function allows the account holder to pay different utility bills
    such as electricity, gas, water, internet, and mobile bills by deducting
    the bill amount from the current account balance and updating it.
"""
def pay_utility_bills(balance):
    global transaction_history
    while True:
        # Display utility bill menu
        print("\n===================================")
        print("          PAY UTILITY BILLS         ")
        print("===================================\n")
        print("1.  Electricity Bill")
        print("2.  Gas Bill")
        print("3.  Water Bill")
        print("4.  Internet/Wifi Bill")
        print("5.  Telephone/Mobile Bill")
        print("6.  Back to Main Menu")
         # Take user choice
        choice = input("\nEnter your choice: ")
        if choice in ["1", "2", "3", "4", "5"]:
            while True:
                # Ask for bill amount
                amount = input("\nEnter bill amount: ")
                # Validate numeric input
                if amount.isdigit():
                    amount = int(amount)
                    # Check if sufficient balance exists
                    if amount <= balance:
                        balance -= amount # Check if sufficient balance exists
                        print("\nBill paid successfully")
                        print("Remaining Balance:", balance)
                        # Map bill type with choice
                        bill_types = {
                            "1": "Electricity",
                            "2": "Gas",
                            "3": "Water",
                            "4": "Internet/Wifi",
                            "5": "Telephone/Mobile"
                        }
                        # Store transaction in history
                        current_bill = bill_types[choice]
                        transaction_history.append("Paid " + str(current_bill) + " bill: Rs " + str(amount))
                        break
                    else:
                        print("Balance is insufficient. Try again.")
                else:
                    print("Invalid bill amount. Try again.")
            break  # exit main choice loop after successful bill payment
        elif choice == "6":
            # Return to main menu
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Try again.")
    return balance

"""
    This function allows the account holder to securely change their ATM PIN
    after verifying the old PIN and confirming the new PIN.
"""
def change_Pin(current_Pin):
    global transaction_history
    print("\n== Change PIN ==")
    # Verify old PIN
    old_pin = input("Enter old PIN: ")
    if old_pin != current_Pin:
        print("Incorrect PIN")
        return current_Pin
    while True:
    # Take new PIN input
        new_pin = input("Enter new PIN: ")
        if not new_pin.isdigit() : #validating the composition of new pin 
            print("Invalid PIN. PIN must contain only digits.")
            continue
        if len(new_pin) != 4: #validating the length of new pin
            print("Invalid PIN. PIN must contain only 4 digits.")
            continue
        confirm_pin = input("Re-enter new PIN: ")
        # Confirm both PIN entries match
        if new_pin != confirm_pin:
            print("PINs do not match...Try Again")
            continue

        break
    print("PIN changed successfully!")
    # Store PIN change operation
    transaction_history.append("PIN changed successfully")

    return new_pin

"""
    This function searches for an account in the system using the provided
    account number and returns the account details if found.
"""
def find_account(account_no):
    # Loop through all stored accounts
    for acc in accounts:
        if acc["account_no"] == account_no:
            return acc # Account found
    return None # Account not found

"""
    This function handles account holder login by verifying the account number
    and PIN, while limiting the number of incorrect login attempts.
"""
def account_holder_login():

    while True:
        acc_no = input("\nEnter account number (or 0 to exit): ")
        #if 0 then exit
        if acc_no == "0":
            print("Returning to main menu...")
            return

        #search for account
        acc = find_account(acc_no)

        if acc is None:
            print("Account not found. Please try again.")
            continue   # ask again instead of going to main menu

        global transaction_history
        transaction_history = []   # reset for each session
        attempts = 3 #Maximum pin attempts allowed

        while attempts > 0:
            pin = input("Enter pin: ")

            if not pin.isdigit():
                print("Invalid PIN. PIN must contain only digits.")
                continue

            if pin == acc["pin"]:
                print("\nWelcome", acc["name"])
                member_menu(acc)
                return
            else:
                attempts = attempts - 1
                print("Incorrect Pin! Attempts left:", attempts)

        print("Too many failed attempts. Account Locked!")
        return

"""
    This function displays the current balance of the logged-in account holder
    and records the balance inquiry in the transaction history.
"""
def view_balance_member(acc):
    global transaction_history
    print("\n======Displaying Balance======")
    print("Account Holder: ",acc["name"])
    print("Balance :",acc["balance"])
    # Log balance inquiry
    transaction_history.append("Viewed balance: Rs " + str(acc["balance"]))

"""
    This function allows the account holder to deposit a valid amount of money
    into their account and updates the balance accordingly.
"""
def deposit_money_member(acc):
    global transaction_history
    while True:
        # Ask for deposit amount
        amount = input("\nEnter amount to deposit: ")
        # Validate numeric input
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                acc["balance"] += amount # Add amount to balance
                print("Deposit Successful")
                print("New balance: ", acc["balance"])
                # Log deposit transaction
                transaction_history.append("Deposited Rs " + str(amount))
                break
            else:
                print("Amount must be positive. Try again.")
        else:
            print("Invalid Amount. Try again.")

"""
    This function allows the account holder to withdraw money from their account
    after checking that sufficient balance is available.
"""
def withdraw_money_member(acc):
    global transaction_history
    while True:
        # Ask for withdrawal amount
        amount = input("\nEnter amount to withdraw: ")
        if amount.isdigit():
            # Validate numeric input
            amount = int(amount)
            # Check available balance
            if amount <= acc["balance"]:
                acc["balance"] -= amount # Deduct amount
                print("Withdraw Successful!")
                print("New Balance :", acc["balance"])
                # Log withdrawal
                transaction_history.append("Withdrew Rs " + str(amount))
                break
            else:
                print("Insufficient Balance. Try again.")
        else:
            print("Invalid Amount. Try again.")

"""
    This function generates and displays a receipt showing the account holder’s
    starting balance, closing balance, and complete transaction history.
"""
def generate_receipt_member(acc):
    print("\n===================================")
    print("              RECEIPT               ")
    print("===================================\n")
    print(acc["name"])
    print("Starting Balance = ", acc["initial_balance"])
    print("Closing Balance = ", acc["balance"])
    print("\n-----------------------------------")
    print("         TRANSACTION HISTORY        ")
    print("-----------------------------------")
    # Display all transactions
    if not transaction_history:
        print("No actions performed.")
    else:
        for t in transaction_history:
            print("-", t)

"""
    This function displays the ATM menu for the logged-in account holder and
    allows them to perform different banking operations.
"""
def member_menu(acc):
    while True:
        # displaying menu
        print("\n===================================")
        print("              ATM MENU")
        print("===================================\n")
        print("1.  View Balance")
        print("2.  Deposit Money")
        print("3.  Withdraw Money")
        print("4.  Pay Utility Bills")
        print("5.  Change PIN")
        print("6.  Exit to main")
        choice = input("Enter Choice: ") # taking user's choice
        if choice == "1":
            view_balance_member(acc) # call to function
        elif choice == "2":
            deposit_money_member(acc) # call to function
        elif choice == "3":
            withdraw_money_member(acc) # call to function
        elif choice == "4":
            acc["balance"] = pay_utility_bills(acc["balance"]) # call to function
        elif choice == "5":
            acc["pin"] = change_Pin(acc["pin"]) # call to function
        elif choice == "6":
            generate_receipt_member(acc) # call to function
            print("Session ended.")
            break
        else:
            print("Invalid Choice")
            member_menu(acc)

"""
    This function displays the main ATM welcome menu and controls the overall
    flow of the ATM program until the user chooses to exit.
"""
def main_menu():
    while True:
        print("\n===========================")
        print("====== WELCOME TO ATM =====")
        print("===========================\n")
        print("1.  Perform an Operation")
        print("2.  Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            account_holder_login() # calls the function to login the member
        elif choice == "2":
            print("Exiting program.")
            exit()   # terminates the program
        else:
            print("Invalid choice. Try again.")
#=========== Program Start ==============
main_menu() #call to the main_menu() function
