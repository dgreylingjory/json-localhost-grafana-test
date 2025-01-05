import time
import datetime

from modules.classes import *
from modules.functions import *

def main():
    while True:
        text = 'random_number'
        value = random_number(2)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') ##Timestamp format that wont kill json
        ##Takes random number, pairs with current timestamp and arbitrary label, turns it into a class instance
        data_class = Random_data(text, value, timestamp) 
        print(data_class) #To see its working
        time.sleep(2) ##Delay so console doesn't explode
        write_dict(data_class, 'db.json') ##Puts everything nicely into the json
main()