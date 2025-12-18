# Arbitrary Arguments, *args
def addition(*numbers):
    result = 0
    for num in numbers:
        result += num
    print(result)
    
# addition(1,2,3,4,5,6,7,8,9,10)
# def fullname(fname, lname):
#     print(f"your fullname is", end="")
#     print(f"{fname} {lname}")
# fullname(lname = "antara", fname = "jaka")
# def fullname(**fullname):
#     result = fullname.values()
#     print(" ".join(result))
# fullname(
#     fname = 'zaahid',
#     mname = 'azka',
#     lname = 'lobma'
# )
# def sayHello(name, message="Hello"):
#     print(f"{message}, {name}")
    
# sayHello("jaka")
# sayHello(
#     message = "assalamualaikum",
#     name = "indra"
# )