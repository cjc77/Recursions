#! usr/bin/env python3
# An Example of Triangle Numbers
####### n = 0 -> 0
#       n = 1 -> 1
##      n = 2 -> 3
###     n = 3 -> 6
####    n = 4 -> 10
"""
PSEUDO
1. n == 0? No? Proceed. Yes? Go to step 3.
2a. call triangle_numbers(n - 1) i.e. triangle_numbers(3),
triangle_numbers(2), etc.
2b. + n
2c. go to step 1
3. You've reached BASE CASE x == 0. Return 0.

0 -> 0
1 -> 1
2 -> 3
3 -> 6
etc.
"""
def triangle_numbers(n):
    if n == 0:
        return 0
    return triangle_numbers(n - 1) + n

for n in range(20):
    print(triangle_numbers(n), "n =", n)
