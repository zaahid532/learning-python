x = ["apel","jeruk","semangka","pir","anggur"]
def foo():
    global x
    y = ["wortel","bayam","kol","brokoli","ubi"]
    x = x*2
    print(x)
    print(y)
    
foo()