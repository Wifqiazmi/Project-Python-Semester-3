"""Quiz Nomor 1"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

Titik_21102277 = [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'd'), ('c', 'a'), ('d', 'a'), ('d', 'b'), ('d', 'c')]
dict_titik_21102277 = {}

for elemen in Titik_21102277:
    if elemen[0] in dict_titik_21102277:
        dict_titik_21102277[elemen[0]].append(elemen[1])
    else:
        dict_titik_21102277[elemen[0]] = [elemen[1]]

print(dict_titik_21102277)
print()

"""Quiz Nomor 2"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

bilangan_21102277 = 20
faktor_21102277 = [1, 2, 4, 5, 10, 20]
hasil_21102277 = [x for x in faktor_21102277 if bilangan_21102277 % x == 0]
print(hasil_21102277)
print()


"""Quiz Nomor 3"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

from functools import reduce

def reduce_operator(f, data, init=0):
    return reduce(f, data, init)

def tambah_21102277(data_21102277):
    return reduce_operator(lambda x, y: x + y, data_21102277)

def kali_21102277(data_21102277):
    return reduce_operator(lambda x, y: x * y, data_21102277, 1)

print(tambah_21102277([1, 2, 3, 4, 5]))
print(kali_21102277([1, 2, 3, 4, 5]))
print()

"""Quiz Nomor 4"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
pelanggan_21102277 = [dict(id=1, total=200, kode_kupon='F20'), 
             dict(id=2, total=150, kode_kupon ='P30'), 
             dict(id=3, total=100, kode_kupon ='P50'), 
             dict(id=4, total=110, kode_kupon ='F15')]
discount_21102277 = {'F20': (0.0, 20.0), 
            'P30': (0.3, 0.0), 
            'P50': (0.5, 0.0), 
            'F15': (0.0, 15.0)}
            
for p in pelanggan_21102277:
    id = p['id']
    total_sebelum_21102277 = p['total']
    kode_kupon_21102277 = p['kode_kupon']
    diskon = discount_21102277[kode_kupon_21102277]
    if diskon[0] != 0:
        diskon = total_sebelum_21102277 * diskon[0]
    else:
        diskon = diskon[1]
        
    print(f" {id} {total_sebelum_21102277} {diskon}")
    print()

"""Quiz Nomor 5"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()
dict_nama_21102277= {0: 'Tono', 1: 'Tini', 2: 'Boby', 3: 'Ani', 4: 'Roni', 5: 'Rania'}
dict_filter_21102277 = dict(filter(lambda x: 'a' in x[1].lower(), dict_nama_21102277.items()))
print(dict_filter_21102277)


"""Quiz Nomor 6"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

a_21102277 = [1, 2, 3]
b_21102277 = [10, 20, 30]

result_21102271 = list(map(lambda x, y: x + y, a_21102277, b_21102277))
print(result_21102271)
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

"""Quiz Nomor 3"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

print("Output A")
bilangan_21102277 = [0,1,2,3,4,5,6,7,8,9,10,11,12]
print (bilangan_21102277[1:11:2])
print()
print("Output B")
print (bilangan_21102277[0:15:3])