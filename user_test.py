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

    
    def test_user_values(self):
        self.assertTrue(self.new_user.user_name,'harry')
        self.assertTrue(self.new_user.password,'kk')
        self.assertEqual(self.new_user.credentials,[])
    
    def test_find_user(self):
        self.new_user.find_user_by_uname('harry')



    

    if __name__ == "__main__":
        unittest.TestCase()