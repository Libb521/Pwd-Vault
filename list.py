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
	    # print("Use these codes to navigate : \n A/C-Create an Account \n Log-Log In \n Leave-Exit the list')
        print("Use these codes to navigate : cu - create a user a/c, du - display users, fu -find a user, cc - create credential, dc - display credential, fc - find credential, ex -exit the  list ")
		
        short_code = input('Enter a choice: ').lower().strip()
       
        if short_code == 'cu':
            print("welcome")
            print("-"*10)
            
            print("First name ...")
            name1 = input()

            print("name2...")
            name2 = input()

            print("Your password...")
            password = input()

            print("Email address...")
            email = input()

            save_users(create_user(name1,name2,password,email))
            print('\n')
            print(f"welcome {name1} {name2} created")
            print('\n')



