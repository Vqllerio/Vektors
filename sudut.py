import math
def sudut(a,b):
    product = a[0]*b[0] + a[1]*b[1]
    panjang_a = a[0]**2 + a[1]**2
    panjang_A = panjang_a**0.5
    panjang_b = b[0]**2 + b[1]**2
    panjang_B = panjang_b**0.5
    product/(panjang_A*panjang_B)
    angle = product/(panjang_A*panjang_B)
    return math.degrees(math.acos(angle))

a = [3,2]
b = [2,1]

print(f"theta = {sudut(a,b)} degrees")