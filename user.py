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
        This is to delete users from a list
        '''

        User.user_list.remove(self)
    @classmethod
    def find_by_password(cls, password):
        '''
        Method that takes in a password and returns user that match the password

        Args:
            password: pass to search
        Returns :
            user
        '''

        for user in cls.user_list:
            if user.password == password:
                return user

    @classmethod
    def user_exist(cls, password):
        '''
        it checks if user exists from the list.
        Args:
            passwrd: if it exists
        Returns :
            Boolean: True or false depending if user exists
        '''
        for user in cls.user_list:
            if user.password == password:
                    return True

        return False


    @classmethod
    def display_users(cls):
        '''
        shows the user list
        '''
        return cls.user_list


    @classmethod
    def copy_email(cls,password):
        user_found = User.find_by_password(password)
        pyperclip.copy(user_found.email)


    

