def init_validation(haveAccount):
    #ensure the input is not empty
    #ensure the input is an integer
    if haveAccount:
        try:
            int(haveAccount)
            return True
            
        except ValueError:
            print('Invalid option selected')
            return False
    else:
        print('Please select an option')
        return False

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
        login()
        return False
        
#registration validation
def first_name_validation(first_name):
    #ensure the input is not empty
    if first_name:
        return True
    else:
        print('First name is required')
        register()
        return False
        

def last_name_validation(last_name):
    #ensure the input is not empty
    if last_name:
        return True
    else:
        print('Last name is required')
        register()
        return False
        

def email_validation(email):
    #ensure the input is not empty
    if email:
        return True
    else:
        print('Email address is required')
        register()
        return False
        

def password_validation(password):
    #ensure the input is not empty
    if password:
        return True            
    else:
        print('Password is required')
        register()
        return False
        

