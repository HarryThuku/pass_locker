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
                
