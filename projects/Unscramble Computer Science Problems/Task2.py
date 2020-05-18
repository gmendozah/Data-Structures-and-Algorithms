"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from datetime import datetime

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

dictionary = {}


# Set value in dictionary
def setDict(phoneNumber, duration):
    if dictionary.get(phoneNumber) is None:
        dictionary[phoneNumber] = duration
    else:
        dictionary[phoneNumber] = dictionary.get(phoneNumber) + duration


# this function returs true if the phone call belongs to a month and year period]
def callsBelongsToPeriod(phoneCall, month, year):
    date = datetime.strptime(phoneCall[2], '%d-%m-%Y %H:%M:%S')
    if date.month == month and date.year == year:
        return True
    else:
        return False


for call in calls:
    if callsBelongsToPeriod(call, 9, 2016):
        call_duration = int(call[3])
        setDict(call[0], call_duration)
        setDict(call[1], call_duration)

longest_call = None
total_time = 0

for call in dictionary:
    duration = dictionary[call]
    if duration > total_time:
        total_time = duration
        longest_call = call


print(F"{longest_call} spent the longest time, {total_time} seconds, on the phone during September 2016.")
