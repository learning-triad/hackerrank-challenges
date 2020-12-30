#!/bin/python3
#
# https://www.hackerrank.com/challenges/python-loops/problem
#
# For all non-negative integers i < n, print i^2.
#
# Sample Input:
# 5
#
# Sample Output:
# 0
# 1
# 4
# 9
# 16

def generator(num):
    for i in range(num):
        yield square(i)


def square(num):
    return num*num


if __name__ == '__main__':
    n = int(input())
    for i in generator(n):
        print(i)
