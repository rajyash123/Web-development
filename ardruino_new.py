# # zero to one knapsack problem that we need calculate
#
# def knapsack(size, wt, val, n):
#     '''
#     :param size: list of item
#     :param wt: weight of each item
#     :param val: weight of the knapsack
#     :param n: no. of item
#     :return:
#     '''
#
#     # return the maximum value that can be put in a knapsack of capacity of n
#     k = [[0 for x in range(size+1)] for x in range(n+1)]
#
#
#     # for loop for i and i represent the index or the rows for the table
#
#     for i in range(n+1):
#         for w in range(n+1):             # in this w stands for the column
#             if i == 0 or w == 0:         # true when the column and rows are 0
#                 k[i][w] = 0
#             elif wt[i-1] <= w:           # true when the weight of object is less than the column numbers
#                 k[i][w]= max(size[i] + k[i-1][w-wt[i-1]], k[i-1][w])
#             else:                        # this oppsite to the second condition
#                 k[i][w] = k[i-1][w]
#
#     return k[n][size]
#
#
#
# p = {12,13,14,15,16,66}
# wt = {4,5,6,9,7,1}
# val = 34
# n = len(p)
# a = knapsack(p,wt, val, n)
# print(a)

# we are printing the methods for recursion and making sure that everything works as it is

# def func1(n):
#     a = n
#     if a > 0:
#         print(a)
#         func1(a-1)
# x = 5
# func1(x)

# reverse of the above function
#
# def func2(n):
#
#     b = n
#     if b > 0:
#         func2(b - 1)
#         print(b)
#
# y = 6
# func2(y)

# lis = [10,23,34,5,4,56,7,8,56,7,6,8]
#
# def func(n):
#
#

# def foo(n, sum):
#     k=0
#     j=0
#     if n == 0:
#         return 0
#     else:
#         k = n % 10
#         j = n /10
#         sum = sum+k
#         foo(j,sum)
#         print(k)
#
# a = 2048
# sum = 0
#
# foo(a, sum)
# print(sum)


a = (1,2,3,4,5,6,7)

