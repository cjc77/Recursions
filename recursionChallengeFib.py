#! usr/bin/env python3
# Recursively execute Fibonacci Sequence
import time

# The Recursion
####===================================
def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x - 1) + fib(x - 2)
####===================================

"""
0 -> 0
1 -> 1
2 -> 1 + 0 -> 1
3 -> 1 + 1 -> 2
4 -> 2 + 1 -> 3
5 -> 3 + 2 -> 5
6 -> 5 + 3 -> 8
7 -> 8 + 5 -> 13
etc.
if x == 0 return 0
if x == 1 return 1
otherwhise:
fib(x - 1) == the previous result
fib(x - 2) == the result previous to fib(x - 1)
Thus, fib(x - 1) + fib(x - 2) = the previous two results combined

"""

# Taking input and timing results
####===================================
inp_range = int(input("How many values into the Fibonacci sequence" +
                    " would you like to go?(enter as numeric character) "))
start = time.time()
for n in range(inp_range):
    print(fib(n))
time_taken = time.time() - start
if time_taken == 1:
    s = "second"
else:
    s = "seconds"
print("Time taken: ", time_taken, s)
####===================================
