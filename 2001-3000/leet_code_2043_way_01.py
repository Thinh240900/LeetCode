from collections import defaultdict
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = defaultdict(lambda: -1)
        for i in range(len(balance)):
            self.accounts[i+1] = balance[i]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.accounts[account1] == -1 or self.accounts[account2] == -1 or self.accounts[account1] < money:
            return False
        self.accounts[account1] -= money
        self.accounts[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if self.accounts[account] == -1:
            return False
        self.accounts[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if self.accounts[account] == -1 or self.accounts[account] < money:
            return False
        self.accounts[account] -= money
        return True

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