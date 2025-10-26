from collections import defaultdict
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.num_account = len(balance)

    def is_valid_account(self, account: int) -> bool:
        return 1 <= account <= self.num_account

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.is_valid_account(account1) and self.is_valid_account(account2):
            if self.balance[account1-1] >= money:
                self.balance[account1-1] -= money
                self.balance[account2-1] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.is_valid_account(account):
            self.balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.is_valid_account(account):
            if self.balance[account-1] >= money:
                self.balance[account-1] -= money
                return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)


bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10)) # return true
print(bank.transfer(5, 1, 20)) # return true
print(bank.deposit(5, 20)) #return true
print(bank.transfer(3, 4, 15)) #false
print(bank.withdraw(10, 50))