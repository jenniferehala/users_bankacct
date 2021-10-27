class BankAccount:
    def __init__(self, int_rate = 0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        # print(self.balance)
        return self
    def withdraw(self,amount):
        self.balance -= amount
        # print(self.balance)
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance*self.int_rate + self.balance
            # print(self.balance)
            return self

        else:
            print("Insufficient Funds")


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account += amount
        return self
    def make_withdrawal(self,amount):
        self.account -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account}")
        return self