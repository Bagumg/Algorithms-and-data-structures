# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint

guesses_taken = 0
n = int(input('Введите верхнее число диапазона: '))
k = int(input('Сколько попыток желаете использовать?: '))


number = randint(1, n)

while guesses_taken <= k:
    print('Угадайте, какое число я загадал')
    guess = input()
    guess = int(guess)
    guessesTaken = guesses_taken + 1
    if guess < number:
        print('Загаданное число больше')
    elif guess > number:
        print('Загаданное число меньше')
    elif guess == number:
        print('Вы угадали')
    if guessesTaken == k:
        print('Попытки закончились')
