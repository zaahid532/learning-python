pilihan = input("tentukan ganjil genap")
number =[1,2,3,4,5,6,7,8,9,10,11,12,13]
if pilihan == 'genap' or pilihan == 'even':
    print(f"menampilkan angka genap dari number")
    for i in number:
        if i % 2 == 0:
            print(i)
elif pilihan == 'ganjil' or pilihan == 'odd':
    print(f"menampilkan angka ganjil dari number")
    for i in number:
        if i % 2 != 0:
            print(i)
else:
    print('input nya salah')