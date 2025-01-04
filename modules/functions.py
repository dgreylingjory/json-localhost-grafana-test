import random
import string
import json 
import os

from modules.classes import *

def random_string(length): ##Create random string of certain length just for testing
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def random_number(length): ##Create random number of certain length just for testing
    return random.randint(10**(length-1), 10**length-1)

def write_dict(class_instance, file_name): ##Uses class attribute to turn instance into a json dict then write to file
     ##Convert the class instance to a dictionary
    data_dict = class_instance.to_dict()

    # Check if the file exists and contains data
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r+') as file:
            # Read the existing data (if any)
            existing_data = json.load(file)
            # Append the new dictionary to the existing list
            existing_data.append(data_dict)
            # Move to the beginning of the file
            file.seek(0)
            # Write the updated list of dictionaries back to the file
            json.dump(existing_data, file, indent=4)
    else:
        # If the file doesn't exist or is empty, start with a list containing the first dictionary
        with open(file_name, 'w') as file:
            json.dump([data_dict], file, indent=4)