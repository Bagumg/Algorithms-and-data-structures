import random


# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


def div_array(arr):
    if len(arr) <= 1:
        return arr
    middle = int(len(arr) / 2)
    left = div_array(arr[:middle])
    right = div_array(arr[middle:])
    return merge_arr(left, right)


def merge_arr(left, right):
    merged_arr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged_arr.append(left[0])
            left = left[1:]
        else:
            merged_arr.append(right[0])
            right = right[1:]
    if len(left) > 0:
        merged_arr += left
    if len(right) > 0:
        merged_arr += right
    return merged_arr


arr = [round(random.uniform(0, 50), 3) for i in range(20)]  # Округлил числа, для улучшения читаемости.
print(f'Исходный массив: {arr}')
print(f'Массив отсортирован методом слияния {div_array(arr)}')
