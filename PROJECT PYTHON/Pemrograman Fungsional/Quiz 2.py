"""Quiz Nomor 1"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

bilangan_21102277 = range(10)
hasil_21102277 = list(map(lambda x: (x, x % 2 == 0), bilangan_21102277))
print(hasil_21102277)

"""Quiz Nomor 2"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

dict_a_21102277 = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
hasil_21102277 = list(filter(lambda x: x['name'] == 'python', dict_a_21102277))
print('output 1')
print(hasil_21102277)
print()

"""ATAU BISA JUGA DENGAN"""
hasil_21102277 = [x for x in dict_a_21102277 if x['name'] == 'python']
print('output 2')
print(hasil_21102277)
print()

"""Quiz Nomor 3"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

import itertools

bil_binner_21102277 = [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
for key_21102277, group_21102277 in itertools.groupby(bil_binner_21102277):
    print("Group {} -> {}".format(key_21102277, " ".join(map(str, group_21102277))))
    print()


"""Quiz Nomor 4"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()
        
def kalihkan(x, y):
    print(f'Bilangan : {x}, {y}')
    return x * y

from functools import partial

def kalihkan_21102277(x, y):
    print(f'Bilangan: {x}, {y}')
    return x * y

kalihkan4_21102277 = partial(kalihkan_21102277, 4)
kalihkan5_21102277 = partial(kalihkan_21102277, 5)

list_bil_21102277 = [1, 2, 3, 4]
list_bil_4x_21102277 = list(map(kalihkan4_21102277, list_bil_21102277))
print(list_bil_4x_21102277)
print()

list_bil_5x_21102277 = list(map(kalihkan5_21102277, list_bil_21102277))
print(list_bil_5x_21102277)
print()

"""Quiz Nomor 5"""
print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

berat_badan_21102277 = [120, 45, 75] 
tinggi_badan_21102277 = [1.80, 1.60, 1.55]

bmi = lambda b, t: b / t ** 2

bmi_list_21102277 = list(map(bmi, berat_badan_21102277, tinggi_badan_21102277))

for i in range(len(bmi_list_21102277)):
    if bmi_list_21102277[i] < 18.5:
        print(f"BMI:{bmi_list_21102277[i]:.2f} - Berat Badan Kurang")
    elif bmi_list_21102277[i] >= 18.5 and bmi_list_21102277[i] <= 22.9:
        print(f"BMI:{bmi_list_21102277[i]:.2f} - Berat Badan Normal")
    elif bmi_list_21102277[i] >= 23 and bmi_list_21102277[i] <= 29.9:
        print(f"BMI:{bmi_list_21102277[i]:.2f} - Berat Badan Berlebih")
    else:
        print(f"BMI:{bmi_list_21102277[i]:.2f} - Obestitas")
        print()

