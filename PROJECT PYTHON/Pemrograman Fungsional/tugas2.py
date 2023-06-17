"""Tugas Nomor 1"""

print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

topping_tersedia_21102277 = ["Keju", "Daging Sapi", "Sosis", "Bawang Bombai", "Ayam Barbeque", "Jamur"] 
topping_request_21102277 = ["Jamur", "Keju", "French Fries"]
 
for x in topping_tersedia_21102277:
    if x == "Jamur":
        print("Topping", x,"Ditambahkan.")
for i in topping_request_21102277:
    if i == "French Fries": 
        print("Topping", i, "tidak tersedia.")
for a in topping_tersedia_21102277:
    if a == "Keju":
        print("Topping", a, "Ditambahkan.")
        print("Selesai, pesanan pizza anda!")

"""Tugas Nomor 2"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

user_aktif21102277 = set (('a', 'b', 'd'))
user_baru21102277 = set (('b', 'c', 'd', 'e'))

print ("Penambahan pada user : ")
hasil_4 = user_baru21102277.difference(user_aktif21102277)
finaly_4 = list(hasil_4)
print(finaly_4)

print ("Pengapusan pada user : ")
hasil_3 = user_aktif21102277.difference(user_baru21102277)
finaly_2 = list(hasil_3)
print(finaly_2)

print ("Daftar user yang tidak berubah : ")
hasil_2 = user_aktif21102277.intersection(user_baru21102277)
finaly_1 = list(hasil_2)
print(finaly_1)

"""Tugas Nomor 3"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

lst_21102277 = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
lst2_21102277 = ["Hello word"]
lst3_21102277 = [lst_21102277, lst2_21102277]
print ("A. ", lst3_21102277)
x_21102277 = lst3_21102277
x_21102277 = set()
print ("B. ", type (x_21102277))

"""Tugas Nomor 4"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

listku_21102277 = [i for i in range (4, 30 +1)]
print ('listku')

bil_genap = []

for bil in listku_21102277:
    if bil % 2 == 0:
        bil_genap.append(bil)
print (format(', '.join([str(bil) for bil in bil_genap])))

"""Tugas Nomor 5"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

bil_biner_21102277 = int(input('masukan bilangan : '))
print()
print('angka desimal dari biner', bil_biner_21102277, end= '')

bil_desimal_21102277 = 0
i = 1
while (bil_biner_21102277 !=0):
    digit = bil_biner_21102277 % 10
    bil_desimal_21102277 = bil_desimal_21102277 + (digit*i)
    i = i*2;
    bil_biner_21102277 = bil_biner_21102277 // 10

print(' =',bil_desimal_21102277)
print()

"""Tugas Nomor 6"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

biodata_21102277 = { 'trojan' : '111-222-333', 'spam' : '444-55-111'}
for data_21102277 in biodata_21102277 :
    print(data_21102277, ' : ', biodata_21102277[data_21102277])

"""Tugas Nomor 7"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

bilangan_21102277 = int(input("masukan bilangan : "))
print("nilai absolute dari", bilangan_21102277, " Adalah ",
abs(bilangan_21102277))
print()
