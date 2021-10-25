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

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.full_name,"brenda andeso")
        self.assertEqual(self.new_user.user_name,"bree")
        self.assertEqual(self.new_user.email,"brendaandeso4@gmail.com") 

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Faith","fay","faith@gmail.com")
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Faith","fay","faith@gmail.com")
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()
