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