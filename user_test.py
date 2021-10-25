import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("brenda andeso","bree","brendaandeso4@gmail.com")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.full_name,"brenda andeso")
        self.assertEqual(self.new_user.user_name,"bree")
        self.assertEqual(self.new_user.email,"brendaandeso4@gmail.com") 


if __name__ == '__main__':
    unittest.main()
