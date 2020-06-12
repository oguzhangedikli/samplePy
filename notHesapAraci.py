print ('''
************************
PUAN HESAPLAMA ARACI

************************
''')

vize1=int(input("1. vizenin notunu giriniz:"))
vize2=int(input("2. vizenin notunu giriniz:"))
final=int(input("Final notunu giriniz:\t"))

toplam_not= vize1*30/100 + vize2*30/100 + final*40/100

if toplam_not >=90:
    print("AA")
elif toplam_not >=85:
    print("BA")
elif toplam_not >=80:
    print("BB")
elif toplam_not >=75:
    print("CB")
elif toplam_not >=70:
    print("CC")
elif toplam_not >=65:
    print("DC")
elif toplam_not >=60:
    print("DD")
elif toplam_not >=55:
    print("FD")
else:
    print("FF")
