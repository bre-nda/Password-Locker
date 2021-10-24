class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty contact list

    def __init__(self,user_name,password,email):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New contact first name.
            last_name : New contact last name.
            number: New contact phone number.
            email : New contact email address.
        '''
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credential_list
        '''

        Credentials.credential_list.append(self)
    
    def save_multiple_credentials(self):
        '''
        save_multiple_credentials method saves multiple credentials objects into credential_list
        '''
        Credentials.credential_list.append(self)
    
    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credential from the credential_list
        '''

        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a username and returns a username that matches that username.

        Args:
            user_name: user_name to search for
        Returns :
            Credentials of person that matches the username.
        '''

        for credentials in cls.credential_list:
            if credentials.user_name == user_name:
                return credentials