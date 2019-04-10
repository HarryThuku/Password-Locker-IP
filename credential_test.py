import unittest
from credentials import Credentials

class TestCredential(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_credential = Credentials('instagram','harry@gmail.com','king',6)
    
    def tearDown(self):
        '''
        '''
        Credentials.credential_list = []


    def test_saveAccount(self):
        '''
        '''
        self.new_credential.save_account()








if __name__ == "__main__":
    unittest.main()