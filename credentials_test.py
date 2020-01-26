import unittest
import pyperclip
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    '''
    This test class defines test cases for the credentials behavior
    '''

    def setUp(self):
        '''
        This is to run before each test case.
        '''
        self.new_credentials = Credentials("Libby","Instagram","Libby19","eotieno39@yahoo.com")

    def test_init(self):
        '''
        This is to test if it has been initialized properly
        '''

        self.assertEqual(self.new_credentials.name,"Libby")
        self.assertEqual(self.new_credentials.credential,"Instagram")
        self.assertEqual(self.new_credentials.password,"Libby19")
        self.assertEqual(self.new_credentials.email,"eotieno39@yahoo.com")


    
    def test_save_credentials(self):
        '''
        This is a test to help in saving the credentials inputted by users 
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):


            Credentials.credentials_list = []
   

    def test_save_multiple_credentials(self):
        '''
        This is a test to see if we can save multiple credentials.
        '''
        self.new_credentials.save_credentials()
        test_save_credentials = Credentials("Test","user","Libb19","eotieno39@yahoo.com")
        test_save_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        This test enables credentials be deleted from our credential list
        '''
        self.new_credentials.save_credentials()
        test_save_credentials = Credentials("Test","user","Libb19","eotieno39@yahoo.com")
        test_save_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

   

if __name__ == '__main__':
    unittest.main()



