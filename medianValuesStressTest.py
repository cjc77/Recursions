#! usr/bin/env python3
# Finds Median Value of input

import random, numpy


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
    print(x)
    if len(x) == 1:
        return float(x[0])
    if first:
        first = False
        return if_odd(x[1:])
    elif not first:
        first = True
        return if_odd(x[:-1])

usr = int(input("How many digits?: "))
response = True
first = True
while response:
    L = [random.randrange(usr) for x in range(usr)]
    L.sort()
    print(L)
    if len(L) % 2 == 0:
        print("My function:", if_even(L))
        print("Numpy:", numpy.median(numpy.array(L)))
        if if_even(L) != numpy.median(numpy.array(L)):
            print("Error")
            break
    elif len(L) % 2 == 1:
        print("My function:", if_odd(L))
        print("Numpy:", numpy.median(numpy.array(L)))
        if if_odd(L) != numpy.median(numpy.array(L)):
            print("Error")
            break
