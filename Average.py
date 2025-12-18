def calculate_average(*args):
    return sum(args) / len(args) if args else 0
print(f"Rata-rata dari (10, 20, 30) adalah: {calculate_average(10, 20, 30)}")
print(f"Rata-rata dari (5, 10, 15, 20, 25) adalah: {calculate_average(5, 10, 15, 20, 25)}")
print(f"Rata-rata dari (7, 12, 19, 3, 8, 10) adalah: {calculate_average(7, 12, 19, 3, 8, 10)}")
print(f"Rata-rata jika tidak ada angka: {calculate_average()}")