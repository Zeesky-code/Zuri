import random
import validation
from getpass import getpass #to make the password invisible
database = {} 

def init():
    print("Welcome to Bank of Esther ")
 
    haveAccount = input("Do you have account with us: 1 (yes) 2 (no) \n")
    is_valid_option = validation.init_validation(haveAccount)
    #error with validation 
    if is_valid_option:
        if(int(haveAccount) == 1):
            login()
        elif(int(haveAccount == 2)):
            register()
    else:
        init()


#login 
def login():
    print("******* Login *******")
    accountNumberFromUser = int(input("What is your account number? \n"))
    is_valid_account = validation.account_number_validation(accountNumberFromUser)
    
    if is_valid_account: 
        password = getpass("What is your password? \n")

        for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    bankOperation(userDetails)
            else:
                print('Invalid account or password')
                login()   
                
    
    

#register
def register():
    print("****** Register *******")
    email = input("What is your email address? \n")
    is_valid_email = validation.email_validation(email)
    if is_valid_email:

        first_name = input("What is your first name? \n")
        is_valid_first_name = validation.first_name_validation(first_name)
        if is_valid_first_name:

            last_name = input("What is your last name? \n")
            is_valid_last_name = validation.last_name_validation(last_name)
            if is_valid_last_name:

                password = input("Create a password: \n")
                password = validation.password_validation(password)
                if is_valid_first_name:

                    accountNumber = generationAccountNumber()

                    database[accountNumber] = [ first_name, last_name, email, password ]

                    print("Your Account Has been created")
                    print(" == ==== ====== ===== ===")
                    print("Your account number is: %d" % accountNumber)
                    print("Make sure you keep it safe")
                    print(" == ==== ====== ===== ===")

                    login()
    
        

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )

    selectedOption = int(
        input(
            "What would you like to do? (1) Deposit (2) Withdrawal (3) Purchase Airtime (4) Complain (5) Logout \n")
        )

    if(selectedOption == 1):
        deposit()
    elif(selectedOption == 2):
        withdrawal()
    elif(selectedOption == 3):
        airtime()
    else:
        print("Invalid option selected")
        bankOperation(user)

def depositOperation():
    deposit_amount=input('How much would you like to deposit?')
    print('You have successfully deposited' + deposit_amount)


def withdrawalOperation():
    withdraw_amount=input('How much would you like to withdraw?')
    print('Take your cash')

def airtime():
    print('What network do you want to purchase?')
    phone_number = input('Please enter the phone number:  \n' )
    amount = input('How much airtime do you want to purchase')
    print('Your purchase of ' + amount + ' to ' + phone_number + ' is successful')

def generationAccountNumber():
    return random.randrange(1111111111,9999999999)

def logout():
    init()

#### ACTUAL BANKING SYSTEM #####

init()
