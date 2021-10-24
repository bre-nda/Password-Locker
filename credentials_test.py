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
        self.new_credentials = Credentials("Bree","b1234","brendaandeso4@gmail.com")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.user_name,"Bree")
        self.assertEqual(self.new_credentials.password,"b1234")
        self.assertEqual(self.new_credentials.email,"brendaandeso4@gmail.com")
        
        
if __name__ == '__main__':
    unittest.main()