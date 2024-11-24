from penjumlahan import jumlah
from pengurangan import pengurangan
from panjangvektor import panjang
from dotprocut import dotproduct
from sudut import sudut
from unit import unit

print("Operasi Pada vektor")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Panjang")
print("4. Dot Product")
print("5. Sudut")
print("6. Unit")

pilih = input("pilih : ")
def pick_1():
    x1 = int(input("componen X untuk Vektor 1 : "))
    y1 = int(input("componen y untuk Vektor 1 : "))
    x2 = int(input("componen X untuk Vektor 2 : "))
    y2 = int(input("componen y untuk Vektor 2 : "))
    A = [x1, y1]
    B = [x2, y2]

def pick_2():
    x = int(input("componen X untuk Vektor 1 : "))
    y = int(input("componen y untuk Vektor 1 : "))

if pilih == '1':
    pick_1()
    C = jumlah(A, B)
    print(f'{A} + {B} = {C}')

elif pilih == '2':
    pick_1()
    C = pengurangan(A, B)
    print(f'{A} - {B} = {C}')

elif pilih == '3':
    pick_1()
    C = panjang(A, B)
    print(f'(({A}^2 + {B}^2)^0.5 = {C}')

elif pilih == '4':
    pick_1()
    C = dotproduct(A, B)
    print(f'{A[0]} x {B[0]} + {A[1]} x {B[1]} = {C}')

elif pilih == '5':
    pick_1()
    C = sudut(A, B)
    print(f'({A} x {B})/|{A}| x |{B}| = {C}')

elif pilih == '6':
    pick_2()
    C = unit(x, y)
    
