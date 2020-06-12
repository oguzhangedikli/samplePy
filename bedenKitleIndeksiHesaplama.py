print('''
***********************

BEDEN KİTLE ENDEKSİ

***********************
''')

while 1:
    a= float(input("Metre cinsinden Boyunuz:"))
    b= int(input("Kilonuzu giriniz:"))
    kitle_endeks = b/a**2

    if (kitle_endeks < 18.5):
        print("Sonuclar\n")
        print("Boyunuz: {}\nKilonuz: {}\nBeden Kitle Endeksiniz:{}\nDurumunuz: {}".format(a,b,kitle_endeks,"Zayıf"))
    elif (kitle_endeks >=18.5 and kitle_endeks < 25):
        print("Sonuclar\n")
        print("Boyunuz: {}\nKilonuz: {}\nBeden Kitle Endeksiniz:{}\nDurumunuz: {}".format(a,b,kitle_endeks,"Normal"))
    elif (kitle_endeks >=25 and kitle_endeks < 30):
        print("Sonuclar\n")
        print("Boyunuz: {}\nKilonuz: {}\nBeden Kitle Endeksiniz:{}\nDurumunuz: {}".format(a,b,kitle_endeks,"Kilolu"))
    else:
        print("Sonuclar")
        print("Boyunuz: {}\nKilonuz: {}\nBeden Kitle Endeksiniz:{}\nDurumunuz: {}".format(a,b,kitle_endeks,"Obez"))
    c= str(input("Devam etmek için 'o' çıkmak için 'x' yazınız:"))
    if c == "x":
        break
