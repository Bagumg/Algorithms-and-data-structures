import random
import timeit

# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).


def bubble_sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def bubble_sort_upgraded(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - j - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


arr = [random.randint(-100, 100) for i in range(10)]

print(f'Исходный массив: {arr}')
print(f'Массив отсортирован по убыванию методом пузырька {bubble_sort(arr)}')
print(f'Массив отсортирован по убыванию улучшенным методом пузырька {bubble_sort_upgraded(arr)}')

# print(timeit.timeit('bubble_sort(arr)', number=100, globals=globals()))  # 19.416797800999998 arr на 1000 элементов
# print(timeit.timeit('bubble_sort_upgraded(arr)', number=100, globals=globals()))  # 8.737221936000001 arr на 1000 элементов
