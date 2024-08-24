
first = int(input('Введи число: '))
second = int(input('Введи число: '))
third = int(input('Введи число: '))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)