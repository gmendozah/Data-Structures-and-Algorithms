"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
phone_code_prefix = set()
calls_in_bangalore = 0
total_from_bangalore = 0
bangalore_code = '(080)'

for call in calls:
    if call[0].startswith(bangalore_code):
        receiving = call[1]
        total_from_bangalore += 1

        if receiving.startswith(bangalore_code):  # calls to bangalore too
            calls_in_bangalore += 1

        if ' ' in receiving:  # mobile cases
            phone_code_prefix.add(receiving[:4])
        elif receiving[0].startswith('('):  # fixed phone case
            index = receiving.find(')')
            phone_code_prefix.add(receiving[1:index])
        elif (' ' not in receiving) and (not receiving.startswith('(')):  # telemarketer  case
            phone_code_prefix.add(receiving[1:3])

print("The numbers called by people in Bangalore have codes:")
print(*sorted(phone_code_prefix), sep='\n')

call_percentage_in_bangalore = calls_in_bangalore / total_from_bangalore * 100

print(
    F'{round(call_percentage_in_bangalore, 2)} percent of calls from fixed lines in Bangalore are calls to other '
    F'fixed lines in Bangalore.')

