
ask_price = 100
if ask_price > 50:
    volume = 50
else:
    volume = 80

print(volume)
print()

ask_price = 100
volume = 50 if ask_price > 50 else 80
print(volume)
print('-'*80)


a = 10
b = 20
print(abs(10 - 20))
print()
distance = a-b if a >= b else b-a
print(distance)
print()

a = 20
b = 10
print(abs(10 - 20))
print()
distance = a-b if a >= b else b-a
print(distance)
print()

print('-'*80)


current_value = -999
running_total = 15000
running_count = 125

if current_value == -999:
    clean_value = 0
else:
    clean_value = current_value
running_total = running_total + clean_value
print(running_total)
print()

current_value = -999
running_total = 15000
running_count = 125
clean_value = 0 if current_value==-999 else current_value
running_total = running_total + clean_value
print(running_total)
print()

