# Print the same text (from previous task) in the following format:
# 1.
# Event: Workshop & Tutorial proposals due
# Date: November 21, 2019
# 2.
# Event: Notification of acceptance
# Date: December 1, 2019
# and so forth.

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

lines = text.split('\n')
for i, line in enumerate(lines, 1):
    print(f'{i}.')
    print(f'Event: {line.split(":")[0]}')
    print(f'Date: {line.split(":")[1]}')
    print()