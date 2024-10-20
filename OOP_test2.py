class BankAccount(object):

    def __init__(self, account_number, balance=0):

        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):

        if (self.balance - amount) >= 0:

            self.balance -= amount
            print(f"Current Balance:{self.balance}")
        
        else:
            print("Insufficient Balance, operation not permmited")
    
    def deposit(self, amount):

        self.balance += amount
        print(f"Current Balance:{self.balance}")

acc_1 = BankAccount(1,12)
acc_1.withdraw(13)
acc_1.deposit(28)

acc_2 = BankAccount(1,32)
acc_2.deposit(23)
acc_2.withdraw(6)