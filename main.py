from penjumlahan import jumlah
print("Operasi Pada vektor")
print("1. Penjumlahan")
print("2. Pengurangan")

pilih = input("pilih : ")

if pilih == '1':
    x1 = int(input("componen X untuk Vektor 1 : "))
    y1 = int(input("componen y untuk Vektor 1 : "))
    x2 = int(input("componen X untuk Vektor 2 : "))
    y2 = int(input("componen y untuk Vektor 2 : "))
    A = [x1, y1]
    B = [x2, y2]
    C = jumlah(A, B)
    print(f'{A} + {B} = {C}')