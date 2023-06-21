#!/usr/bin/python3
"task 5"
import json


def save_to_json_file(my_obj, filename):
    "placeholder"
    jsoned = json.dumps(my_obj)
    with open(filename, mode='w') as j_son:
        j_son.write(jsoned)
