try:
    angka1 = int(input("masukan angka pertama"))
    angka2 = int(input("masukan angka kedua"))
    if angka1 ==0:
        print("error,angka pertama tdak boleh nol")
    else:
        print("tidak error")
except ValueError:
    print("input salah")