import json
import time
import datetime

from modules.classes import *
from modules.functions import *

def main():
    while True:
        text = random_string(4)
        value = random_number(2)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_class = Random_data(text, value, timestamp)
        print(data_class)
        time.sleep(1)
        write_dict(data_class, 'db.json')
main()