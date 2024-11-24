from penjumlahan import jumlah
from pengurangan import 
from panjangvektor import panjangV
print("Operasi Pada vektor")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Panjang")

pilih = input("pilih : ")

x1 = int(input("componen X untuk Vektor 1 : "))
y1 = int(input("componen y untuk Vektor 1 : "))
x2 = int(input("componen X untuk Vektor 2 : "))
y2 = int(input("componen y untuk Vektor 2 : "))
A = [x1, y1]
B = [x2, y2]

if pilih == '1':
    C = jumlah(A, B)
    print(f'{A} + {B} = {C}')

elif pilih == '2':
    C = 

elif pilih == '3':
    C = panjangV(A, B)
    print(f'(({A}^2 + {B}^2)^0.5 = {C}')
    
