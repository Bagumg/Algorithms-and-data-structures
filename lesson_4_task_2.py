import timeit
import cProfile
# import matplotlib.pyplot as plt


# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.


# Первый — с помощью алгоритма «Решето Эратосфена».

def sieve(n):
    # Максимальный делитель простого числа не может быть больше квадратного корня из этого числа.
    lst = list(range((n * n)))
    lst[1] = 0
    for i in lst:
        if i > 1:
            for j in range(i + i, len(lst), i):
                lst[j] = 0
    lst = [x for x in lst if x != 0]
    return lst[n]


x_1_1 = timeit.timeit('sieve(50)', number=100, globals=globals())
print(x_1_1)  # 0.09553841500000002
x_1_2 = timeit.timeit('sieve(100)', number=100, globals=globals())
print(x_1_2)  # 0.39448716800000005
x_1_3 = timeit.timeit('sieve(200)', number=100, globals=globals())
print(x_1_3)  # 1.6319871200000002
x_1_4 = timeit.timeit('sieve(400)', number=100, globals=globals())
print(x_1_4)  # 6.777547141000001
x_1_5 = timeit.timeit('sieve(800)', number=100, globals=globals())
print(x_1_5)  # 31.425262047000004


cProfile.run('sieve(50)')  # 1    0.001    0.001    0.001    0.001 lesson_4_task_2.py:11(sieve)
cProfile.run('sieve(100)')  # 1    0.004    0.004    0.004    0.004 lesson_4_task_2.py:11(sieve)
cProfile.run('sieve(200)')  # 1    0.014    0.014    0.017    0.017 lesson_4_task_2.py:11(sieve)
cProfile.run('sieve(400)')  # 1    0.060    0.060    0.069    0.069 lesson_4_task_2.py:11(sieve)
cProfile.run('sieve(800)')  # 1    0.291    0.291    0.329    0.329 lesson_4_task_2.py:11(sieve)


# Второй — без использования «Решета Эратосфена».

def prime_num(n):
    lst = [0, ]
    while True:
        for i in range(2, (n * n)):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lst.append(i)
                if len(lst) >= n + 1:
                    return lst[n]


x_2_1 = timeit.timeit('prime_num(50)', number=100, globals=globals())
print(x_2_1)  # 0.056527941
x_2_2 = timeit.timeit('prime_num(100)', number=100, globals=globals())
print(x_2_2)  # 0.249197893
x_2_3 = timeit.timeit('prime_num(200)', number=100, globals=globals())
print(x_2_3)  # 1.1641708
x_2_4 = timeit.timeit('prime_num(400)', number=100, globals=globals())
print(x_2_4)  # 5.440637249
x_2_5 = timeit.timeit('prime_num(800)', number=100, globals=globals())
print(x_2_5)  # 25.133132441

cProfile.run('prime_num(50)')  # 1    0.001    0.001    0.001    0.001 lesson_4_task_2.py:9(prime_num)
cProfile.run('prime_num(100)')  # 1    0.003    0.003    0.003    0.003 lesson_4_task_2.py:9(prime_num)
cProfile.run('prime_num(200)')  # 1    0.012    0.012    0.012    0.012 lesson_4_task_2.py:9(prime_num)
cProfile.run('prime_num(400)')  # 1    0.085    0.085    0.085    0.085 lesson_4_task_2.py:9(prime_num)
cProfile.run('prime_num(800)')  # 1    0.257    0.257    0.257    0.257 lesson_4_task_2.py:9(prime_num)


# Отрисовка графиков
# y_1 = 50
# y_2 = 100
# y_3 = 200
# y_4 = 400
# y_5 = 800
# data_x_1 = [x_1_1, x_1_2, x_1_3, x_1_4, x_1_5]
# data_y = [y_1, y_2, y_3, y_4, y_5]
# plt.plot(data_y, data_x_1)
# plt.title('sieve')
# plt.ylabel('Затраченное время')
# plt.xlabel('Размер списка')
# plt.figure()
# data_x_2 = [x_2_1, x_2_2, x_2_3, x_2_4, x_2_5]
# data_y = [y_1, y_2, y_3, y_4, y_5]
# plt.plot(data_y, data_x_2)
# plt.title('prime_num')
# plt.ylabel('Затраченное время')
# plt.xlabel('Размер списка')
# plt.show()
