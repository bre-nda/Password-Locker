import unittest
from credentials import Credentials

class TestCredentials (unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("user_name","password","email")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.user_name,"user_name")
        self.assertEqual(self.new_credentials.password,"password")
        self.assertEqual(self.new_credentials.email,"email")

        
if __name__ == '__main__':
    unittest.main()