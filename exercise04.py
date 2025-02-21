"""
Exercise 4
Given an elapsed time (in seconds), write code to set a variable magnitude
based on the following conditions:

if elapsed time is less than 1 minute, magnitude --> 'seconds'
if elapsed time is more than 1 minute, but less than 1 hour, magnitude --> 'minutes'
if elapsed time is more than 1 hour, but less than 1 day, magnitude --> 'hours'
if elapsed time is more than 1 day, but less than 1 week: magnitude --> 'days'
if elapsed time is more than 1 week, magnitude --> 'weeks'
"""

elapsed_time = 3601
MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
WEEK = DAY * 7

if elapsed_time > WEEK:
    magnitude = 'weeks'
elif elapsed_time > DAY:
    magnitude = 'days'
elif elapsed_time > HOUR:
    magnitude = 'hours'
elif elapsed_time > MINUTE:
    magnitude = 'minutes'
else:
    magnitude = 'seconds'

print(f'{elapsed_time} seconds will be {magnitude}.')




