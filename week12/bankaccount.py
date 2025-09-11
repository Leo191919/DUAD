class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount 
            print (f'Deposited ${amount}. New balance: ${self.balance}')
        else: 
            print ("Deposit amount must be greater than zero.")


    def withdraw(self, amount):
        if amount >0:
            if self.balance >= amount:
                self.balance -=amount 
                print (f'Withdrew ${amount}. New balance: ${self.balance}')
            else :
                print('Insufficient funds.')
        else:
            print ('Withdrawal amount must be greater than zero.')


class SavingAccount(BankAccount):
    def __init__(self,balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance


    def withdraw(self, amount):
        if amount> 0 :
            if self.balance - amount >=self.min_balance:
                self.balance -= amount
                print(f'Withdrew ${amount}. New balance: ${self.balance}')
            else:
                raise ValueError(f'Withdrawal not allowed. Balance cannot go below the minimum balance of ${self.min_balance}.')
        else:
            print('Withdrawal amount must be greater than zero.')


if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(200)

    savings_account = SavingAccount(200,50)
    savings_account.deposit(100)
    savings_account.withdraw(100)
    try:
        savings_account.withdraw(180)
    except ValueError as e:
        print(f'Error attempting withdrawal:{e}')
    savings_account.withdraw(50)
    try:
        savings_account.withdraw(1)
    except ValueError as e:
        print(f'Error attempting withdrawal:{e}')

        