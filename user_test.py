import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_user = User('harry','harry@gmail.com','bigboy',[])

    def tearDown(self):
        '''
        '''
        User.users_list = {}

    def test_init(self):
        '''
        '''
        self.assertEqual(self.new_user.u_name, 'harry')
        self.assertEqual(self.new_user.email, 'harry@gmail.com')
        self.assertEqual(self.new_user.password, 'bigboy')
        self.assertEqual(self.new_user.accounts, [])

    def test_save_user(self):
        '''
        '''
        self.new_user.save_user()
        self.assertIsNotNone(User.users_list)

    def test_add_user_to_users_list(self):
        '''
        '''

        pass






if __name__ == "__main__":
    unittest.main()