import random
from Account import Account
from CoinCollector import CoinCollector
from BankUtility import BankUtility
from Bank import Bank


class BankManager:
    def __init__(self):
        pass
    # This is where you will implement your ‘main’ method and start
    # the program from.  The BankManager class should create an instance
    # of a Bank object when the program runs and use that instance to
    # manage the Accounts in the bank

    while action != 11:

        print("""
        1. Open an account
        2. Get account information and balance
        3. Change PIN
        4. Deposit money in account
        5. Transfer money between accounts
        6. Withdraw money from account
        7. ATM withdrawal
        8. Deposit change
        9. Close an account
        10. Add monthly interest to all accounts
        11. End Program
        """)
        action = str(input('What do you want to do? Enter your number here: '))
        account = Account()

        if action == '1':
            action.createAccount()

        elif action == '2':
            pass

        elif action == '3':
            pass

        elif action == '4':
            pass

        elif action == '5':
            pass

        elif action == '6':
            pass

        elif action == '7':
            pass

        elif action == '8':
            pass

        elif action == '9':
            pass

        elif action == '10':
            pass

        elif action == '11':
            print('Thank you for chosing using The Daffy Duck Banking System!')
            break



    # @staticmethod
    # promptForAccountNumberAndPIN(bank):

    # implement promptForAccountNumberAndPIN here
    # takes one parameter, a Bank object that represents the bank.
    # The method should prompt the user to enter an account number
    # and then try to find a matching account with that account number
    # in the bank.

    # return # be sure to change this as needed
