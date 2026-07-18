account=[]

def create_account():
    print("\n🏦 ----- Create Account -----")
    account_no = input("🆔 Enter Account Number:")
    cnic = input("🪪 Enter CNIC:")
    for accounts in account:
        if accounts['Account_no'] == account_no:
            print("⚠️ Account Number already exists.")
            return
        if accounts["cnic"] == cnic:
            print("⚠️ CNIC already exists.")
            return
    
    name = input("👤 Enter Name:")
    phone = input("📞 Enter Phone Number:")
    balance = float(input("💰 Enter Initial Balance:"))

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
    print("\n📋 ----- Account Details -----")
    if len(account) == 0:
        print("📂 No Account Created.")
        return
    for accounts in account:
        print("-" * 40)
        print(f"🆔 Account Number :  {accounts['Account_no']}")
        print(f"🪪 CNIC           :  {accounts['cnic']}")
        print(f"👤 Name           :  {accounts['name']}")
        print(f"📞 Phone          :  {accounts['Phone']}")
        print(f"💰 Balance        :  {accounts['balance']}")
        print("-" * 40)


def search_account():
    print("\n🔍 ----- Search Account -----")
    if len(account) == 0:
        print("📂 No Account Created.")
        return
    cnic = input("🔍 Enter the CNIC number: ")
    for accounts in account:
        if accounts['cnic'] == cnic:
            print(f"🆔 Account Number  :     {accounts['Account_no']}")
            print(f"🪪 CNIC            :     {accounts['cnic']}")
            print(f"👤 Name            :     {accounts['name']}")
            print(f"📞 Phone           :     {accounts['Phone']}")
            print(f"💰 Balance          :     {accounts['balance']}")
            return
    print("❌ Account not found.")
            
def deposit():
    print("\n💵 ----- Deposit Money -----")
    if len(account) == 0:
        print("📂 No Account Created.")
        return
    account_no = input("🆔 Enter your account number: ")
    for accounts in account:
        if accounts['Account_no'] == account_no:
            amount = int(input("Enter the amount for deposit: "))
            if amount <=0:
                print("❌ Invalid Amount.")
                return
    
            accounts['balance'] += amount
            print("✅ Deposit Successful!")
            print(f"💰 Deposited Amount : {amount}")
            print(f"🏦 Current Balance  : {accounts['balance']}")
            return
    print("❌ Account not found.")    


def withdraw():
    print("\n💸 ----- Withdraw Money -----")
    if len(account) == 0:
        print("📂 No Account Created.")
        return
    account_no = input("Enter your account number: ")
    for accounts in account:
        if accounts['Account_no'] == account_no:
            amount = int(input("💸 Enter withdrawal amount: "))
            if amount <=0:
                print("❌ Invalid Amount.")
                return
            if amount > accounts["balance"]:
                print("❌ Insufficient Balance.")
                return
            
            accounts['balance'] -= amount
            print("✅ Withdrawal Successful!")
            print(f"💸 Withdrawn : {amount}")
            print(f"🏦 Remaining Balance : {accounts['balance']}")
            return

    print("❌ Account not found.")

def transfer():
    print("\n🔄 ----- Transfer Money -----")
    if len(account) == 0:
        print("📂 No Account Created.")
        return
    sender_account = input("🆔 Enter sender account number: ")
    receiver_account = input("🆔 Enter receiver account number: ")
    if sender_account == receiver_account:
        print("⚠️ Sender and Receiver accounts cannot be the same.")
        return
    transfer_amount = int(input("💸 Enter transfer amount: "))
    if transfer_amount <= 0:
        print("❌ Invalid Amount.")
        return

    sender = None
    receiver = None
    for accounts in account:
        if accounts["Account_no"] == sender_account:
            sender = accounts
        if accounts["Account_no"] == receiver_account:
            receiver = accounts
    if sender is None:
        print("❌ Sender account not found.")
        return
        
    if receiver is None:
        print("❌ Receiver account not found.")
        return
        

    if sender["balance"] < transfer_amount:
        print("❌ Insufficient Balance.")
        return
    sender["balance"] -= transfer_amount
    receiver["balance"] += transfer_amount

    print("✅ Transfer Successful!")
    print(f"💸 {transfer_amount} transferred successfully.")
    print(f"👤 Sender Balance   : {sender['balance']}")
    print(f"👤 Receiver Balance : {receiver['balance']}")


def update_account():
    print("\n✏️ ----- Update Account -----")
    if len(account) == 0:
        print("📂 No Account Created.")
        return
    account_no = input("🆔 Enter account number: ")
    name = input("Enter your new Name: ")
    phone = input("Enter your new Phone number")
    for accounts in account:
        if accounts["Account_no"] == account_no:
            accounts['name'] = name
            accounts['Phone'] = phone
            print("✅ Account Updated Successfully!")
            return
    print("❌ Account not found.")
    


def delete_account():
    print("\n🗑️ ----- Delete Account -----")
    if len(account) == 0:
        print("📂 No Account Created.")
        return
    account_no  = input("Enter Account number to Delete: ")
    for accounts in account:
        if accounts['Account_no'] == account_no:
            account.remove(accounts)
            print("✅🗑️ Account Deleted Successfully!")
            return
    print("❌ Account not found.")


def check_balance():
    print("\n💳 ----- Check Balance -----")
    if len(account) == 0:
        print("📂 No Account Created.")
        return
    account_no  = input("Enter Account number to Check Balance: ")
    for accounts in account:
        if accounts['Account_no'] == account_no:
            
            print("="*40)
            print(f"👤 Account Holder : {accounts['name']}")
            print(f"🆔 Account Number : {accounts['Account_no']}")
            print(f"💰 Current Balance: {accounts['balance']}")
            print("="*40)
            return
    print("❌ Account not found.")
    

while True:
    print("""
🏦========================================🏦
        BANK MANAGEMENT SYSTEM
🏦========================================🏦

1️⃣  Create Account
2️⃣  View Accounts
3️⃣  Search Account
4️⃣  Deposit Money
5️⃣  Withdraw Money
6️⃣  Transfer Money
7️⃣  Update Account
8️⃣  Delete Account
9️⃣  Check Balance
🔟 Exit

🏦========================================🏦
""")

    choice = input("👉 Enter your choice: ")

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
        print("""==================================================
            🙏 Thank you for using Bank Management System.
            💙 Developed by Abdul Haseeb
            🚀 Keep Learning | Keep Coding
            🐍 Python Console Project
            ==================================================""")
        break

    else:
        print("❌ Invalid Choice! Please try again.")