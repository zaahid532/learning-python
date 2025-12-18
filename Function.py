# def nyfunction():
#     print("this is a custom function")
    
# nyfunction()
# def num1to100():
#     numbers = list(range(1,101))
#     print(numbers)
# num1to100()
# def sayhello(name):
#     print(f"hello, {name}")
    
# name = "jaka"
# sayhello(name)
# def num1to100(mulai, akhir,):
#     number = list(range(mulai, akhir,))
#     print(number)
# nilai1 = int(input('masukan nilai untuk mulai :'))
# nilai2 = int(input('masukan nilai untuk akhir'))
# num1to100(nilai1, nilai2)
# def addition(num1, num2):
#     result = num1 + num2
#     return f"{num1} + {num2} = {result}"
# print(addition(15,17))
def addition(num1, num2):
    result = num1 + num2
    return f"{num1} + {num2} = {result}"
number = int(input("enter a number to addition"))
loop = int(input("enter how many loops"))
for i in range(1,loop+1):
    print(addition(number,i))