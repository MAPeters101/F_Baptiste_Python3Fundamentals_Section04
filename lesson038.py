
if 1 < 2:
    print('1 is less than 2')

if 1 > 2:
    print('1 is greater than 2')

if 1 < 2:
    print('block - line 1')
    print('block - line 2')
    print('block - line 3')
print('next line')
print()

if 1 > 2:
    print('block - line 1')
    print('block - line 2')
    print('block - line 3')
print('next line')
print()
print('-'*80)

if 1 < 2:
    print('1 is less than 2')
else:
    print('1 is not less than 2')

print()


if 1 > 2:
    print('1 is less than 2')
else:
    print('1 is not less than 2')

print()
print('-'*80)


account_enabled = True
balance = 1000
withdraw = 100

if account_enabled and withdraw <= balance:
    print('authorized')
else:
    print('not authorized')


account_enabled = True
balance = 1000
withdraw = 100_000

if account_enabled and withdraw <= balance:
    print('authorized')
else:
    print('not authorized')


account_enabled = True
balance = 1000
withdraw = 100_000

if account_enabled and withdraw <= balance:
    print('authorized')
else:
    if not account_enabled:
        print('account disabled')
    else:
        print('insufficient funds')


account_enabled = False
balance = 1000
withdraw = 100

if account_enabled and withdraw <= balance:
    print('authorized')
else:
    if not account_enabled:
        print('account disabled')
    else:
        print('insufficient funds')






