# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов: '))
digits = 0
counter = 1
for i in range(n):
    counter = counter / 2
    digits += counter
print(digits)
