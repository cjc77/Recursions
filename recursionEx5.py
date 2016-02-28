#! usr/bin/env python3
# Factorial Recursion
# 0! = 1
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# etc.


def factorial(x):
    if x in (0, 1):
        return 1
    return factorial(x - 1) * x

for x in range(10):
    print(factorial(x))
