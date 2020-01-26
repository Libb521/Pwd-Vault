#!/usr/bin/env python3.6
from credentials import Credentials

def create_credential(name1,name2,phone,email):
    '''
    This is to create a new credential
    '''
    new_cridential = Credential(name1,name2,phone,email)
    return new_credential 

def save_credentials(credential):
    '''
    This is to save the credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    This is to delete a credential
    '''
    credential.delete_credential()

def find_credential(password):
    '''
    This is to help search for and find a credential
    '''
    return Credentials.find_by_password(password)

def find_existing_credentials(password):
    '''
    This is to help in checking if a credential has been logged using the password
    '''
    return Credentials.credentials_exist(password)

def display_credentials():
    '''
    This helps return all saved contacts
    '''
    return Credentials.display_credentials()
