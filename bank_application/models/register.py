#!/usr/bin/python3
"""register model """
from models.base_model import BaseModel
from models import storage
import re


class Register(BaseModel):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.middle_name = ""
        self.age = 0
        self.sex = ""
        self.phone_number = ""
        self.password = ""
        self.email = ""
        self.user_name = "faith"
        super().__init__()

    def get_first_name(self):
        """function to get the users first name"""
        while True:
            self.first_name = input("enter first name: ").split(" ")
            self.first_name = self.first_name[0]
            if not self.first_name:
                print("please fill in this field")
            else:
                return self.first_name

    def get_last_name(self):
        """function to get users last name"""
        while True:
            self.last_name = input("enter last name: ").split(" ")
            self.last_name = self.last_name[0]
            if not self.last_name:
                print("please fill in this field")
            else:
                return self.last_name

    def get_age(self):
        """function to get users age """
        while True:
            try:
                self.age = int(input("enter your age: "))
                if not self.age:
                    print("please fill this field")
                elif self.age < 7:
                    print("sorry you are too young to register")
                    exit()
                else:
                    return self.age
            except ValueError as e:
                print("Invalid input: age must be an integer")

    def get_sex(self):
        """function to get users sex """
        while True:
            self.sex = input("Are you male or female: ")
            if self.sex.lower() not in ["male", "female"]:
                print("please enter male or female no spaces")
            else:
                return self.sex

    def get_phone_number(self):
        """function to get phone number"""
        while True:
            try:
                self.phone_number = input("Enter your phone number: ")
                self.phone_number = ''.join(filter(str.isdigit, self.phone_number))
                if len(self.phone_number) != 11:
                    raise ValueError
                else:
                    return self.phone_number
            except ValueError:
                print("Invalid phone number. Please enter a 11-digit number.")
    def get_email(self):
        """function that gets email """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        while True:
            self.email = input("enter email address: ")
            match = re.search(email_regex, self.email)
            if not match:
                print("please enter a valid email format: favour767@gmial.com")
            else:
                return self.email

    def get_password(self):
        """function to get Users password """
        while True:
            self.password = input("enter your password: ")
            if not self.password:
                print("please enter a passord")
            elif len(self.password) < 6:
                print("password cannot be less tham 6 characters")
            else:
                return self.password
    
    def confirm_password(self):
        """Function to confirm Users initial password"""
        while True:
            password = input("confirm password: ")
            if self.password != password:
                print("password did not match")
            else:
                print("password matched")
                return password
