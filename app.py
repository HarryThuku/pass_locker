from user import User
from credential import Credential


def emptyChecker(*args):
    '''
    '''
    results = all([item!='' for item in args])
    return results

def login():
    '''
    '''
    main_user = User('','',[])
    while True:
        print('\t\tlogin page')
        print('__________________________________  __________________________________')
        username = input('Enter your username : ')
        account = main_user.find_user_by_uname(username)


        if account:
            print('_____________________ Enter password for {}\'s account _____________________\n'.format(username))
            attempt_password = input()
            if attempt_password == account['password']:
                print('You are currently loged in as {}.\n'.format(username))
                
                while True:
                    print('\n*_____________________ What would you like to do? _____________________*\n\na/A for add account credentials.\nb/B to list credentials.\nc/C to delete account.\nx/X to logout.')
                    option = input('\nproceed with option? ')
                    if  option == 'a':
                        print('Let\'s add an account. You could read the documentation for further clarification at "www.google.com"')
                        acc_name = input('Account name : ')
                        acc_url = input('Account url : ')
                        acc_pass = input('Account password : ')
                        acc_conf_pass = input('Confirm password : ')
                        results = emptyChecker([acc_conf_pass,acc_name,acc_pass,acc_url])
                        if acc_conf_pass == acc_pass and results:
                            new_credential = Credential(acc_name, acc_url, acc_pass)
                            account['credentials'].append(new_credential)
                            if len(account['credentials'],>=1):
                                print('Successfully added your {}\'s credential to your credential list.\n'.format(acc_name))
                    
                    elif option == 'b':
                        for item in account['credentials']:
                            print('\tYour {} account url is {}.\n'.format(item.cred_name,item.cred_url))
                    
                    elif option == 'c':
                        pass
                    
                    elif option == 'x':
                        print('loging out.')
                        break
                    
                    else:
                        print('Incorrect input. Please select from available inputs.')
            else:
                print('\tIncorrect username or password. Try again\n')


def create_account():
    while True:
        print('+++++++++++++++++++++++++++++++++ Create a new account +++++++++++++++++++++++++++++++++\n')
        uname = input('Enter your preffered username : ')
        pword =  input('Enter your preffered password : ')
        conf_pass = input('Confirm password entry : ')
        result = emptyChecker([uname,pword,conf_pass])

        if result and pword == conf_pass:
            new_account = User(uname,pword,[])
            new_account.make_user_dict()
            break
            

