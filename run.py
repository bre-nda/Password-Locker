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

def check_existing_credentials(user_name):
    '''
    Function that check if a credentials exists with that username and return a Boolean
    '''
    return Credentials.credentials_exist(user_name)

def check_existing_users(user_name):
    '''
    Function that check if a user exists with that user_name and return a Boolean
    '''
    return User.user_exist(user_name)



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
    print("cc - create a new account, dc - display various accounts, fc -find an account, del -delete credentials, ex -exit the  list ")

    short_code = input().lower()

    if short_code == 'cc':
        print("New Credentials")
        print("-"*10)

        print("username ...")
        user_name = input()

        print("password")
        password = input()

        print("email...")
        email = input()

        save_credentials(create_credentials(user_name,password,email))
        print ('\n')
        print(f"New User {user_name} {password} {email} created")
        print ('\n')

    elif short_code == 'dc':
        if display_credentials():
            print("Here is a list of all your login credentials")
        print('\n')

        for Credentials in display_credentials():
            print(f"{Credentials.user_name} {Credentials.password} {Credentials.email}.....")

            print('\n')
        else:
            print('\n')
            print("You dont seem to have any accounts saved yet")
            print('\n')

    elif short_code == 'fc':
        print("Enter the account credentials you want to search for")
        search_user_name = input()
        if check_existing_credentials(search_user_name):
            search_credentials = find_credentials(search_user_name)
            print(f"{search_credentials.user_name} {search_credentials.password}")
            print('-' * 20)

            print(f"user_name.......{search_credentials.user_name}")
            print(f"email.......{search_credentials.email}")
        else:
            print("That user does not exist")

    elif short_code == 'del':
        if del_credentials(create_credentials):
            print("choose credentials to delete")
            print('/n')
            for Credentials in del_credentials():
                print("delete credential")

        else:
            print('/n')
            print("cannot delete credentials")
            print('/n')

    elif short_code == "ex":
        print("Bye .......")
        break



if __name__ == '__main__':
  main()


