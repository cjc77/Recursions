#! usr/bin/env python3
# An Example of Recursion
def double(x):
    """
    decrements x by 1 and adds 2 to running total
    """
    if x == 0:
        return 0
    return double(x - 1) + 2

print(double(4))

"""
PSEUDO:
1. is your x == 0? If NO, proceed to 2a. If YES, proceed to 3.
2a. call this function again but with x - 1 i.e. double(3), double(2), ...
2b. add 2 to your running total
2c. Go back to 1 with new info
3. x == 0? return 0.


4 -> 2
3 -> 2
2 -> 2
1 -> 2
0 -> 0
"""
