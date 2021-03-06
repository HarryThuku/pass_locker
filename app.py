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
                        print('\nLet\'s add an account. You could read the documentation for further clarification at "www.google.com"\n')
                        acc_name = input('Account name : ')
                        acc_url = input('Account url : ')
                        acc_pass = input('Account password : ')
                        acc_conf_pass =n input('Confirm password : ')
                        results = emptyChecker([acc_conf_pass,acc_name,acc_pass,acc_url])
                        if acc_conf_pass == acc_pass and results:
                            new_credential = Credential(acc_name, acc_url, acc_pass)
                            account['credentials'].append(new_credential)
                            if len(account['crendentials'])>=1:
                                print('Successfully added your {}\'s credential to your credential list.\n'.format(acc_name))
                    
                    elif option == 'b':
                        print('\n\t^^^^^^^^^^ These are all accounts listed under you. ^^^^^^^^^^^\n')
                        for item in account['credentials']:
                            print('\tYour {}\'s account url is {}.\n'.format(item.cred_name,item.cred_url))
                    
                    elif option == 'c':
                        pass
                    
                    elif option == 'x':
                        print('\nloging out.\n')
                        break
                    
                    else:
                        print('\n\tIncorrect input. Please select from available inputs.\n')
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
            

def app():
    '''
    '''
    while True:
        print('Welcome to password locker. What would you like to do?\n- l/L to login.\n- s/S to signup.\n- x/X to exit system.')
        entry = input('\nProceed to ? ')
        if entry == 'l':
            if User.users_list:
                login()
            else:
                print('\nThere are no registered users yet. Register first before proceeding to signing in.\n')
                create_account()
        elif entry == 's':
            create_account()
        
        elif entry == 'x':
            print('\n............ Exiting system .........\n\n')
            break
        
        else:
            print('Wrong choices. Please try again.')

if __name__ == "__main__":
    app()