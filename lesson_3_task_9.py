# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [[], [], [], []]
for i in range(0, 4):
    for j in range(0, 4):
        matrix[i].append(int(input('Введите число: ')))

maximum_matrix = [max(i) for i in matrix]
print(max(maximum_matrix))
