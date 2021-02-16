# 9. Model an Account class in the banking sector
# Account class ->
#       first name,
#       last name,
#       amount

# 10. Write a class that models the account described in 9 above.
# Also model the operations to be carried out on the model

class Account():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.name = f'{fname} {lname}'
        self.amount = 0

    def balance(self):
        print(f'Your present balance is ${self.amount}')

    def deposit(self, amt):
        self.amount += amt
        print(f'You just deposited ${amt}. You current balance is ${self.amount}')

    def withdraw(self, amt):
        if self.amount - amt > 0:
            self.amount -= amt
            print(f'You just withdrew ${amt}. You current balance is ${self.amount}')
        else:
            print('Insufficient funds.')
