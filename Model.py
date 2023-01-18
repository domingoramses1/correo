"""https://www.pythontutorial.net/tkinter/tkinter-mvc/
/home/cir/Escritorio/cir/apuntes/devnet/mvc
modificado por Cirino Silva Tovar el 9 sep 2022
para que acepte el nombre y lo guarde
"""

import re

class Model:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        
    @property
    def email(self):
        return self.__email
        
    @property    
    def name(self):    
        return self.__name
        
    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    @name.setter
    def name(self, value):
        self.__name = value
        
    def save(self):
        """
        Save the email into a file
        :return:
        """
        with open('emails.txt', 'a') as f:
            f.write(self.__email + '\n')
            f.write(self.__name + '\n')
            
