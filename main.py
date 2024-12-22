from penjumlahan import jumlah
from pengurangan import pengurangan
from panjangvektor import panjang
from dotproduct import dotproduct
from sudut import sudut
from unit import unit

while True:
    print("Operasi Pada vektor: \n0. Exit\n1. Penjumlahan\n2. Pengurangan\n3. Panjang\n4. Dot Product\n5. Sudut\n6. Unit")

    pilih = input("pilih : ")
    if pilih == "6" or pilih == "3":
        x = int(input("komponen X : "))
        y = int(input("Komopnen Y : "))
        A = [x, y]
    elif pilih == '0':
        print("Exiting...")
    else:
        x1 = int(input("Komponen X untuk Vektor 1 : "))
        y1 = int(input("Komponen y untuk Vektor 1 : "))
        x2 = int(input("Komponen X untuk Vektor 2 : "))
        y2 = int(input("Komponen y untuk Vektor 2 : "))
        A = [x1, y1]
        B = [x2, y2]

    if pilih == '1':
        C = jumlah(A, B)
        print(f'{A} + {B} = {C}')

    elif pilih == '2':
        C = pengurangan(A, B)
        print(f'{A} - {B} = {C}')

    elif pilih == '3':
        C = panjang(A[0], A[1])
        print(f'(({A[0]}^2 + {A[1]}^2)^0.5 = {C}')

    elif pilih == '4':
        C = dotproduct(A, B)
        print(f'{A[0]} x {B[0]} + {A[1]} x {B[1]} = {C}')

    elif pilih == '5':
        C = sudut(A, B)
        print(f'({A} x {B})/|{A}| x |{B}| = {C}')

    elif pilih == '6':
        C = unit(A[0], A[1])
        print(f'{A}/|A| = {C}')
    elif pilih == '0':
        break

    
