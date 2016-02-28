#! usr/bin/env python3
# Find out how many times a number appears in a string
# Could do this:


string = 'yyxxxyx'  # x appears 4 times
x_count = 0
for i in string:
    if i == 'x':
        x_count += 1
print(x_count)


# of you could do it recursively
def count_x(str_):
    if str_ == '':
        return 0
    last_number = str_[-1]

    if last_number == 'x':
        return count_x(str_[:-1]) + 1
    return count_x(str_[:-1]) + 0

print(count_x(string))

"""
1. is str_ == 0? No? Proceed. Yes? go to 6
2. last_number = the last value in str_
3. if last_number == 'x' go to 4a
4a. add 1 to count
4b. call yourself again with the next value of str_ to the LEFT
5. go to 1
6. return 0
"""
