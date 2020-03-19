import sys
from random import randint

array_1 = list(randint(1, 100) for i in range(100))  # Список из 100 случайных чисел


def show_info(obj):
    res = []
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                res.append(sys.getsizeof(key))
                res.append(sys.getsizeof(value))
        elif not isinstance(obj, str):
            for item in obj:
                res.append(sys.getsizeof(item))
    else:
        res.append(sys.getsizeof(obj))
    return sum(res)


# Вариант 1
def change_arr_indexes(array):
    res = 0
    res += sys.getsizeof(res)
    res += sys.getsizeof(array)
    array_min = array[0]
    res += sys.getsizeof(array_min)
    array_max = array[0]
    res += sys.getsizeof(array_max)
    for i in range(len(array)):
        res += sys.getsizeof(i)
        if array_min > array[i]:
            array_min = array[i]
        if array_max < array[i]:
            array_max = array[i]
    array[array.index(array_max)] = array_max
    array[array.index(array_min)] = array_min
    print(f'Total size of variables in change_arr_indexes function is {res} bytes')
    return array


def change_arr_indexes_2(array):
    res = 0
    res += show_info(res)
    res += show_info(array)
    array_min = array[0]
    res += show_info(array_min)
    array_max = array[0]
    res += show_info(array_max)
    for i in range(len(array)):
        res += show_info(i)
        if array_min > array[i]:
            array_min = array[i]
        if array_max < array[i]:
            array_max = array[i]
    array[array.index(array_max)] = array_max
    array[array.index(array_min)] = array_min
    print(f'Total size of variables in change_arr_indexes_2 function is {res} bytes')
    return array


def change_arr_indexes_3(array):
    res = 0
    array_min = array[0]
    array_max = array[0]
    for i in range(len(array)):
        res += show_info(i)
        if array_min > array[i]:
            array_min = array[i]
        if array_max < array[i]:
            array_max = array[i]
    array[array.index(array_max)] = array_max
    array[array.index(array_min)] = array_min
    for variable in locals():
        res += show_info(variable)
    print(f'Total size of variables in change_arr_indexes_3 function is {res} bytes')
    return array


# Вариант 2
def change_arr_indexes_4(array):
    res = 0
    res += sys.getsizeof(res)
    res += sys.getsizeof(array)
    array[array.index(max(array))], array[array.index(min(array))] = min(array), max(array)
    print(f'Total size of variables in change_arr_indexes_4 function is {res} bytes')
    return array


def change_arr_indexes_5(array):
    res = 0
    array[array.index(max(array))], array[array.index(min(array))] = min(array), max(array)
    for variable in locals():
        res += sys.getsizeof(variable)
    print(f'Total size of variables in change_arr_indexes_5 function is {res} bytes')
    return array


def change_arr_indexes_6(array):
    res = 0
    array[array.index(max(array))], array[array.index(min(array))] = min(array), max(array)
    for variable in locals():
        res += show_info(variable)
    print(f'Total size of variables in change_arr_indexes_6 function is {res} bytes')
    return array


# Вариант 3
def change_arr_indexes_7(array):
    res = 0
    array_min = sorted(array)[0]
    array_max = sorted(array, reverse=True)[0]
    array[array.index(max(array))], array[array.index(min(array))] = array_min, array_max
    res += sys.getsizeof(array)
    res += sys.getsizeof(res)
    res += sys.getsizeof(array_min)
    res += sys.getsizeof(array_max)
    print(f'Total size of variables in change_arr_indexes_7 function is {res} bytes')
    return array


def change_arr_indexes_8(array):
    res = 0
    array_min = sorted(array)[0]
    array_max = sorted(array, reverse=True)[0]
    array[array.index(max(array))], array[array.index(min(array))] = array_min, array_max
    res += show_info(array)
    res += show_info(res)
    res += show_info(array_min)
    res += show_info(array_max)
    print(f'Total size of variables in change_arr_indexes_8 function is {res} bytes')
    return array


def change_arr_indexes_9(array):
    res = 0
    array_min = sorted(array)[0]
    array_max = sorted(array, reverse=True)[0]
    array[array.index(max(array))], array[array.index(min(array))] = array_min, array_max
    for variable in locals():
        res += sys.getsizeof(variable)
    print(f'Total size of variables in change_arr_indexes_9 function is {res} bytes')
    return array


change_arr_indexes(array_1)
change_arr_indexes_2(array_1)
change_arr_indexes_3(array_1)
change_arr_indexes_4(array_1)
change_arr_indexes_5(array_1)
change_arr_indexes_6(array_1)
change_arr_indexes_7(array_1)
change_arr_indexes_8(array_1)
change_arr_indexes_9(array_1)


# OS Windows 7 Microsoft Windows [Version 6.1.7601]
# Python 3.7.0

# Total size of variables in change_arr_indexes function is 3860 bytes
# Total size of variables in change_arr_indexes_2 function is 5676 bytes
# Total size of variables in change_arr_indexes_3 function is 2796 bytes
# Total size of variables in change_arr_indexes_4 function is 1008 bytes
# Total size of variables in change_arr_indexes_5 function is 106 bytes
# Total size of variables in change_arr_indexes_6 function is 0 bytes
# Total size of variables in change_arr_indexes_7 function is 1068 bytes
# Total size of variables in change_arr_indexes_8 function is 2884 bytes
# Total size of variables in change_arr_indexes_9 function is 222 bytes


# Вывод:
# Сделал сначала варианты с ручным сбором с помощью sys.getsizeof().
# Затем решил немного переработать функцию, которую писали на вебинаре и её помощью посчитать использование памяти.
# Третьим моим вариантом была попытка автоматического сбора информации с помощью locals() и vars().
# В итоге у меня, по каждому решению получили различные данные.
# Много думал
# Явно что-то не учёл, например с помощью locals(), при итерации в цикле, учитывается только "вес" одной переменной,
# пришлось в ручную дописывать "костыль", что не есть гуд.
# Запутался окончательно, не знаю, какой из вариантов верный и есть ли он у меня, вообще. Буду ждать разбора ДЗ.

# P.S. Чисто логически, вариант с ручным сбором должен быть самым верным, но, опять же, есть шанс упусть переменную.
# Исходя из этого вариант №2 потребляет меньше всех ресурсов, а т.к. как раз этот вариант, при выполнении ДЗ №4
# оказался ещё и самым быстрым, то хочется верить, что хоть тут я не ошибся.
