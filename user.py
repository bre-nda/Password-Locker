import pyperclip
class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] 

    def __init__(self,full_name,user_name,email):


        self.full_name = full_name
        self.user_name = user_name
        self.email = email

    user_list = [] 
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a username and returns a username that matches that username.

        Args:
            user_name: user_name to search for
        Returns :
            Credentials of person that matches the username.
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that takes in a username and returns a username that matches that username.

        Args:
            user_name: user_name to search for
        Returns :
            Credentials of person that matches the username.
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return True
        
        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls,user_name):
        user_found = User.find_by_user_name(user_name)
        pyperclip.copy(user_found.email)