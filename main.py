import json
import os
import time

from validators import *

users = [   ]

fileName = 'users.json'
if os.path.exists(fileName) and os.path.getsize(fileName) > 2:
    with open(fileName, 'r') as f:
        users = json.load(f)

def saveToJson(fName):
    with open(fName, 'w') as f:
        json.dump(users, f, indent=2)

def waitingAnimation(message, seconds, option=1):
    symbols = []
    if option == 1:
        symbols = [
            '▒▒▒▒▒▒▒▒▒▒ 0%', '██▒▒▒▒▒▒▒▒ 20%', '████▒▒▒▒▒▒ 40%',
            '██████▒▒▒▒ 60%', '████████▒▒ 80%', '██████████ 100%'
        ]
    elif option == 2:
        symbols = ['○', '◔', '◑', '◕', '●']
    elif option == 3:
        symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    print()
    for i in symbols:
        print(f'\r{message} {i}', end='')
        time.sleep(seconds)
    print('\n')

while True:
    print('*──────────────────Central Bank of Yemen──────────────────*')
    print('If you already have an account please enter login')
    print('If you do not have an account enter register')

    choice = input('>> ').strip().lower()

    # REGISTER
    if choice == 'register':
        print('\n#────────Sign-up────────#')
        print('Please fill in your personal information: ')

        # User Input
        fullName = input('Full Name: ').strip().title()
        dateOfBirth = input('Date of Birth (dd-mm-yyyy): ').strip()
        gender = input('Gender: ').strip().capitalize()
        job = input('Job: ').strip().title()
        address = input('Address (building #, Street Name, Neighbourhood, City-Postal Code): ').strip()
        phoneNum = input('Phone number (+967): ').strip()
        email = input('Email (example@gmail.com): ').strip()

        waitingAnimation('Validating Information', 1)

        # Validations
        fullName = validate(fullName, nameValidator, 'Invalid Full Name. Only alphabetic characters allowed, try again:')
        dateOfBirth = validate(dateOfBirth, dofValidator, 'Invalid Date of Birth. Only integer values allowed in the formatB of "dd-mm-yyyy", try again:')
        gender = validate(gender, genderValidator, 'Invalid Gender. Enter either male or female:')
        job = validate(job, jobValidator, 'Invalid Job. Only alphabetic characters allowed, try again:')
        address = validate(address, addressValidator, 'Invalid Address. Please use this format "building #, Street Name, Neighbourhood, City-Postal Code":')
        phoneNum = validate(phoneNum, phoneValidator, 'Invalid Phone Number. Omit +967 and enter 9 digits counting from "7":')
        email = validate(email, emailValidator, 'Invalid Email. Please use this format "example@gmail.com":')

        username = input('Username: ').strip()
        waitingAnimation('Checking Availability', 1, 3)
        username = validate(username, usernameValidator, '✘ Username is taken. Please try again:')

        password = input('Password: ')
        waitingAnimation('Validating Password', 1, 3)
        password = validate(
            password,
            passwordValidator,
            'Invalid Password. must be at least 8 characters long, contain at least one number, and include no spaces. Try again:'
        )

        users.append(
            {
                'username': username,
                'full name': fullName,
                'date of birth': dateOfBirth,
                'gender': gender,
                'job': job,
                'address': address,
                'phone number': phoneNum,
                'email': email,
                'balance': 0.0
            }
        )

        saveToJson(fileName)

        waitingAnimation('Registering User', 1, 2)
        print('Sign-up successful, your id is ' + str(len(users)))

    elif choice == 'login':
        ...
    else:
        print('Invalid Input. Please try again.\n')