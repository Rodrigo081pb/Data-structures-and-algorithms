"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


# TASK 2: Which telephone number spent the longest time on the phone
# during the period? Don't forget that time spent answering a call is
# also time spent on the phone.
# Solução Task2
time_spent = {}
for call in calls:
    caller, receiver, _, duration = call
    duration = int(duration)
    time_spent[caller] = time_spent.get(caller, 0) + duration
    time_spent[receiver] = time_spent.get(receiver, 0) + duration

max_number = max(time_spent, key=time_spent.get)
max_time = time_spent[max_number]
print(f"{max_number} spent the longest time, {max_time} seconds, on the phone during September 2016.")
# Print a message:
# "<telephone number> spent the longest time, <total time> seconds, on the phone during 
# September 2016.".


