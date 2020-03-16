from collections import deque

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


# def hex_sum():
#     hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
#     # print(hex_list)
#     a = [i for i in input('Input first hex number: ').lower()]
#     b = [i for i in input('Input second hex number: ').lower()]
#     # print(a, b, sep='\n')
#     divider = len(a)
#     for i in range(len(a)):
#         divider -= 1
#         if a[i].isalpha():
#            a[i] = int((hex_list.index(a[i]) * (16 ** divider)))
#         else:
#             a[i] = int(a[i]) * (16 ** divider)
#
#     divider = len(b)
#     for i in range(len(b)):
#         divider -= 1
#         if b[i].isalpha():
#             b[i] = int((hex_list.index(b[i])) * (16 ** divider))
#         else:
#             b[i] = int(b[i]) * (16 ** divider)
#
#     decimal_a = sum(a)
#     decimal_b = sum(b)
#     decimal_sum = decimal_a + decimal_b
#
#     hex_s = decimal_sum
#     remainder = deque()
#     while hex_s > 16:
#         if hex_s % 16 >= 10:
#             remainder.appendleft(str(hex_list[hex_s % 16]))
#         else:
#             remainder.appendleft(str(hex_s % 16))
#         hex_s = hex_s // 16
#     if hex_s > 10:
#         remainder.appendleft(str(hex_list[hex_s]))
#     else:
#         remainder.appendleft(str(hex_s))
#     # print(a, b, sep='\n')
#     # print(decimal_a, decimal_b, sep='\n')
#     # print(decimal_sum)
#     # print(hex_s)
#     # print(remainder)
#     # print(list(remainder))
#     print(''.join(remainder).upper())
#
# hex_sum()


# Сильно длинное и не красивое решение получилось, решил разнести по функциям.
# Да и собственные отдельные функции конвертации десятичных чисел в шеснадцатиричные и обратно, не помешают.

def hex_to_decimal():
    hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    a = [i for i in input('Input hex number: ').lower()]

    # Для перевода шестнадцатеричного числа в десятичное необходимо его записать в виде многочлена,
    # состоящего из произведений цифр числа и соответствующей степени числа 16.
    # Например:
    # C4F = 12 * (16**2) + 4 * (16 ** 1) + 15 * (16 ** 0) = 3072 + 64 + 15 = 3151

    divider = len(a)
    for i in range(len(a)):
        divider -= 1
        if a[i].isalpha():
            a[i] = int((hex_list.index(a[i]) * (16 ** divider)))
        else:
            a[i] = int(a[i]) * (16 ** divider)

    return sum(a)


def decimal_to_hex(hex_by_me):
    hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    remainder = deque()
    while hex_by_me > 16:
        if hex_by_me % 16 >= 10:
            remainder.appendleft(str(hex_list[hex_by_me % 16]))
        else:
            remainder.appendleft(str(hex_by_me % 16))
        hex_by_me = hex_by_me // 16
    if hex_by_me > 10:
        remainder.appendleft(str(hex_list[hex_by_me]))
    else:
        remainder.appendleft(str(hex_by_me))

    return ''.join(remainder).upper()


print(decimal_to_hex(hex_to_decimal() + hex_to_decimal()))
print(decimal_to_hex(hex_to_decimal() * hex_to_decimal()))


# Нашел ещё вариант, как без hex() решить. Но тут о прокачке алгоритмического мышления тоже говорить не стоит.
# a = list(input('Input hex number: '))
# b = list(input('Input hex number: '))
#
# print(int(''.join(a), 16) + int(''.join(b), 16))
# print(int(''.join(a), 16) * int(''.join(b), 16))