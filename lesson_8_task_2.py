from collections import Counter
from operator import attrgetter

# 2) Закодируйте любую строку по алгоритму Хаффмана.

# class Node:
#     def __init__(self, left, right, height):
#         self.height = height
#         self.right = right
#         self.left = left
#
#     def create_map(self, map):
#
# test_node = Node
#
#
#
# def haffman_encode(string):
#     cnt = Counter(string)
#     cnt_list = list(cnt.items())[::-1]
#     print(cnt_list)
#     test = [[] for i in range(len(cnt_list))]
#     nums = []
#     for i in range(len(cnt_list) - 1):
#         if cnt_list[i][1] == cnt_list[i + 1][1]:
#             test[i].append(cnt_list[i][0])
#             test[i].append(cnt_list[i + 1][0])
#             nums.append(cnt_list[i][1] + cnt_list[i + 1][1])
#     for i in test:
#         if not i:
#             test.remove(i)
#     print(test)
#     print(nums)
#     print(list(zip(test, nums)))

