import string
import random
import pyperclip


class Credentials:

        '''
        Defines the structure and behavior of credentials.
        '''
   
        def __init__( self,account_name, email, password_length, pass_len ):
                '''
                Initializes the Credentials class instance.
                '''
                self.account_name = account_name
                self.email = email
                self.password = ''
                self.password_length = pass_len


        def save_account(self):
                '''
                This method is used to save the account to where it'll be called to.
                '''
                account = {}
                account[self.account_name] = dict(
                        account_name = self.account_name, email = self.email, password = self.passwordGenerator(self.password_length)
                )
                return account


        def passwordGenerator(self, password_length):
                '''
                This method is used to to create random passwords. It takes in the argument password_length, which predetermines the expected password length.
                '''
                password_generator = ''.join(random.choices(
                        string.ascii_uppercase + string.digits, k = password_length
                ))

                return password_generator