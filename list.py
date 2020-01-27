#!/usr/bin/env python3.6
import pyperclip
from credentials import Credentials

def create_user(name1,name2,phone,email):
    '''
    This is to create a new user
    '''
    new_user = User(name1,name2,phone,email)
    return new_user 

def save_user(user):
    '''
    This is to save the user
    '''
    user.save_user()

def del_user(user):
    '''
    This is to delete a user
    '''
    credential.delete_credential()

def find_user(password):
    '''
    This is to help search for and find a user
    '''
    return User.find_by_password(password)

def verify_user(password):
    '''
    This is to help in checking if a credential has been logged using the password
    '''
    checking_user = Credential.check_user(name1,password)
    return checking_user

def display_users():
    '''
    This shows saved users
    '''
    return User.display_users()

def generate_password():
    '''
    This helps return all saved contacts
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def create_credentials(name,credential,password,email):
    '''
    This is to create new user credentials
    '''
    new_credentials = Credentials(name,credential,password,email)
    return new_credentials

def save_credential(credential):
    '''
    This helps to save newly created credentials
    '''
    credential.save_credentials()

def display_credentials(name):
    '''
    This displays credentials saved by the user
    '''
    return credential.display_credentials(name)

def del_credentials(Credentials):
    '''
    This deletes the saved user credentials
    '''
    Credentials.delete_credentials()

def find_credentials(password):
    '''
    helps to find credentials using password
    '''
    return Credentials.find_by_password(password)

def check_existing_credentials(password):
    '''
    this helps to check if the credentials exist
    '''
    return credentials.credentials_exist(password)

def main():
    print(' ')
    print("Hi there, Welcome to the Password vault")
    user_name = input()

    while True:
        print(f'Hi {user_name}, Kindly select what you would like to do')
        print('\n')
        print("-"*60)
        print("Use these codes to navigate: \n ac-Create an Account \n log-Log In \n go-Exit")		
        short_code = input('Enter a choice: ').lower().strip()
        if short_code == 'go':
            break
        
        elif short_code == 'ac':
            print("-"*60)
            print(' ')
            print('Create a new account:')
            name1 = input('Your first name - ').strip()
            name2 = input('Your last name - ').strip()
            password = input('Enter your password - ').strip()
            email = input('Your email address - ').strip()

            save_user(create_user(name1,name2,password,email))
            print('\n')
            print(f"New account created for: {name1} {name2} created")
            print('\n')

        elif short_code == 'log':
            print("-"*60)
            print(' ')
            print('Welcome back, enter your account details to go on')
            user_name = input('Your first name - ').strip()
            password = input('Enter your password - ').strip()
            user_exists = verify_user(name1,password)
            if user_exists == user_name:
                print(" ")
                print(f'Welcome back {user_name}. choose an option to continue')
                print(' ')
                while True:
                    print("-"*60)
                    Print('Explore more: \n cr-Create a credentials \n dis-Display Credentials \n cp-Copy Password \n go-Exit')
                    short_code = input('Explore: ').lowercase().strip()
                    print("-"*60)
                    if short_code == 'go':
                        print(' ')
                        print(f'Have a nice day {user_name}')
                        break
                    elif short_code == 'cr':
                        print(' ')
                        print('Enter your credentials:')
                        site_name = input('Site name - ').strip()
                        account_name = input('Your account name - ').strip()
                        while True:
                            




