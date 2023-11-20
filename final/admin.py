class Admin:
    def __init__(self,email,password):
        self.email=email
        self.password=password


    def check_total_balance(self,users):
        total_balance=sum(user.balance for user in users)
        return total_balance


    def check_total_loan(self,users):
        total_loan=sum(user.loan for user in users)
        return total_loan





    def toggle_loan_feature(self,enable):
        global allow_loan
        allow_loan = enable

        if allow_loan:
            print(" loan feature available.")
        else:
            print(" loan feature  disabled.")