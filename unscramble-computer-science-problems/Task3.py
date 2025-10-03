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


# Solução Task3
codes = set()
from_bangalore = 0
bangalore_to_bangalore = 0
for call in calls:
    caller = call[0]
    receiver = call[1]
    if caller.startswith('(080)'):
        from_bangalore += 1
        # Fixed line
        if receiver.startswith('('):
            code = receiver.split(')')[0][1:]
            codes.add(code)
            if receiver.startswith('(080)'):
                bangalore_to_bangalore += 1
        # Mobile
        elif ' ' in receiver and receiver[0] in '789':
            codes.add(receiver[:4])
        # Telemarketing
        elif receiver.startswith('140'):
            codes.add('140')
print("The numbers called by people in Bangalore have codes:")
for code in sorted(codes):
    print(code)
if from_bangalore > 0:
    percent = (bangalore_to_bangalore / from_bangalore) * 100
    print(f"{percent:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


