# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint

array = list(randint(-10, 10) for i in range(randint(0, 100)))

counter = 0
max_element = 0
for i in array:
    if i < 0:
        if abs(i) > counter:
            counter = abs(i)
            max_element = i
print(max_element, array.index(max_element))
