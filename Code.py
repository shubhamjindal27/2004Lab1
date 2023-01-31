#!/usr/bin/env python
# coding: utf-8

# In[ ]:


accounts = dict()
retryLimit = 6

def displayOptions():
    print("Select an option from below - ")
    print("1. Create Account")
    print("2. Deposit Account")
    print("3. Withdraw Account")
    print("4. Transfer Money")
    print("5. Account Balance")
    print("6. Quit")

def createAccount():
    i = 0
    while True:
        i += 1
        if i == retryLimit: 
            print("You have reached maximum retry limit")
            input("Press Enter to continue...")
            break
        accountNumber = input("Enter new account number: ")
        if accountNumber.isdigit():
            if accountNumber in accounts:
                print("Account Number already exists, please retry")
            else:
                accounts[accountNumber] = 0.00
                print("Account has been successfully created")
                input("Press Enter to continue...")
                break
        else:
            print("Account Number has to be numeric only, please retry")

def depositAccount():
    i = 0
    while True:
        i += 1
        if i == retryLimit: 
            print("You have reached maximum retry limit")
            input("Press Enter to continue...")
            break
        account = input("Enter account number: ")
        if account.isdigit():
            if account in accounts:
                while True:
                    try:
                        amount = float(input("Enter amount: "))
                    except:
                        print("Amount has to be digits only, please retry")
                    else:
                        break
                if amount == 0.0:
                    print("Amount entered cannot be 0")
                    input("Press Enter to continue...")
                    break
                elif amount < 0.0:
                    print("Amount entered cannot be negative")
                    input("Press Enter to continue...")
                    break
                accounts[account] += amount
                print("Amount has been successfully deposited. New account balance is:", accounts[account])
                input("Press Enter to continue...")
                break
            else:
                print("Account number does not exist, please retry")
        else:
            print("Account number has to be numeric, please retry")
    
def withdrawAccount():
    i = 0
    while True:
        i += 1
        if i == retryLimit: 
            print("You have reached maximum retry limit")
            input("Press Enter to continue...")
            break
        account = input("Enter account number: ")
        if account.isdigit():
            if account in accounts:
                while True:
                    try:
                        amount = float(input("Enter amount: "))
                    except:
                        print("Amount has to be digits only, please retry")
                    else:
                        break
                if amount == 0.0:
                    print("Amount entered cannot be 0")
                    input("Press Enter to continue...")
                elif amount < 0.0:
                    print("Amount entered cannot be negative")
                    input("Press Enter to continue...")
                elif accounts[account] < amount:
                    print("There isn't sufficient balanace to withdraw. Account Balance is", accounts[account])
                    input("Press Enter to continue...")
                else:
                    accounts[account] -= amount
                    print("Amount has been successfully withdrawn. New account balance is:",accounts[account])
                    input("Press Enter to continue...")
                break
            else:
                print("Account number does not exist, please retry")
        else:
            print("Account number has to be numeric, please retry")
    
def transferMoney():
    i = 0
    while True:
        i += 1
        if i == retryLimit: 
            print("You have reached maximum retry limit")
            input("Press Enter to continue...")
            return
        senderAccount = input("Enter sender's account number: ")
        if senderAccount.isdigit():
            if senderAccount in accounts:
                break
            else:
                print("Account number does not exist, please retry")
        else:
            print("Account number has to be numeric, please retry")
    i = 0
    while True:
        i += 1
        if i == retryLimit: 
            print("You have reached maximum retry limit")
            input("Press Enter to continue...")
            return
        receiverAccount = input("Enter receiver's account number: ")
        if receiverAccount.isdigit():
            if receiverAccount in accounts:
                if senderAccount == receiverAccount:
                    print("Sender account and Receiver account number cannot be same, please retry")
                else:
                    break
            else:
                print("Account number does not exist, please retry")
        else:
            print("Account number has to be numeric, please retry")
    i = 0
    while True:
        i += 1
        if i == retryLimit: 
            print("You have reached maximum retry limit")
            input("Press Enter to continue...")
            return
        try:
            amount = float(input("Enter amount to be transferred: "))
        except:
            print("Amount has to be digits only, please retry")
        else:
            if amount == 0.0:
                print("Amount to be transferred cannot be 0, please retry")
            elif amount < 0.0:
                print("Amount to be transferred cannot be negative, please retry")
            elif accounts[senderAccount] < amount:
                print("There isn't sufficient balanace to transfer. Account Balance is", accounts[senderAccount])
                input("Press Enter to continue...")
                break
            else:
                accounts[senderAccount] -= amount
                accounts[receiverAccount] += amount
                print("Amount has been successfully transferred. New account balance is:",accounts[senderAccount])
                input("Press Enter to continue...")
                break

def accountBalance():
    i = 0
    while True:
        i += 1
        if i == retryLimit: 
            print("You have reached maximum retry limit")
            input("Press Enter to continue...")
            break
        account = input("Enter account number: ")
        if account.isdigit():
            if account in accounts:
                print("Account balance is:", accounts[account])
                input("Press Enter to continue...")
                break
            else:
                print("Account number does not exist, please retry")
        else:
            print("Account number has to be numeric, please retry")    

print("Hello, welcome to your banking services!")
choice = '0'
while(choice != '6'):
    displayOptions()
    choice = input("Enter your choice: ")
    if choice == '1':
        createAccount()
    elif choice == '2':
        depositAccount()
    elif choice == '3':
        withdrawAccount()
    elif choice == '4':
        transferMoney()
    elif choice == '5':
        accountBalance()
    elif choice == '6':
        print("Thanks for visiting, have a great day!")
    else:
        print("Entered option is not correct! Retry")

