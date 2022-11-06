#Modul_1, task 3
 x1 = float(input('Введите первое число: '))
 x2 = float(input('Введите второе число : '))
 max1 = (x1 > x2 ) * x1 + (x2 >= x1) * x2

 print ('Максимальное значение: ', max1)

 #Modul_2, task 2
x1 = int(input('Введите координату по горизонтали_1: '))
y1 = int(input('Введите координату по вертикали_1: '))
x2 = int(input('Введите координату по горизонтали_2: '))
y2 = int(input('Введите координату по вертикали_2: '))


if x1 == x2:
    print('YES')
elif y1 == y2:
    print('YES')
else: 
    print('NO')
