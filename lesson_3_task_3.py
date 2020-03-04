# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

array = list(randint(0, 100) for i in range(randint(0, 10)))

index_min = array[0]
index_max = array[0]
for i in range(len(array)):
    if index_min > array[i]:
        index_min = array[i]
    if index_max < array[i]:
        index_max = array[i]
array[array.index(index_max)] = index_max
array[array.index(index_min)] = index_min
print(array)

