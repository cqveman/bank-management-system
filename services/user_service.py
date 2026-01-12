import json
from datetime import datetime

class UserService:
    def __init__(self):
        self.users: list = []

    def create_user(self, username, legal_name, date_of_birth,
                    gender, address, phone_number,
                    email, password_hash, accounts):

        with open('users.json', 'r') as f:
            self.users = json.load(f)

        # Check if username exists
        for user in self.users:
            if username == user.username:
                return False

        # Check if age is at leats 18
        age = date_of_birth - datetime.now()

        # Check if phone number is valid

        # Check if email exists
        for user in self.users:
            if email == user.email:
                return False

        return True