import random
import string
import json 
import os

from modules.classes import *

def random_string(length): ##Create random string of certain length just for testing (currently unused)
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def random_number(length): ##Create random number of certain length to have a data point to monitor
    return random.randint(10**(length-1), 10**length-1)

def write_dict(class_instance, file_name): ##Uses class attribute to turn instance into a json dict then write to file
    ##Initialize the data structure if the file doesn't exist or is empty
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                data = json.load(file)
                ##Ensure 'metrics' is a list
                if not isinstance(data.get("metrics", []), list):
                    data["metrics"] = []  ##If 'metrics' is not a list, reset it to an empty list
            except json.JSONDecodeError:
                ##If the file is empty or invalid, start fresh
                data = {"metrics": []}
    else:
        ##If the file doesn't exist, initialize the structure
        data = {"metrics": []}

    ##Add the new data entry to the list under 'metrics'
    new_data = class_instance.to_dict()
    data['metrics'].append(new_data)

    ##Write the updated data back to the file
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)
        