while True:
    cevap=input("Girilen 10 sayıdan en küçüğünü hesaplamak için Q, Çıkmak için W tuşuna basınız:\t")
    if cevap.upper()=="Q":
        a=int(input("1.Sayı:"))
        b=int(input("2.Sayı:"))
        c=int(input("3.Sayı:"))
        d=int(input("4.Sayı:"))
        e=int(input("5.Sayı:"))
        f=int(input("6.Sayı:"))
        g=int(input("7.Sayı:"))
        h=int(input("8.Sayı:"))
        ı=int(input("9.Sayı:"))
        i=int(input("10.Sayı:"))

        if a<b and a<c and a<d and a<e and a<f and a<g and a<h and a<ı and a<i:
            print("Girilen en küçük sayı: ",a)
        elif b<a and b<c and b<d and b<e and b<f and b<g and b<h and b<ı and b<i:
            print("Girilen en küçük sayı: ",b)
        elif c<a and c<b and c<d and c<e and c<f and c<g and c<h and c<ı and c<i:
            print("Girilen en küçük sayı: ",c)
        elif d<a and d<b and d<c and d<e and d<f and d<g and d<h and d<ı and d<i:
            print("Girilen en küçük sayı: ",d)
        elif e<a and e<b and e<c and e<d and e<f and e<g and e<h and e<ı and e<i:
            print("Girilen en küçük sayı: ",e)
        elif f<a and f<b and f<c and f<d and f<e and f<g and f<h and f<ı and f<i:
            print("Girilen en küçük sayı: ",f)
        elif g<a and g<b and g<c and g<d and g<e and g<f and g<h and g<ı and g<i:
            print("Girilen en küçük sayı: ",g)
        elif h<a and h<b and h<c and h<d and h<e and h<f and h<g and h<ı and h<i:
            print("Girilen en küçük sayı: ",h)
        elif ı<a and ı<b and ı<c and ı<d and ı<e and ı<f and ı<g and ı<h and ı<i:
            print("Girilen en küçük sayı: ",ı)
        else:
            print("Girilen en küçük sayı: {}",i)
    elif cevap.upper()=="W":
        print("İsteğiniz üzerine program sonlandırıldı")
        
        break
