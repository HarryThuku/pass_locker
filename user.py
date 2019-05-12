class User:
    users_list = {}
    '''
    '''

    def __init__( self, user_name, password, credentials ):
        '''
        '''

        self.user_name = user_name
        self.password = password
        self.credentials = []



    def make_user_dict(self):
        '''
        '''

        user = { }
        user[self.user_name] = dict( user_name = self.user_name, password = self.password, credentials = [] )
        print('\n______________________ Successfully created an account for user {}. ______________________\n'.format(self.user_name))
        
        if self.user_name in User.users_list.keys():
            print('!_______________________ Error saving user. The user {} already exits. Try a different user name _______________________!\n'.format(self.user_name))
            return False
        else:
            self.users_list.update( user )
            print('________________________ User {}\'s account has been successfully saved. ________________________\n'.format(self.user_name))
            return True





    # def save_user( self, user, user_name ):
    #     '''
    #     '''

    #     if user_name in User.users_list.keys():
            
    #     else:
            


    def find_user_by_uname( self, user_name ):
        '''
        '''
        
        users = User.users_list
        for key,value in users.items( ):
            if key == user_name:
                print('\n___________________ Found user {} records ___________________\n'.format(user_name))
                return value
            else:
                print('\n!__________________ User {} is not in our records. __________________!\n'.format(user_name))



    def add_credential_to_user( self, credential, user ):
        '''
        '''

        user[self.user_name]['credentials'].append( credential )
        return True



    def find_credential( self, user_account, credential_name ):
        '''
        '''

        credentials = user_account[self.user_name]['credentials']
        for credential in credentials:
            if credential['cred_name'] == credential_name:
                print('_________________________ Found your {} credentials _________________________\n'.format(credential_name))
                return credential