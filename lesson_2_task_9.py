# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

digit_one = input('Введите первое число: ')
digit_two = input('Введите второе число: ')
sum_one = 0
sum_two = 0
for i in digit_one:
    sum_one += int(i)
for i in digit_two:
    sum_two += int(i)
if sum_one > sum_two:
    print('Сумма цифр', digit_one, 'равна', sum_one)
else:
    print('Сумма цифр', digit_two, 'равна', sum_two)
