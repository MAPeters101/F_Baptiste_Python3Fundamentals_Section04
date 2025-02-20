from lesson038 import account_enabled

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
print('-'*80)


account_enabled = True
balance = 1000
withdraw = 100_000

if account_enabled and withdraw <= balance:
    print('withdrawal authorized')
else:
    if not account_enabled:
        print('account disabled')
    else:
        print('insufficient funds')


print('-'*80)


account_enabled = True
balance = 1000
withdraw = 100_000

if not account_enabled:
    print('account disabled')
else:
    if withdraw > balance:
        print('insufficient funds')
    else:
        print('withdrawal authorized')


print('-'*80)


account_enabled = True
balance = 1000
withdraw = 100_000

if not account_enabled:
    print('account disabled')
elif withdraw > balance:
    print('insufficient funds')
else:
    print('withdrawal authorized')



