# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

x = input('Введите число: ')
print(x[::-1])
print(str(int(x) % 10) + str((int(x) % 100) // 10) + str((int(x) % 1000) // 100) + str(int(x) // 1000))
