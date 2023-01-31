from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female" 
    FLUID = "fluid"

    def __str__(self):
        return self.value

class Author:
    
    def __init__(self, name: str, email: str, gender: Gender):
        self._name = name
        self._email = email
        self._gender = gender

    def get_name(self):
        return self._name
    
    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email 
    
    def get_gender(self):
        return str(self._gender)

    def __str__(self):
        return f"Author[name={self._name},email={self._email},gender={self._gender}]"

