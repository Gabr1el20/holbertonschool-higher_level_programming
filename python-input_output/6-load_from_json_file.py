#!/usr/bin/python3
"Task 6"
import json


def load_from_json_file(filename):
    "Placeholder"
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
