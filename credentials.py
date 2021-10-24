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