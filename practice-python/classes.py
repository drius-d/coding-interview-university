# %%
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def greet(self):
    print("Hello, my name is " + self.name)

def main():
    p1 = Person("John", 36)
    greet(p1)

if __name__ == "__main__":
    main()

# %%

# Bank account class. Each account should have an owner and balance. Methods include: deposit, withdraw, get_balance.
# Cannot have negative amount of money
# Invalid transactions should print an appropriate message

class InvalidDepositError(ValueError):
    """Custom exception for invalid banking deposits"""
    pass

class InvalidWithdrawalError(ValueError):
    """Custom exception for invalid banking withdrawals"""
    pass

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:
            raise InvalidDepositError(f"Rejected: Cannot deposit an amount of £{amount:.2f}. "
                                      f"Deposits must be greater than zero.")


        self.balance += amount 

    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidWithdrawalError(f"Rejected: Cannot withdraw an amount of £{amount:.2f}."
                                      f"Withdrawals must be greater than zero.")

        if amount > self.balance:
            raise InvalidWithdrawalError(f"Rejected: Cannot withdraw an amount of £{amount: .2f}."
                                         f"Cannot withdraw more than your balance.")

        self.balance -= amount

    def get_balance(self, amount):

        print(f"Your balance is: £{self.balance}")


def main():
    account = BankAccount("Alice", 100)
    account.deposit(50)
    account.withdraw(30)
    




if __name__ == "__main__":
    main()



# %%
