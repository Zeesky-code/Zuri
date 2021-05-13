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
        except ValueError:
            print('Invalid account number, account number must be an integer')
            return False
    else:
        print('Account number is required')
        return False