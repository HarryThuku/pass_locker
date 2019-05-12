import unittest
from user import User

class User_test(unittest.TestCase):
    def setUp(self):
        self.new_user = User('harry','kk',[])
    
        def tearDown(self):
        User.users_list = {}


    def test_save_user(self):
        self.new_user.make_user_dict()
        self.assertTrue(len(User.users_list),1)

    



    

    if __name__ == "__main__":
        unittest.TestCase()