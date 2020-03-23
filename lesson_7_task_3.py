import random
from statistics import median


# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).


m = int(input('Введите длину массива: ' ))
arr = [random.randint(0, 100) for i in range(2 * m + 1)]


# Вариант 1
def median_find(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        for i in range(left, right, +1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1

        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return arr


mediana = median_find(arr)


# Не знаю, считается ли первый вариант вариантом с сортировкой, поэтому сделал ещё вариант, с гномьей сортировкой.
# Вариант 2
def gnome_sort(arr):
    cnt = 1
    while cnt < len(arr):
        if arr[cnt - 1] <= arr[cnt]:
            cnt += 1
        else:
            arr[cnt], arr[cnt - 1] = arr[cnt - 1], arr[cnt]
            cnt -= 1
    return arr


def median_find_2(arr):
    arr = gnome_sort(arr)
    return arr[len(arr) // 2]


print(f'Function median_find says -> медиана равна: {mediana[m]}')
print(f'Function median_find_2 says -> медиана равна: {median_find_2(arr)}')
print(f'Проверка на корректность встроенной функцией statistics -> median: {median(arr)}')