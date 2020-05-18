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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_telemarketers = set()
outgoingCallsList = []
outgoingTextsList = []
receivingCallsList = []
receivingTextsList = []

for call in calls:
    outgoing = call[0]
    receiving = call[1]
    if outgoing not in outgoingCallsList:
        outgoingCallsList.append(outgoing)
    if receiving not in receivingCallsList:
        receivingCallsList.append(receiving)

for text in texts:
    outgoing = text[0]
    receiving = text[1]
    if outgoing not in outgoingTextsList:
        outgoingTextsList.append(outgoing)
    if receiving not in receivingTextsList:
        receivingTextsList.append(receiving)

for phoneNumber in outgoingCallsList:
    if phoneNumber not in receivingCallsList and phoneNumber not in receivingTextsList and phoneNumber not in outgoingTextsList:
        possible_telemarketers.add(phoneNumber)

print("These numbers could be telemarketers: ")
print(*sorted(possible_telemarketers), sep='\n')

