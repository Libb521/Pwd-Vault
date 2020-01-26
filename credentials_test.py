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
        self.new_credentials = Credentials("Libby","instagram","Libby19","eotieno39@yahoo.com")

    def test_init(self):
        '''
        This is to test if it has been initialized properly
        '''

        self.assertEqual(self.new_credentials.name,"Libby")
        self.assertEqual(self.new_credentials.credentials,"instagram")
        self.assertEqual(self.new_credentials.password,"Libby19")
        self.assertEqual(self.new_credentials.email,"eotieno39@yahoo.com")

if __name__ == '__main__':
    unittest.main()


