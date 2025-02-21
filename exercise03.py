"""
Exercise 3
Given a credit score score, assign a string value to another variable rating
based on the following scale:

[0, 580) --> Poor
[580, 670) --> Fair
[670, 740) --> Good
[740, 800) --> Very Good
[800, 850] --> Excellent
"""
score = 8
if 800 <= score:
    rating = 'Excellent'
elif 740 <= score:
    rating = 'Very Good'
elif 670 <= score:
    rating = 'Good'
elif 580 <= score:
    rating = 'Fair'
elif 0 <= score:
    rating = 'Poor'

print(f'A score of {score} yields a {rating} rating.')

