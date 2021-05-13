def account_number_validation(accountNumberFromUser):
    #ensure the input is not empty
    #ensure it is 10 digits long
    #ensure it is an integer
    if accountNumberFromUser:
        try:
            int(accountNumberFromUser)
            if len(str(accountNumberFromUser)) == 10:
               return True
            else:
                print('Invalid account number,account number cannot be more or less than 10 digits')
                return False
                login()
        except ValueError:
            print('Invalid account number, account number must be an integer')
            return False
            login()
    else:
        print('Account number is required')
        return False
        login()
#registration validation
def first_name_validation(first_name):
    #ensure the input is not empty
    if first_name:
        return True
    else:
        print('First name is required')
        return False
        register()

def last_name_validation(last_name):
    #ensure the input is not empty
    if last_name:
        return True
    else:
        print('Last name is required')
        return False
        register()

def email_validation(email):
    #ensure the input is not empty
    if email:
        return True
    else:
        print('Email address is required')
        return False
        register()

def password_validation(password):
    #ensure the input is not empty
    if password:
        return True            
    else:
        print('Password is required')
        return False
        register()

