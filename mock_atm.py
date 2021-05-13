import random

database = {}

#system initialization
def init():
    print('Welcome to Esther Bank')
    
    have_account = int(input('Do you have an account with us? \n 1 (yes) 2 (no) \n'))

    if(have_account == 1):
        login()
    elif(have_account == 2):
        register()
    else:
        print('You have selected an invalid option')
        init()


#user login
def login():
    print('***Login to your account***')

    user_acct = int(input('Enter your account number: \n'))
    user_pwd = input('Enter your password: \n')

    for acct_no, user_details in database.items():
        if user_acct == acct_no:
            if user_pwd == user_details[3]:
                print('Welcome %s %s' %(user_details[0], user_details[1]))
                bank_operations(user_details)
        else: 
            print('Invalid account or password, try again')
            login()

    


#user registration
def register():
    print('********Register******')
    email = input('Enter your email address: \n')
    f_name = input('Enter your first name: \n')
    l_name = input('Enter your last name: \n')
    password = input('Create a strong password: \n') 

    account_number = generate_acct_number()
    balance = 0

    database[account_number] = [f_name, l_name, email, password, balance]
    
    print('Welcome %s, your account has been created \n' %f_name)
    print('Your account number is %s \n' %account_number)
    print('Ensure your keep your account number and password safe')
    login()


#bank operations
def bank_operations(user):
    print('What would you like to do? \n')
    print('1. Deposit')
    print('2. Withdrawal')
    print('3. Check account balance')
    print('4. Purchase Airtime')
    print('5. Logout')

    selected_option = int(input('Select an option \n'))

    if(selected_option == 1):
        deposit(user) 
    elif(selected_option == 2):
        withdraw(user)
    elif(selected_option == 3):
        check_balance(user)
    elif(selected_option == 4):
        airtime()
    elif(selected_option == 5):
        logout()
    else:
        print('Invalid option, try again')
        bank_operations(user)

def withdraw(user):
    amount = int(input('How much would you like to withdraw? \n'))
    if amount >= user[-1]:
        print('Insufficient Funds')
        retry = int(input('Would you like to try again or deposit funds? \n 1. Retry 2. Deposit 3. exit \n'))
        if(retry == 1):
            withdraw(user)
        if(retry == 2):
            deposit(user)
        else:
            print('Thank you for banking with us')
            exit()

    else:
        user[-1] -= amount #subtracts amount from user_balance
        print('Take your cash')
        print('Do you want to make another transaction?')
        option = int(input(' 1.Yes 2.No \n'))

        if(option == 1):
            bank_operations(user)
        elif(option == 2):
            print('Thank you for banking with us')
            logout()

def deposit(user):
    amount = int(input('How much do you want to deposit? \n'))
    user[-1] += amount #subtracts amount from user_balance
    acct_balance = user[-1]
    print('Deposit successful')
    print('Your current account balance is %s' %acct_balance)
    print('Do you want to make another transaction?')
    option = int(input(' 1.Yes 2.No \n'))

    if(option == 1):
        bank_operations(user)
    else:
        print('Thank you for banking with us')
        login()

def check_balance(user):
    acct_balance = user[-1]
    print('Your account balance is %s' %acct_balance)

    print('Do you want to make another transaction?')
    option = int(input(' 1.Yes 2.No \n'))

    if(option == 1):
        bank_operations(user)
    else:
        print('Thank you for banking with us')
        login()

def airtime(user):
    acct_balance = user[-1]
    airtime_amount= int(input("How much airtime would you like to purchase? \n"))
    user[-1] -= airtime_amount #subtracts airtime_amount from user_balance
    acct_balance = user[-1]
    network = int(input("What would network would you like to purchase? (1) MTN (2) GLO (3) Airtel (4) 9mobile \n"))
    input('Please enter the phone number: ')
    print('Your airtime has been successfully sent.' )
    print('Your current account balance is %s' %acct_balance)
    print('Do you want to make another transaction?')
    option = int(input(' 1.Yes 2.No \n'))

    if(option == 1):
        bank_operations(user)
    else:
        print('Thank you for banking with us')
        login()
def logout():
    print('Thank you for banking with us')
    login()


# generate account number for new user
def generate_acct_number():
    return random.randrange(1111111111,9999999999)


### ACTUAL BANKING SYSTEM ### 
init()


