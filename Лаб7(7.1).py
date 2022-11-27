string=input("Введіть символи: ")
d = {'Літери': 0, 'Цифри': 0}
for i in string:
    if i.isalpha():
        d['Літери'] += 1
    elif i.isdigit():
        d['Цифри'] += 1
print("Цифр",d['Цифри'])
print("Літери",d['Літери'])