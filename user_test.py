import unittest
import pyperclip
from user import User 



class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for user class

    '''


    def setUp(self):
        '''
        Set method to run before test classes
        '''
        self.new_user = User("Elizabeth","Otieno","Libby19","eotieno39@yahoo.com")


    def test_init(self):
        '''
        to test if the object is initialized well
        '''

        self.assertEqual(self.new_user.name1,"Elizabeth")
        self.assertEqual(self.new_user.name2,"Otieno")
        self.assertEqual(self.new_user.password,"Libby19")
        self.assertEqual(self.new_user.email,"eotieno39@yahoo.com")
    
    def test_save_user(self):
        '''
        test to test if user is saved into the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):
            '''
            it cleans up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_user(self):
            '''
            to check saving multiple users to our user_list is possible
            '''
            self.new_user.save_user()
            test_save_user = User("Test","user","Libby19","eotieno39@yahoo.com") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
            '''
             to test if we can remove user from our list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","Libby19","eotieno39@yahoo.com") 
            test_user.save_user()

            self.new_user.delete_user() 
            self.assertEqual(len(User.user_list),1)


    def test_find_user_by_password(self):
        '''
        to check if we can find user by password
        '''

        self.new_user.save_user()
        test_user = User("Test","user","Libby19","eotieno39@yahoo.com") 
        test_user.save_user()

        found_user = User.find_by_password("Libby19")

        self.assertEqual(found_user.email,test_user.email)

    def test_user_exists(self):
        

        self.new_user.save_user()
        test_user = User("Test","user","Libby19","eotieno39@yahoo.com")
        test_user.save_user()

        user_exists = User.user_exist("Libby19")

        self.assertTrue(user_exists)


    def test_display_all_users(self):
        '''
        it returns a list of all users in a list
        '''

        self.assertEqual(User.display_users(),User.user_list)