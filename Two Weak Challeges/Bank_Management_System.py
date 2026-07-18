account=[]

def create_account():
    print("\n🏦 ----- Create Account -----")
    account_no = input("🆔 Enter Account Number:")
    cnic = input("🪪 Enter CNIC:")
    for accounts in account:
        if accounts['Account_no'] == account_no:
            print("Account Number already exists.")
            return
        if accounts["cnic"] == cnic:
            print("CNIC already exists.")
            return
    
    name = input("👤 Enter Name:")
    phone = input("📞 Enter Phone Number:")
    balance = int(input("💰 Enter Initial Balance:"))

    new_account = {
        "Account_no" : account_no,
        "cnic" : cnic,
        "name"  : name,
        "Phone" : phone,
        "balance" : balance
    }
    account.append(new_account)
    print("✅ Account created successfully.")


def view_accounts():
    if len(account) == 0:
        print("No Account Created")
        return
    for accounts in account:
        print("-" * 40)
        print(f"Account Number : {accounts['Account_no']}")
        print(f"CNIC           : {accounts['cnic']}")
        print(f"Name           : {accounts['name']}")
        print(f"Phone          : {accounts['Phone']}")
        print(f"Balance        : {accounts['balance']}")
        print("-" * 40)


def search_account():
    if len(account) == 0:
        print("No Account Created")
        return
    cnic = input("Enter the CNIC number: ")
    for accounts in account:
        if accounts['cnic'] == cnic:
            print(f"Account Number : {accounts['Account_no']}")
            print(f"CNIC           : {accounts['cnic']}")
            print(f"Name           : {accounts['name']}")
            print(f"Phone          : {accounts['Phone']}")
            print(f"Balance        : {accounts['balance']}")
            return
    print("Account not found.")
            
def deposit():
    if len(account) == 0:
        print("No Account Created")
        return
    account_no = input("Enter your account number: ")
    for accounts in account:
        if accounts['Account_no'] == account_no:
            amount = int(input("Enter the amount for deposit: "))
            if amount <=0:
                print("Invalid Amount")
                return
    
            accounts['balance'] += amount
            print("Deposit successful.")
            print(f"Updated balance {accounts['balance']}")
            return
    print("Account not found.")    


def withdraw():
    if len(account) == 0:
        print("No Account Created")
        return
    account_no = input("Enter your account number: ")
    for accounts in account:
        if accounts['Account_no'] == account_no:
            amount = int(input("Enter the amount for Withdraw: "))
            if amount <=0:
                print("Invalid Amount")
                return
            if amount > accounts["balance"]:
                print("Insufficient balance")
                return
            
            accounts['balance'] -= amount
            print("Withdrawl Successful.")
            print(f"Current balance {accounts['balance']}")    
            return

    print("Account not found.")

def transfer():
    if len(account) == 0:
        print("No Account Created")
        return
    sender_account = input("Enter the transfer account number: ")
    receiver_account = input("Enter the Receive account number: ")
    if sender_account == receiver_account:
        print("Both accounts cannot be the same.")
        return
    transfer_amount = int(input("Enter transfer amount: "))
    if transfer_amount <= 0:
        print("Invalid Amount")
        return

    sender = None
    receiver = None
    for accounts in account:
        if accounts["Account_no"] == sender_account:
            sender = accounts
        if accounts["Account_no"] == receiver_account:
            receiver = accounts
    if sender is None:
        print("Sender account not found.")
        return
        
    if receiver is None:
        print("Receiver account not found.")
        return
        

    if sender["balance"] < transfer_amount:
        print("Insufficient balance.")
        return
    sender["balance"] -= transfer_amount
    receiver["balance"] += transfer_amount

    print("Transfer Successful!")
    print(f"Sender Balance   : {sender['balance']}")
    print(f"Receiver Balance : {receiver['balance']}")


def update_account():
    if len(account) == 0:
        print("No Account Created")
        return
    account_no  = input("Enter Account number : ")
    name = input("Enter your new Name: ")
    phone = input("Enter your new Phone number")
    for accounts in account:
        if accounts["Account_no"] == account_no:
            accounts['name'] = name
            accounts['Phone'] = phone
            print("Account details updated")
            return
    print("❌ Account not found.")
    


def delete_account():
    if len(account) == 0:
        print("No Account Created")
        return
    account_no  = input("Enter Account number to Delete: ")
    for accounts in account:
        if accounts['Account_no'] == account_no:
            account.remove(accounts)
            print("🗑️ Account deleted successfully.")
            return
    print("❌ Account not found.")


def check_balance():
    if len(account) == 0:
        print("No Account Created")
        return
    account_no  = input("Enter Account number to Check Balance: ")
    for accounts in account:
        if accounts['Account_no'] == account_no:
            
            print(f"Account Holder : {accounts['name']}")
            print(f"Current Balance : {accounts['balance']}")
            return
    print("No account Found")
    

while True:
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

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        search_account()

    elif choice == "4":
        deposit()

    elif choice == "5":
        withdraw()

    elif choice == "6":
        transfer()

    elif choice == "7":
        update_account()

    elif choice == "8":
        delete_account()

    elif choice == "9":
        check_balance()

    elif choice == "10":
        print("Thank you for using Bank Management System.")
        break

    else:
        print("Invalid Choice!")