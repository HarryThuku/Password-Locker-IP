from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from user import User

root = Tk()

class Home(Frame):
    '''
    '''
    def __init__(self, master):
        Frame.__init__(self, master)
        self.screen = Frame()
        print('available users at the begining: ',User.users_list,'\n\n')
        if User.users_list:
            self.login()
        else:
            tkinter.messagebox.showinfo('Info','kindly sign up first. There are no registered users yet.')
            self.signUp()




    def canvas(self, new_user, user_account, uname):




        '''
        This function is called by the login button. Its primary purpose is to authenticate user info and route them to their page.
        '''
        self.screen.destroy()
        self.screen = Frame()
        
        # heading details:
        self.uname_label = Label( self.screen, text = 'Loged in as {}.'.format(user_account['u_name']) )
        self.uname_label.place( x = 20, y = 20 )

        # user Data:
        self.email_label = Label( self.screen, text = 'Email: {}.'.format(user_account['email']) )
        self.email_label.place( x = 20, y = 40 )

        # sign out button:
        self.signOut = Button( self.screen, text = 'Sign Out', width = '15', command = self.signUserOut )
        self.signOut.place( x = 800, y = 20 )

        
        # add credentials:
        self.add_credential = Button( self.screen, text = 'Add Credential', width = '15', fg = 'navy', bg = 'green', command = self.addCredential )
        self.add_credential.place( x = 800, y = 100 )



        # displaying credentials

        l = Listbox( self.screen, width = 115, height = 18, selectmode = EXTENDED )
        l.place( x = 30, y = 160 )

        # for item in user_account['account']:
        #     print(item)
        #     if item != "{}":
        #         l.insert(item['account_name'])            





        self.screen.pack(fill = BOTH, expand = 1)






        # tkinter.messagebox.showinfo('login','Success!')
    



    def login(self):
        '''
        This is the parent graphical interface. It acts as the authentication page.
        '''

        self.screen.destroy()
        self.screen = Frame()
        


        # heading details
        self.welcome = Label( self.screen, text = 'Welcome to your password vault' , bg = 'grey', fg = 'black', width = '1000', height='3')
        self.welcome.pack()


        # email interface construct
        self.email_text = Label( self.screen, text = 'Email : ',)
        self.email_text.place(x = 375, y = 80)
        self.mail_entry = Entry( self.screen, width = '40')
        self.mail_entry.place(x = 450, y = 80)

        # password interface construct
        self.password_text = Label( self.screen, text = 'Password : ',)
        self.password_text.place(x = 350, y = 120)
        self.password_entry = Entry( self.screen, show = '*', width = '40')
        self.password_entry.place(x = 450, y = 120)

        



        # login interface construct
        self.login_btn = Button( self.screen, text = 'Login', width = '12', command = self.ultimate)
        self.login_btn.place(x = 450, y = 160)
        self.labelor=Label( self.screen, text = 'or', fg = 'red')
        self.labelor.place(x=600, y = 163)

        # signUp interface construct
        self.signUp_btn = Button( self.screen, text = 'Sign Up', width = '12', command = self.signUp)
        self.signUp_btn.place(x = 650, y = 160)
        self.screen.pack(fill = BOTH, expand = 1)


    def ultimate(self):
        new_user = User('','','',[])
        email = self.mail_entry.get()
        password = self.password_entry.get()

        result = self.checkNulls([email,password])

        if result == False:
            tkinter.messagebox.showerror('Ooops!','Please check to ensure that all fields have been filled.')
        
        else:
            print('caught email entry: ',email,'\n\n')

            user_account = new_user.find_user_by_email( email )
            print('the available list of users: \n\n',User.users_list,'\n\n')
            
            if user_account==None:
                tkinter.messagebox.showerror('Ooops!','The email entered is not registered. Please register first.')
                self.login()
                
            else:
                print('\n\nuser account: ',user_account,'\n\n')
            #
            # 
            # 
            
            
            if user_account['password'] == password:
                tkinter.messagebox.showinfo('Successful Login!','Welcome ' + email + '.')
                return self.canvas(new_user, user_account, email)
            else:
                tkinter.messagebox.showerror('Ooops!','The password entered has been deemed un-authentic.')



    def signUp(self):
        '''
        '''

        self.screen.destroy()
        self.screen = Frame()

        


        # heading details
        self.heading = Label( self.screen, text='Sign up and get a free accounts mangager.', bg = 'grey', fg = 'black', width='1000', height='3')
        self.heading.pack()

        # uname interface construct
        self.uname_text = Label( self.screen, text = 'User Name : ',)
        self.uname_text.place(x = 325, y = 80)
        self.uname_entry = Entry( self.screen, width = '40')
        self.uname_entry.place(x = 450, y = 80)

        # email interface construct
        self.email_text = Label( self.screen, text = 'Email : ',)
        self.email_text.place(x = 363, y = 120)
        self.email_entry = Entry( self.screen, width = '40')
        self.email_entry.place(x = 450, y = 120)

        # password interface construct
        self.passwd_text = Label( self.screen, text = 'Enter Password : ')
        self.passwd_text.place(x = 300 ,y = 160)
        self.passwd_entry = Entry( self.screen, show='*', width = '40')
        self.passwd_entry.place(x = 450, y = 160)

        # confirm password interface construct
        self.con_passwd_text = Label( self.screen, text = 'Confirm Password : ')
        self.con_passwd_text.place(x = 285 ,y = 200)
        self.con_passwd_entry = Entry( self.screen, show = '*', width = '40')
        self.con_passwd_entry.place(x = 450, y = 200)




        # sign in button
        signup_btn = Button( self.screen, text = 'Sign Up', width = '15', command = self.final)
        signup_btn.place(x = 450, y = 240)
        self.screen.pack(fill = BOTH, expand = 1)

        # log in button
        signIn_btn = Button( self.screen, text = 'Proceed to login', width = '15', command = self.checkLogin )
        signIn_btn.place(x = 630, y = 240)

    def checkNulls(self, args):
        result = all(item != '' for item in args)
        print (result)
        return result


    def final(self):
        password = self.passwd_entry.get()
        print(password)
        con_password = self.con_passwd_entry.get()
        uname = self.uname_entry.get()
        email = self.email_entry.get()

        # 
        result = self.checkNulls([password,con_password,uname,email])

        if result == False:
            tkinter.messagebox.showwarning('Ooops!','There are empty values in some fields. Kindly check on that before proceeding')

        else:

            if password == con_password:
                self.new_user = User(uname,email,password,[])
                # 
                print('new user email: \n\n',self.new_user.email,'\n\n')
                # 
                
                self.user_account = self.new_user.save_user()
                print('user account keys: ',self.user_account.keys(),'\n\n')
                # 
                
                print('user account values: ',self.user_account.values(),'\n\n')
                
                # 
                print('user account dictionary: ',self.user_account,'\n\n being passed to add_user_to_users_list function.\n\n')
                # 
                print('email at add-user-to-users-list: ',email,'\n\n')

                state = self.new_user.add_user_to_users_list(email,self.user_account)
                print('email at add-user-to-users-list: ',email,'\n\n')

                if state:
                    tkinter.messagebox.showinfo('Success',f'user {email} has been succesfully created.')
                    self.login()
                else:
                    tkinter.messagebox.showwarning('Ooops!',f'user {email} already exits. Try a different Email Address perhaps!')
                    self.signUp()
            else:
                tkinter.messagebox.showerror('Ooops!','The confirmation password does not match the suggested password. Please try again.')
                password = ''
                con_password = ''



    def signUserOut(self):
        '''
        '''
        self.login()


    def checkLogin(self):
        '''
        '''
        if User.users_list:
            self.login()
        else:
            tkinter.messagebox.showinfo('Info','kindly sign up first. There are no registered users yet.')
            self.signUp()


    def addCredential(self):
        '''
        '''

        self.screen.destroy()
        self.screen = Frame()


        self.heading = Label( self.screen, text='Add new account detail', bg = 'grey', fg = 'black', width='1000', height='3')
        self.heading.pack()

        # uname interface construct
        self.uname_text = Label( self.screen, text = 'User Name : ',)
        self.uname_text.place(x = 325, y = 80)
        self.uname = StringVar()
        self.uname_entry = Entry( self.screen, textvariable = self.uname, width = '40')
        self.uname_entry.place(x = 450, y = 80)

        # email interface construct
        self.email_text = Label( self.screen, text = 'Email : ',)
        self.email_text.place(x = 363, y = 120)
        self.email = StringVar()
        self.email_entry = Entry( self.screen, textvariable = self.email, width = '40')
        self.email_entry.place(x = 450, y = 120)

        # password interface construct
        self.passwd_text = Label( self.screen, text = 'Enter Password : ')
        self.passwd_text.place(x = 300 ,y = 160)
        self.password = StringVar()
        self.passwd_entry = Entry( self.screen, textvariable = self.password, width = '40')
        self.passwd_entry.place(x = 450, y = 160)


        # submit credential

        self.cred_submit = Button( self.screen, text = 'Submit Credentials')
        self.cred_submit.place(x = 550, y = 200)
        self.screen.pack()



    


root.geometry('1000x500')
root.title('Password Locker')
root.resizable(0, 0)
welcome = Home(root)
root.mainloop()