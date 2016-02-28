#! usr/bin/env python3
# Finds Median Value of random list in range of input

def if_even(x):
    global first
    if len(x) == 2:
        return (x[0] + x[1]) / 2
    if first:
        first = False
        return if_even(x[1:])
    elif not first:
        first = True
        return if_even(x[:-1])


def if_odd(x):
    global first
    if len(x) == 1:
        return float(x[0])
    if first:
        first = False
        return if_odd(x[1:])
    elif not first:
        first = True
        return if_odd(x[:-1])

L = [int(usr) for usr in input().split()]
first = True
if len(L) % 2 == 0:
    print(if_even(L))
elif len(L) % 2 == 1:
    print(if_odd(L))
else:
    print("Stop making up numbers!")
