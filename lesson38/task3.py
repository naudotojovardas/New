# text = '''Workshop & Tutorial proposals: November 21, 2019
# Notification of acceptance: December 1, 2019
# Workshop & Tutorial websites online: December 18, 2019
# Workshop papers: February 28, 2020
# Workshop paper notifications: March 27, 2020
# Workshop paper camera-ready versions: April 10, 2020
# Tutorial material due (online): April 10, 2020'''
 
# Task:
# Print a list of dates from this text.

import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

dates = re.findall(r'\w+ \d{1,2}, \d{4}', text)
print(dates)