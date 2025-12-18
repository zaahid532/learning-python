# student = {
#     "name" : "jaka",
#     "address" : "jakarta",
# }

# try:
#     print()
# except NameError:
#     print("stdent variabel is not defined")
# except:
#     print("An error occured")
# finally:
#     print("script has runs")
#     print("the program stopped")
print("i like python app")
print("=====================")
loop = int(input("enter a number:"))
if loop <= 1:
    raise Exception("number must be > 1")
else:
    for i in range(loop):
        print("i like python!")