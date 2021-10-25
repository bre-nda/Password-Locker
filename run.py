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
    print("Hello Welcome to the Password Locker App...\n Please enter the following to proceed.\n ca --- Create a New Account  \n sa ---  Sign in to account  \n")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)

    fname = input("full_name")
    uname = input("user_name")
    email = input("email")

    while True:
        print("tp - Put your own password")
        password_Choice = input().lower().strip()
        if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
        else:
                print("Invalid password please try again")
    
    save_user(save_user(fname,uname,email))
    print("*" * 85)
    print(f"Hi {fname}, Your account has been created succesfully! here are more of your details email: {email}, user_name: {uname}")
    print("*" * 85)

    short_code == "sa"
    print("*" * 50)
    print("Enter your user_name,password and email to sign in:")
    print('*' * 50)
    uname = input("user_name ")
    password = input("password ")
    email = input("email")
    credentials= save_credentials(uname,password)
    if save_credentials == credentials:
            print(f"Hello {uname}.Welcome to the Password locker App")
            print('\n')

    while True:
        print("cc - Create a new credential \n dc - Display Credentials \n fc - Find credentials \n d - Delete Credential \n ex - Exit the app \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create new credential")
            print("."*20)
            print("user_name ....")
            uname = input().lower()
            print("Your Account user_name")
            uname = input()

            while True:
                print(" tp - To type you're password on your already existing account")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your password\n")
                    break
                else:
                    print("Invalid password please try again")

            save_credentials(create_credentials(uname,password,email))
            print('\n')
            print(f"Account Credentials for user_name: {uname} & Password: {password}, was created successfully") 
            print('\n')

        elif short_code == "dc":
            if display_credentials():
                print("Here's your list of accounts: ")

                print('*' * 30)
                print('_'*30)

            for credentials in display_credentials():
                    print(f"username:{uname}\n password:{password}")
                    print('_' * 30)
                    print('*' * 30)

            else:
                print("Sorry, we dont seem to find your credentials")

        elif short_code == "fc":
            print("Enter the handle you want to search for")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print(f"Name: {search_credential.user_name}")
                print('-' * 50)
                print(f"Username: {search_credential.user_name} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("The Credential does not exist")
                print('\n')

        elif short_code == "d":
            print("Enter the Account handle credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_" * 50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.user_name} successfully deleted!!!")
                print('\n')
            else:
                print("The Credential you want to delete does not exist")

        elif short_code == 'ex':
            print("Bye and Thanks for using our App.")
            break
        else:
            print("Didn't get that, please use the short codes")





if __name__ == '__main__':
  main()


