pembagian = lambda a,b: a / b if b != 0 else 'error tidak bisa dibagi dengan 0'
perkalian = lambda a,b: a*b
pengurangan = lambda a,b: a - b 
pertambahan = lambda a,b: a + b
angka1 = int(input('masukan nilai pertama'))
angka2 = int(input('masukan nilai kedua'))
print(f'pembagian {angka1} : {angka2} = ', pembagian(angka1,angka2))
print(f'perkalian {angka1} x {angka2} = ', perkalian(angka1,angka2))
print(f'pengurangan {angka1} - {angka2} = ', pengurangan(angka1,angka2))
print(f'pertambahan {angka1} + {angka2} = ', pertambahan(angka1,angka2))