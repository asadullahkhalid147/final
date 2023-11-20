from user import User
from admin import Admin

allow_loan= True
users= []

admins = [Admin("khalid", "000")]

def create_account():
    email = input('enter email: ')



    password = input('enter password:')
    user = User(email,password)

    users.append(user)
    print('account created.')

def user_menu(user):
    while True:
        print(' \n user menu:')
        print('1.deposit')

        print('2.withdraw ')
        print('3.transfer')
        print('4. check balance ')
        print('5.take loan ')

        print('6.transaction history')
        print('7.logout')
        choice = input(' enter your choice:')


        if choice=='1':
            amount= float(input('enter  deposit :'))
            user.deposit(amount)
            print(f'{amount} deposited.')


        elif choice=='2':
            amount = float(input('enter withdrawal amount:'))
            user.withdraw(amount)


        elif choice=='3':
            recipient_email= input('Enter recipient email:')
            recipient= next((u for u in users if u.email==recipient_email), None)
            
            if recipient:
                amount = float(input('enter the transfer amount: '))
                user.transfer(recipient, amount)
                print(f'{amount} transferred.')
            else:
                print('Recipient not found.')
        elif choice=='4':
            balance = user.check_balance()
            print(f'available balance:{balance}')


        elif choice =='5':
            user.take_loan()

        elif choice=='6':
            history= user.check_transaction_history()
            print("Transaction History:")
            for transaction in history:
                print(transaction)


        elif choice== '7':
            break
        else:
            print("Invalid choice. Please try again.")


def admin_menu(admin):
    while True:
        print('\n admin menu: ')
        print("1. check total balance")

        print('2.check laon')

        print('3.on off loan feature')
        print('4.logout')

        choice = input('enter  choice:')

        if choice =='1':
            total_balance = admin.check_total_balance(users)

            print(f' total balance : {total_balance}')


        elif choice== '2':
            total_loan = admin.check_total_loan(users)

            print(f' total loan amount : {total_loan}')

        elif choice == '3':
            enable = input(" enable (yes/no): ").lower()== 'yes'

            admin.toggle_loan_feature(enable)


        elif choice== '4':
            break
        else:
            print(' invalid choice,')


def main():
    while True:
        print('\n Banking Management System: ')
        print('1.Create account')

        print('2. User login')
        print('3. Admin login')
        print('4. Exit')

        choice= input(' enter your choice: ')

        if choice=='1':
            create_account()

        elif choice=='2':
            email=input('enter  email: ')
            password=input(' enter  password: ')
            user=next((u for u in users if u.email==email and u.password==password),None)
            if user:
                user_menu(user)
            else:
                print(' invalid email or password, try again.')


        elif choice =='3':
            email= input(' enter admin email: ')
            password=input('enter admin password: ')
            admin =next((a for a in admins if a.email==email and a.password==password),None)
            if admin:
                admin_menu(admin)
            else:
                print(' invalid email or password, try again.')

        elif choice=='4':
            print('The end')
            break
        else:
            print(' invalid choice, try again.')


if __name__== '__main__':
    main()
