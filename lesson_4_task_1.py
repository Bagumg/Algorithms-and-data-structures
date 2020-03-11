import timeit
import cProfile
# import matplotlib.pyplot as plt
from random import randint

# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом
# (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.


# Решил взять задачу с заменой элементов списка из прошлого ДЗ. Максимальный и минимальный надо поменять местами.
# Списки генерируем сразу, один на всех, для чистоты эксперимента.
array_1 = list(randint(1, 100) for i in range(100))  # Список из 100 случайных чисел
array_2 = list(randint(100, 1000) for i in range(1000))  # Список из 1000 случайных чисел
array_3 = list(randint(1000, 10000) for i in range(10000))  # Список из 10000 случайных чисел
array_4 = list(randint(10000, 1000000) for i in range(100000))  # Список из 100000 случайных чисел
array_5 = list(randint(1000000, 10000000) for i in range(1000000))  # Список из 1000000 случайных чисел


# Вариант 1
def change_arr_indexes(array):
    array_min = array[0]
    array_max = array[0]
    for i in range(len(array)):
        if array_min > array[i]:
            array_min = array[i]
        if array_max < array[i]:
            array_max = array[i]
    array[array.index(array_max)] = array_max
    array[array.index(array_min)] = array_min
    return array


# После вашего рассказа решил тоже попробовать график построить. На нём хорошо видно линейную сложность алгоритма.
x_1_1 = timeit.timeit('change_arr_indexes(array_1)', number=100, globals=globals())
print(x_1_1)  # 0.0016864239999998532
x_2_1 = timeit.timeit('change_arr_indexes(array_2)', number=100, globals=globals())
print(x_2_1)  # 0.019349903999999807
x_3_1 = timeit.timeit('change_arr_indexes(array_3)', number=100, globals=globals())
print(x_3_1)  # 0.17533690300000027
x_4_1 = timeit.timeit('change_arr_indexes(array_4)', number=100, globals=globals())
print(x_4_1)  # 1.7849231350000005
x_5_1 = timeit.timeit('change_arr_indexes(array_5)', number=100, globals=globals())
print(x_5_1)  # 18.640757935

cProfile.run('change_arr_indexes(array_1)')  # 1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:15(change_arr_indexes)
cProfile.run('change_arr_indexes(array_2)')  # 1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:15(change_arr_indexes)
cProfile.run('change_arr_indexes(array_3)')  # 1    0.001    0.001    0.001    0.001 lesson_4_task_1.py:15(change_arr_indexes)
cProfile.run('change_arr_indexes(array_4)')  # 1    0.078    0.078    0.088    0.088 lesson_4_task_1.py:15(change_arr_indexes)
cProfile.run('change_arr_indexes(array_5)')  # 1    0.721    0.721    0.797    0.797 lesson_4_task_1.py:15(change_arr_indexes)


# Вариант 2
def change_arr_indexes_2(array):
    array[array.index(max(array))], array[array.index(min(array))] = min(array), max(array)
    return array


x_1_2 = timeit.timeit('change_arr_indexes_2(array_1)', number=100, globals=globals())
print(x_1_2)  # 0.0016080309999999542
x_2_2 = timeit.timeit('change_arr_indexes_2(array_2)', number=100, globals=globals())
print(x_2_2)  # 0.014758699999999791
x_3_2 = timeit.timeit('change_arr_indexes_2(array_3)', number=100, globals=globals())
print(x_3_2)  # 0.13533001899999997
x_4_2 = timeit.timeit('change_arr_indexes_2(array_4)', number=100, globals=globals())
print(x_4_2)  # 1.3154382409999998
x_5_2 = timeit.timeit('change_arr_indexes_2(array_5)', number=100, globals=globals())
print(x_5_2)  # 12.978738815

cProfile.run('change_arr_indexes(array_1)')  # 1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:16(change_arr_indexes)
cProfile.run('change_arr_indexes(array_2)')  # 1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:16(change_arr_indexes)
cProfile.run('change_arr_indexes(array_3)')  # 1    0.002    0.002    0.002    0.002 lesson_4_task_1.py:16(change_arr_indexes)
cProfile.run('change_arr_indexes(array_4)')  # 1    0.016    0.016    0.019    0.019 lesson_4_task_1.py:16(change_arr_indexes)
cProfile.run('change_arr_indexes(array_5)')  # 1    0.161    0.161    0.178    0.178 lesson_4_task_1.py:16(change_arr_indexes)


# Вариант 3
def change_arr_indexes_3(array):
    array_min = sorted(array)[0]
    array_max = sorted(array, reverse=True)[0]
    array[array.index(max(array))], array[array.index(min(array))] = array_min, array_max
    return array


x_1_3 = timeit.timeit('change_arr_indexes_2(array_1)', number=100, globals=globals())
print(x_1_3)  # 0.0014761000000000912
x_2_3 = timeit.timeit('change_arr_indexes_2(array_2)', number=100, globals=globals())
print(x_2_3)  # 0.013502486000000147
x_3_3 = timeit.timeit('change_arr_indexes_2(array_3)', number=100, globals=globals())
print(x_3_3)  # 0.13206692199999992
x_4_3 = timeit.timeit('change_arr_indexes_2(array_4)', number=100, globals=globals())
print(x_4_3)  # 1.4237265780000001
x_5_3 = timeit.timeit('change_arr_indexes_2(array_5)', number=100, globals=globals())
print(x_5_3)  # 14.931298278999998

