import pyperclip
import random

class Dets:
    '''
    Class Dets to create new Detail credentials
    '''

    dets_list = []

    def _init_(self,name,dets,password,email):

        self.name = name
        self.dets = dets
        self.password = password
        self.email = email

    