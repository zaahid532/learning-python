# def countdown(number):
#     print(number)
#     if number == 0:
#         return
#     else:
#         countdown(number - 1)
        
# countdown(10)
def factorial(number):
    if number <= 1:
        return 1
    else:
        result = number * factorial(number - 1)
        return result
print(factorial(int(input('enter a number'))))