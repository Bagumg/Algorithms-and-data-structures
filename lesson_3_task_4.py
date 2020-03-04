# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

array = list(randint(0, 6) for i in range(randint(0, 10)))

frequent = 0
counter = 0
for i in array:
    if array.count(i) > counter:
        frequent = i
        counter = array.count(i)
print(array)
print(frequent)
