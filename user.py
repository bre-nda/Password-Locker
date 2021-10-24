class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] 

    def __init__(self,full_name,user_name,email):

      # docstring removed for simplicity

        self.full_name = full_name
        self.user_name = user_name
        self.email = email