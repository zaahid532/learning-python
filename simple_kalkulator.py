print("welcome to simple kalkulator")
print("===========================")
def pertambahan(num1, num2):
    result = num1 + num2
    return f'{num1} + {num2} = {result}'
def pengurangan(num1, num2):
    result = num1 - num2
    return f'{num1} - {num2} = {result}'
def perkalian(num1, num2):
    result = num1 * num2
    return f'{num1} * {num2} = {result}'
def pembagian(num1, num2):
    result = num1 / num2
    return f'{num1} / {num2} = {result}'
operator = int(input('pilih operator 1,+ 2,- 3,* 4,/'))
number1 = int(input('masukan nilai 1:'))
number2 = int(input('masukan nilai 2:'))
if operator == 1:
    print(f'hasil dari {pertambahan(number1,number2)}')
elif operator == 2:
    print(f'hasil dari {pengurangan(number1,number2)}')
elif operator == 3:
    print(f'hasil dari {perkalian(number1,number2)}')
elif operator == 4:
    print(f'hasil dari {pembagian(number1,number2)}')