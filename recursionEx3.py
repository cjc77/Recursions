#! usr/bin/env python3
def sum_digits(num):
    # Sums up digits of a number
    if num == 0:
        return 0
    return sum_digits(num // 10) + num % 10

print(sum_digits(111222))
print(sum_digits(989))
print(sum_digits(14))

"""
PSEUDO
1. num == 0? No? Proceed. Yes? Go to 3.
2a. returns num (minus first digit)(num // 10) into sum_digits()
2b. returns last digit of num (num % 10) & adds to running total
2c. go to step 1
3. You have hit the BASE CASE. Return 0.
"""
