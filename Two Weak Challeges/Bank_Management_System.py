print("========= BANK MANAGEMENT SYSTEM =========")
account=[]

def create_account():
    CNIC = input("Enter your CNIC number: ")
    for accounts in account:
        if accounts['cnic'] == CNIC:
            print("Account already Created for this CNIC")
            return
    account_no = input("Enter your account_number")
    name = input("Enter your Name: ")
    phone = input("Enter your Phone number")
    balance = int(input("Enter Initial Balance: "))

    create_account_data = {
        "cnic" : CNIC,
        "Account_no" : account_no,
        "name"  : name,
        "Phone" : phone,
        "balance" : balance
    }
    account.append(create_account_data)
    print("Created account sccessfully")


def view_accounts():
    if len(account) == 0:
        print("No Account Created")
        return
    for accounts in account:
        print(f"CNIC : {accounts['cnic']}")
        print(f"Account_no : {accounts['Account_no']}")
        print(f"name : {accounts['name']}")
        print(f"Phone : {accounts['Phone']}")
        print(f"balance : {accounts['balance']}")
        print("-" * 50)


def search_account():
    if len(account) == 0:
        print("No Account Created")
        return
    CNIC = input("Enter the CNIC number: ")
    for accounts in account:
        if accounts['cnic'] == CNIC:
            print(f"CNIC : {accounts['cnic']}")
            print(f"Account_no : {accounts['Account_no']}")
            print(f"name : {accounts['name']}")
            print(f"Phone : {accounts['Phone']}")
            print(f"balance : {accounts['balance']}")
            print("-" * 50)
            return
def deposit():
    if len(account) == 0:
        print("No Account Created")
        return
    account_number = input("Enter your account number: ")
    for accounts in account:
        if accounts['Account_no'] == account_number:
            amount = int(input("Enter the amount for deposit: "))
            if amount <=0:
                print("Amount must be greater than 0")
            else:
                accounts['balance'] += amount
                print("Deposit successful.")
                print(f"Updated balance {accounts['balance']}")    


def withdraw():
    if len(account) == 0:
        print("No Account Created")
        return
    account_number = input("Enter your account number: ")
    for accounts in account:
        if accounts['Account_no'] == account_number:
            amount = int(input("Enter the amount for Withdraw: "))
            if amount <=0:
                print("Amount must be greater than 0")
            elif amount > accounts["balance"]:
                print("Insufficient balance")
            else:
                accounts['balance'] -= amount
                print("Withdrawl Successful.")
                print(f"Updated balance {accounts['balance']}")    
    


create_account()
view_accounts()
search_account()
deposit()
view_accounts()
withdraw()
view_accounts()

def transfer():
    pass

def update_account():
    pass

def delete_account():
    pass

def check_balance():
    pass








# while True:
    print("""
========= BANK MANAGEMENT SYSTEM =========

1. Create Account
2. View All Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Transfer Money
7. Update Account
8. Delete Account
9. Check Balance
10. Exit

==========================================
""")