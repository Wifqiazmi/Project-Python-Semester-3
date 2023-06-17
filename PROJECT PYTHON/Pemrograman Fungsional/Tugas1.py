print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

"""Nilai Maksimal"""

def maksimal(*n):
    if n:
        mn = n[0]
        for value in n [1:]:
            if value > mn:
                mn = value
                print (mn)
maksimal (2, 4, -8, 10)
maksimal (3, 5, 9, 0, 11)

"""Penjumlahan matriks"""

def matrix_mul(a,b):
    return [[sum(i+j for i, j in zip(r, c))
    for c in zip(*b)]for r in a]
a = [[2,1], [4,3]]
b = [[1,5], [1,2]]
c = matrix_mul(a, b)
print (c)

"""UNGUIDED 1"""
def rataan_21102277(bil1, bil2):
    rataan = (bil1 + bil2)/2
    print (rataan)
rataan_21102277(450, 1000)

"""UNGUIDED 2"""
def sum_21102277(bil1, bil2):
    total = 0
    for bil_hasil in list (range(bil1, bil2+1)):
        total = total + bil_hasil
    return total 

hasil = sum_21102277(1, 5)
print (hasil)

"""UNGUIDED 3"""
print (list (range (30)))
