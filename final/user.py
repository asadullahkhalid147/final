class User:
    def __init__(self,email,password):
        self.email= email

        self.password=password
        self.balance=0

        self.loan =0
        self.transaction_history= []


    def deposit(self,amount):
        self.balance+= amount
        self.transaction_history.append(f'deposit {amount}')


    def withdraw(self,amount):
        if amount>self.balance:
            print('money is finished')
        else:
            self.balance -= amount
            self.transaction_history.append(f'withdrew {amount}')

    def transfer(self,recipient,amount):
        if amount> self.balance:
            print('not much  for transfer.')
        else:
            self.balance-= amount
            recipient.balance +=amount
            self.transaction_history.append(f'Transferred{amount}')

    def check_balance(self):
        return self.balance

    def take_loan(self):
        if self.loan==0:
            loan_amount= 2 * self.balance
            self.balance +=loan_amount
            self.loan+=loan_amount

            self.transaction_history.append(f'loan took:{loan_amount}')
            print(f' loan of {loan_amount} credited to your account.')
        else:
            print("You already have took loan.")



    def check_transaction_history(self):
        return self.transaction_history