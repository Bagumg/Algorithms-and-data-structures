# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint

array = list(randint(0, 100) for i in range(randint(0, 10)))

index_min = array[0]
index_max = array[0]
for i in range(len(array)):
    if index_min > array[i]:
        index_min = array[i]
    if index_max < array[i]:
        index_max = array[i]

sum_arr = 0
if array.index(index_min) < array.index(index_max):
    for i in array[array.index(index_min) + 1: array.index(index_max)]:
        sum_arr += i
    else:
        for i in array[array.index(index_max) + 1: array.index(index_min)]:
            sum_arr += i
print(sum_arr)
