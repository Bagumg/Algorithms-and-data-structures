# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import randint

array = list(randint(0, 100) for i in range(randint(0, 100)))
two_minimums = [min(array)]
array.pop(array.index(min(array)))
two_minimums.append(min(array))

index_min = [array[0]]
for i in range(len(array)):
    if index_min[-1] >= array[i]:
        index_min.append(array[i])

print(array)
print(index_min[-2:])
