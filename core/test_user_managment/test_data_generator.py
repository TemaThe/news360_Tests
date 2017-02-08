import os
import time
import json

from core.test_user_managment import POSITIVE_STATIC_USER_DATA_FILE


def get_static_sing_in_user_data_for_positive_tests():
    with open(POSITIVE_STATIC_USER_DATA_FILE) as data_file:
       user_data_dict = json.load(data_file)
    user_data = user_data_dict.items()
    return user_data

def get_new_sing_up_user_data_for_positive_tests():
    with open(POSITIVE_STATIC_USER_DATA_FILE) as data_file:
       static_user_data_dict = json.load(data_file)
    user_data_dict = get_new_user_data_dict(static_user_data_dict)
    user_data = user_data_dict.items()
    return user_data


def get_new_user_data_dict(user_data):
    user_data_dict = dict()
    timestamp = get_str_timestamp()
    for k, v in user_data.items():
        key = getNewEmail(k, timestamp)
        user_data_dict[key] = v
    return user_data_dict

def get_str_timestamp():
    return str(int(time.time()))

def getNewEmail(k, timestamp):
    i = k.index('@')
    if "maximumlen" in k: #to avoid fail due too long email
        l = len(timestamp)
        key = k[l:i]
    else:
        key = k[:i]
    key += timestamp + k[i:]
    return key


def get_all_sing_in_user_data_for_positive_tests():
    static_user_data = get_static_sing_in_user_data_for_positive_tests()
    new_user_data = get_new_sing_up_user_data_for_positive_tests()
    user_data = static_user_data.extend(new_user_data)
    return user_data



def append_to_sign_in_json(email, password):
    fname = "positive_new_sign_in.json"
    entry = {email : password}
    a = []
    if not os.path.isfile(fname):
        a.append(entry)
        with open(fname, mode='w') as f:
            json_string = json.dumps(entry, indent=2)
            f.write(json_string)
    else:
        with open(fname) as feedsjson:
            feeds = json.load(feedsjson)

        feeds.update(entry)
        with open(fname, mode='w') as f:
            f.write(json.dumps(feeds, indent=2))