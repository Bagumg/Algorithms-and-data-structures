# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

import hashlib


def hash_search(string):
    hashes = set()
    cnt = 1
    while cnt < len(string):
        for i in range(0, len(string), 1):
            hashes.add(hashlib.sha1(string[i:i + cnt].encode('utf-8')).hexdigest())
        cnt += 1
    return len(hashes)


print(hash_search('sova'))
print(hash_search('papa'))
