print('''
********************************

Kenar Hesaplama

********************************

''')

sekil=input("Üçgen mi Dörtgen mi hesaplanacak?\t")
if sekil == ("dörtgen"):
    a=int(input("Dörtgenin ilk kenarını giriniz:"))
    b=int(input("Dörtgenin ikinci kenarını giriniz:"))
    c=int(input("Dörtgenin üçüncü kenarını giriniz:"))
    d=int(input("Dörtgenin dördüncü kenarını giriniz:"))    
    if (a==b and b==c and a==d):
          print("Kare")
    elif(a==c and b==d):
          print ("Dikdörtgen")
    else:
          print ("Sıradan Dörtgen")

elif sekil== ("üçgen"):
    a=int(input("Üçgenin ilk kenarını giriniz:"))
    b=int(input("Üçgenin ikinci kenarını giriniz:"))
    c=int(input("Üçgenin ikinci kenarını giriniz:"))
    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a==b and a==c):
            print("Eşkenar Üçgen")
        elif ((a==b and a!=c)or(a==c and a!=b)or(b==c and b!=a)):
            print("İkizkenar üçgen")
        else:
            print("Çeşitkenar üçgen")
    else:
        print("Üçgen Belirtmiyor")
else:
     print("Geçersiz şekil...")
     