cProfile.run('change_arr_indexes(array_1)')  # 1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:16(change_arr_indexes)
cProfile.run('change_arr_indexes(array_2)')  # 1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:16(change_arr_indexes)
cProfile.run('change_arr_indexes(array_3)')  # 1    0.002    0.002    0.002    0.002 lesson_4_task_1.py:16(change_arr_indexes)
cProfile.run('change_arr_indexes(array_4)')  # 1    0.016    0.016    0.017    0.017 lesson_4_task_1.py:16(change_arr_indexes)
cProfile.run('change_arr_indexes(array_5)')  # 1    0.166    0.166    0.212    0.212 lesson_4_task_1.py:16(change_arr_indexes)


# Вывод:
# Все три алгоритма получились линейными, при увеличении размера списка в 10 раз,
# время работы функции увеличивалось в 10 раз. Мой вариант с перебором списка оказался самым медленным и ресурсоёмким.
# Вариант номер два оказася самым быстрым, думаю из-за встроенных функций min и max, также там нет сортировки списка.
# Для наглядности решил сделать четвёртый вариант, с сортировкой пузырьком, который представлен ниже.
# При сортировке пузырьком время увеличивалось квадратично, т.е. при увеличении размера списка в 10 раз,
# время работы функции увеличивалось в 100 раз.


# Предыдущие варианты оказались все с линейными сложностями, решил отсортировать список пузырьком,
# который имет сложность O(n**2). Размеры списков и количество "прогонов" timeit пришлось сократить в 10 раз,
# т.к. время увеличивается пропорционально и несколько месяцев ждать резутата не очень хочется.

# array_1 = list(randint(1, 100) for i in range(10))
# array_2 = list(randint(100, 1000) for i in range(100))
# array_3 = list(randint(1000, 10000) for i in range(1000))
# array_4 = list(randint(10000, 1000000) for i in range(10000))
# array_5 = list(randint(1000000, 10000000) for i in range(100000))


# def change_arr_indexes_4(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     array_min = array[0]
#     array_max = array[-1]
#     array[array.index(array_max)] = array_min
#     array[array.index(array_min)] = array_max
#     return array
#
#
# x_1_4 = timeit.timeit('change_arr_indexes_4(array_1)', number=10, globals=globals())
# print(x_1_4)  # 0.00020114799999992883
# x_2_4 = timeit.timeit('change_arr_indexes_4(array_2)', number=10, globals=globals())
# print(x_2_4)  # 0.010013805000000042
# x_3_4 = timeit.timeit('change_arr_indexes_4(array_3)', number=10, globals=globals())
# print(x_3_4)  # 1.0006986640000002
# x_4_4 = timeit.timeit('change_arr_indexes_4(array_4)', number=10, globals=globals())
# print(x_4_4)  # 105.834587513
# x_5_4 = timeit.timeit('change_arr_indexes_4(array_5)', number=10, globals=globals())
# print(x_5_4)  # 10801.517089549
#
#
# cProfile.run('change_arr_indexes_4(array_1)')  # 1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:15(change_arr_indexes)
# cProfile.run('change_arr_indexes_4(array_2)')  # 1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:15(change_arr_indexes)
# cProfile.run('change_arr_indexes_4(array_3)')  # 1    0.001    0.001    0.001    0.001 lesson_4_task_1.py:15(change_arr_indexes)
# cProfile.run('change_arr_indexes_4(array_4)')  # 1    0.078    0.078    0.088    0.088 lesson_4_task_1.py:15(change_arr_indexes)
# cProfile.run('change_arr_indexes_4(array_5)')  # 1    0.721    0.721    0.797    0.797 lesson_4_task_1.py:15(change_arr_indexes)


# Отрисовка графиков. На всякий случай закоментировал, вдруг matplotlib не установлен.

# data_x_1 = [x_1_1, x_2_1, x_3_1, x_4_1, x_5_1]
# data_y_1 = [len(array_1), len(array_2), len(array_3), len(array_4), len(array_5)]
# plt.plot(data_y_1, data_x_1)
# plt.title('change_arr_indexes')
# plt.ylabel('Затраченное время')
# plt.xlabel('Размер списка')
# plt.figure()
# data_x_2 = [x_1_2, x_2_2, x_3_2, x_4_2, x_5_2]
# plt.plot(data_y_1, data_x_2)
# plt.title('change_arr_indexes_2')
# plt.ylabel('Затраченное время')
# plt.xlabel('Размер списка')
# plt.figure()
# data_x_3 = [x_1_3, x_2_3, x_3_3, x_4_3, x_5_3]
# plt.plot(data_y_1, data_x_3)
# plt.title('change_arr_indexes_3')
# plt.ylabel('Затраченное время')
# plt.xlabel('Размер списка')
# plt.figure()
# data_x_4 = [x_1_4, x_2_4, x_3_4, x_4_4, x_5_4]
# plt.plot(data_y_1, data_x_4)
# plt.title('change_arr_indexes_3')
# plt.ylabel('Затраченное время')
# plt.xlabel('Размер списка')
# plt.show()
