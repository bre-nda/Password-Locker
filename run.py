#!/usr/bin/env python3.6
from credentials import Credentials
from user import User

def create_credentials(uname,password,email):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(uname,password,email)
    return new_credentials

def create_user(fname,uname,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,uname,email)
    return new_user

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def save_user(user):
    '''
    Function to save user credentials
    '''
    user.save_user()

def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_credentials(user_name):
    '''
    Function that finds a user by user_name and returns the credentials
    '''
    return Credentials.find_by_user_name(user_name)

def find_user(user_name):
    '''
    Function that finds a user by user_name and returns the user credentials
    '''
    return Credentials.find_by_user_name(user_name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
   print("Hello Welcome to Password Locker App. What is your user_name?")
   user_name = input()
   print(f"Hello {user_name}. Choose an option below?")
   print('\n')

   while True:
    print("cc - create a new account, dc - display various accounts, fc -find an account, ex -exit the  list ")

    short_code = input().lower()

    if short_code == 'cc':
        print("New User")
        print("-"*10)

        print ("full name ....")
        full_name = input()

        print("username ...")
        user_number = input()

        print("email...")
        email = input()




if __name__ == '__main__':
  main()


