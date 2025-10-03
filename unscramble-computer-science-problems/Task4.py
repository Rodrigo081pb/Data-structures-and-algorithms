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

# Solução Task4
outgoing_calls = set(call[0] for call in calls)
incoming_calls = set(call[1] for call in calls)
send_texts = set(text[0] for text in texts)
receive_texts = set(text[1] for text in texts)

possible_telemarketers = outgoing_calls - incoming_calls - send_texts - receive_texts
print("These numbers could be telemarketers:")
for number in sorted(possible_telemarketers):
    print(number)

