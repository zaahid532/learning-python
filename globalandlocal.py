# x = "global"
# def foo():
#     print('x inside:',x)
# foo()
x = "global"
def foo():
    global x
    y = "local"
    x = x*2
    print(x)
    print(y)
foo()