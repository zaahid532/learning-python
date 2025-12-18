# def cap_name(name):
#     return name.capitalize()
# names = ['andi', 'benny', 'dodi']
# proper_names = []
# for name in names:
#     proper_names.append(cap_name(name))
# print(proper_names)
# proper_names = map(cap_name, name)
# print(proper_names)
# print(list(proper_names))
# numbers = range(1,10)
# def is_even(n):
#     return n % 2 == 0
# even_numbers = filter(is_even, numbers)
# print(even_numbers)
# print(list(even_numbers)
from functools import reduce
def addition(number1, number2):
    return number1 + number2
number_list = range(1,11)
x = reduce(addition, number_list)
print(x)