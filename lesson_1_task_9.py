# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
    print(num_1, 'среднее')
elif num_1 < num_2 < num_3 or num_3 < num_2 < num_1:
    print(num_2, 'среднее')
else:
    print(num_3, 'среднее')
