""" Nomor 1"""

print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

list_2277 = []
for i_2277 in range(4, 30):
    if i_2277 % 2 == 0:
        list_2277.append(i_2277)

print(list_2277)

""" Nomor 2"""

print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

bilangan_2277 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
subA_2277 = []
for i in bilangan_2277:
    if i % 2 == 1:
        subA_2277.append(i)

subB_2277 = []
for i in bilangan_2277:
    if i % 3 == 0:
        subB_2277.append(i)

print(subA_2277)
print(subB_2277)
print()

""" Nomor 3"""

print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

print ("=> Kuadratkan list <=")
def list_2277 (number_2277):
    return number_2277 ** 2

angka = list(range(0,10))
hasil = [list_2277(x) for x in angka]
print(hasil)
print()

print ("=> Kuadratkan dict <=")
dict_2277 = list(range(0,10))
angka = {}
for x in dict_2277:
    angka[x] = x*x
print(angka)
print()

""" Nomor 4"""

print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

print("A")
inventory_2277 = {
    'Emas' : 500,
    'kantong' : ['Korek', 'Tali', 'Batu'],
    'Ransel' : ['Timpani', 'Pisau Belati', 'Kasur gulung', 'Roti']}
print (inventory_2277)
print()

print("B")
inventory_2277['Saku']= ['kerang', 'Bandeng', 'Berry', 'Rumput Laut']
print (inventory_2277)
print()

print("C")
inventory_2277['Ransel']= ['timpani', 'Pisau belati', 'Kasur gulung', 'roti'] 
inventory_2277['Ransel'].sort()
print (inventory_2277['Ransel'])
print()

print("D")
inventory_2277['Ransel']= ['timpani', 'Pisau belati', 'Kasur gulung', 'roti'] 
inventory_2277['Ransel'].remove('Pisau belati')
print (inventory_2277['Ransel'])
print()

print("E")
inventory_2277['Emas'] = {}
inventory_2277['Emas'] = 500
inventory_2277['Emas'] = 50
print(inventory_2277['Emas'])
print()

""" Nomor 5"""

print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

a_2277 =[10,20]
b = sum (a_2277)
c_2277 = [10,20,50,60]
d = sum (c_2277)
print("Jumlahkan", a_2277, b)
print("Jumlahkan", c_2277, d)
print()
