import unittest
from credentials import Credentials
import pyperclip

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

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credential_list = []
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credential_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("hope","hopp","hope@gmail.com")
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credential from our credential list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("hope","hopp","hope@gmail.com") 
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()
            self.assertEqual(len(Credentials.credential_list),1)

    def test_find_credential_by_user_name(self):
        '''
        test to check if we can find a user by  their username and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Kevin","kevo","kevin@gmail.com")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_user_name("Kevin")

        self.assertEqual(found_credentials.user_name,test_credentials.user_name)        

    def test_credentials_exist(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Kevin","kevo","kevin@gmail.com")
        test_credentials.save_credentials()

        credentials_exist = Credentials.credentials_exist("Kevin")

        self.assertTrue(credentials_exist)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all users credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found credentials
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_email("bree")

        self.assertEqual(self.new_credentials.email,pyperclip.paste())



if __name__ == '__main__':
    unittest.main()