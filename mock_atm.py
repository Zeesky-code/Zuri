from  datetime import datetime
now = datetime.now()
date_time = now.strftime("%H:%M:%S %d/%m/%Y")

name = input('What is your name?\n')
#stored user data
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi', 'passwordMike','passwordLove']
try:
    if (name in  allowedUsers):
        password = input('Your password? \n')
        userId=allowedUsers.index(name)
    else:
        print('Name not found, please try again')
    try:
        if(password == allowedPassword[userId]):
            print('Welcome %s' %name)
            print(date_time)
            #options
            print('These are the available options')
            print('1.Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')

            selectedOption = int(input('Please select an option:'))

            if(selectedOption == 1):
                print('You selected %s' % selectedOption)
                input("How much would you like to withdraw? \n")
                print('Please take your cash')

                
            elif(selectedOption == 2):
                print('You selected %s'  % selectedOption)
                balance = input("How much would you like to deposit? \n")
                print('Your current balance is %s' %balance)
            
            elif(selectedOption == 3):
                print('You selected %s'  % selectedOption)
                input('What issue would you like to report? \n')
                print('Thank you for contacting us.')
                
            else:
                print('Invalid option selected,please try again')
        else:
            print('Password Incorrect, please try again')
    except: 
            pass
except print(0):
    pass


