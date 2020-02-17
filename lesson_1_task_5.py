# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
a = input()
b = input()
print(alphabet.index(a))
print(alphabet.index(b))
print(alphabet.index(b) - alphabet.index(a))
