#!/bin/python3
#
# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# 
# Read two integers from STDIN and print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def times(a, b):
    return a * b


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if a < 1 or a > 10**10 or b < 1 or b > 10**10:
        print("Not Applicable")
    else:
        print(add(a, b))
        print(minus(a, b))
        print(times(a, b))
