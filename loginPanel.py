print('''
*******************************

KULLANICI ADI PANELİ

*******************************
''')

ogr_kullanıcı_adı="abc"
ogr_parola="123"

kullanıcıadı=input("Kullanıı adı:")
parola=input("Parola")

if ogr_kullanıcı_adı == kullanıcıadı and ogr_parola != parola:
    print("Parola Hatalı")

elif ogr_kullanıcı_adı != kullanıcıadı and ogr_parola == parola:
    print("Kullanıcı Adı hatalı")

elif ogr_kullanıcı_adı != kullanıcıadı and ogr_parola != parola:
    print("Kullanıcı adı ve Parola hatalı")
else:
    print("Sisteme Giriş yapıldı")
