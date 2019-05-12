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
        print('______________________ Successfully created an account for user {}. Do you want to save your progress? ______________________\n'.format(self.user_name))
        return user


    