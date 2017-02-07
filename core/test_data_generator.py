import time

import json


def get_sing_in_user_data_for_positive_tests():
    with open('static_user_data.json') as data_file:
        user_data_dict = json.load(data_file)
    user_data = user_data_dict.items()
    return user_data

def get__sign_up_user_data_for_positive_tests():
    user_data = (
        [
            ('temamod@gmail.com', '132435'),
            ('tema812@gmail.com', '132435'),
        ]
    )
    return user_data

def generateNewUserEmail(self):
    timestamp = str(time.time())
    email = 'testASM' + timestamp + '@gmail.com'
    password = '132435'
    return email, password