
grade = 72
if grade >= 90:
    print('Passed with distinction')
else:
    if grade >= 70:
        print('Passed')
    else:
        print('Failed')

print('-'*80)


grade = 72
if grade >= 90:
    print('Passed with distinction')
elif grade >= 70:
    print('Passed')
else:
    print('Failed')

print('-'*80)


grade = 72
if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(letter_grade)


