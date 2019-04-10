from credentials import Credentials

class User:
        '''
        This is a class that manages user data.
        '''
        users_list = {}

        def __init__(self, u_name, email, password, accounts):
                '''
                '''

                self.u_name = u_name
                self.email = email
                self.password = password
                self.accounts = []


        def save_user(self):
                '''
                This is a method to create a user item as a dictionary.
                '''
                user = {}
                user[self.email]=dict( u_name = self.u_name, email = self.email, password = self.password, accounts = [] )
                return user
        

        def add_user_to_users_list(self,email,user):
                '''
                this method appends the user object to the user dictionary.
                '''
                if email in self.users_list.keys():
                        return False
                self.users_list.update(user)
                return True


        def add_account_to_user(self, account, user):
                '''
                '''
                user[self.email]['accounts'].append(account)

        
        def find_user_by_email(self, email):
                '''
                This is a class method to display all users.
                '''
                users = User.users_list
                for key,value in users.items():
                        if key == email:
                                return value
                
        
        def find_account_by_name(self, user, account_name):
                '''
                '''
                acc_list = user[self.email]['accounts']
                account = [x for x in acc_list if x['account_name'] == account_name]
                return account