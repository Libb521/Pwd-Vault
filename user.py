import pyperclip

class User:
    """
    This is to generate new contacts.
    """
    user_list =[]

    def __init__(self,name1,name2,password,email):

         self.name1 = name1
         self.name2 = name2
         self.password = password
         self.email = email

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):

        '''
        This is to delete user from list
        '''

        User.user_list.remove(self)

    

