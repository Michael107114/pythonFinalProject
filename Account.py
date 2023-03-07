import random

class Account:

    accountNumber = 0
    first = ''
    last = ''
    balance = 0
    # add methods as getters and setters for attributes
    def __init__(self, first, last):
        self.accountNumber = random.randint(10000000, 99999999)
        self.ssn = str(100000000)
        self.pin = str(random.randint(1000,9999))
        self.first = first
        self.last = last
        self.balance = 0

    def createAccount(self):
        self.first = input("Enter Account Owner's First name: \n")
        self.last = input("Enter Account Owner's Last name: \n")
        self.ssn = str(input("Enter Account Owner's SSN (9 digits): \n"))
        self.pin = str(random.randint(1000, 9999))
        self.balance = 0

    # TODO add the reset of the setters
    def setBalance(self, balance):
        self.balance = balance

    def setPin (self, pin):
        self.pin = str(random.randint(1000, 9999))

    def setFirst(self, first):
        self.first = first

    def setLast(self, last):
        self.last = last

    # TODO create the reset of the getters
    def getfirst(self):
        return self.first

    def getlast(self):
        return self.last

    def getBalance(self):
        return self.balance

    def getAccountNumber(self):
        return self.accountNumber

    def getAccountInfo(self):
        return

    def getPin(self):
        return self.pin

    def deposit(self, amount):

        # implement deposit here
        
        self.balance += amount
        return self.balance


    def withdraw(self, amount):
        
        #need help creating code to check balance first
        self.balance -= amount
        return self.balance
    
    def isValidPIN(self, pin):
        
        # implement isValidPIN here
        
        return self.pin == pin  # be sure to change this


    # all objects have a toString method - this indicates you are providing
    # your own version
    def __repr__(self):
        return (f"Account Number: {self.accountNumber}\n"
                f"Owner First Name: {self.first}\n"
                f"Owner Last Name: {self.last}\n"
                f"Owner SSN: {self.ssn}\n"
                f"PIN: {self.pin}\n"
                f"Balance: {self.balance}\n")

