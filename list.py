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

def generate_password():
    '''
    This helps return all saved contacts
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def create_credentials(name,credential,password,email)
