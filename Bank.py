
class Bank:
    MAX_ACCOUNTS = 10

    def __init__(self):
        self.accounts = []

    def addAccountToBank(self, account):
        # implement addAccountToBank here
        for i in range(len(self.accounts)):
            acc = self.accounts[i]
            if acc is None:
                self.accounts[i] = account
                return True

        if len(self.accounts) < Bank.MAX_ACCOUNTs:
            self.accounts.append(account)
            return True

        print('No more accounts available')
        return False # be sure to change this as needed

    def removeAccountFromBank(self, account):

        # implement removeAccountFromBank here
        for i in range(len(self.account)):
            acc =self.accounts[i]
            if account.getAccountNumber() == acc.getAccountNumber():
                self.accounts[i] = None
                return False

        return False # be sure to change this as needed


    def findAccount(self, accountNumber):
        for i in range(len(self.account)):
            acc = self.accounts[i]
            if accountNumber() == acc.getAccountNumber():

                return acc

        return None


    def addMonthlyInterest(self,percent):
        for account in self.accounts:
            if account is not None:
                interest = account.getBalance() * percent / 100 / 12
                account.deposit(interest)
        # EXTRA CREDIT
