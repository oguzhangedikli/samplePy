print("""
*****************************

Hesap Makinesi Programı

İşlemler;

1. İşlem Toplama

2. İşlem Çıkarma

3. İşlem Çarpma

4. İşlem Bölme

*****************************
""")

a=int(input("Bir sayı giriniz:"))
b=int(input("İkinci sayıyı giriniz:"))

işlem = input("İşlemi giriniz:")

if işlem == "1":
    print("{} ile {} sayısının toplamı {} sayısıdır.".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} sayılarının farkı {} sayısıdır.".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {} sayısının çarpımı {} sayısıdır.".format(a,b,a*b))
elif işlem == "4":
    print("{} ile {} sayısının bölümü {} sayısıdır.".format(a,b,a/b))
else:
    print("İşlem Türünü yanlış seçtiniz")
    


































































































































































