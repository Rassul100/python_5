#Первое задание
a = int(input("Введите число: "))

d = 0

for i in range(10, a + 1):
    d += i

print("Сумма чисел:", d)

#Второе задание
a = int(input("Введите число: "))

for d in range(0, a+1):
if d % 2 == 0:
    print(d)
    
#Третье задание
n = int(input("Введите число: "))

summa = 0

for i in range(0, n+1):
    if i % 3 == 0:
        summa += i


print("Сумма чисел:", summa)
