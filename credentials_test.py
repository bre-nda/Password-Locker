import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("bree","bren","brendaandeso4@gmail.com") 

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.user_name,"bree")
        self.assertEqual(self.new_credentials.password,"bren")
        self.assertEqual(self.new_credentials.email,"brendaandeso4@gmail.com") 

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credential list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),1)


if __name__ == '__main__':
    unittest.main()