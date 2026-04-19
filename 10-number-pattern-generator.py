# Project: Number Pattern Generator
# Source: freeCodeCamp Python Certification
# Description: A function that generates a space-separated string of numbers from 1 to n with input validation.

def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        numbers_list = []
        for i in range(1, n + 1):
            numbers_list.append(str(i))
        return ' '.join(numbers_list)
    
print(number_pattern(4))
