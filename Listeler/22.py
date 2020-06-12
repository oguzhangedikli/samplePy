kayitliOgrenciler=[[13027,'Fatma Ece','MERCAN','Vize',80],
                   [14011,'Furkan','PARMAKSIZ','Vize',80],
                   [14451,'Ahmet','ÖZDEMİR','Vize',100]]                  
kayitliOgrenciler.append([15014,'Dilek','DURMUŞ','Quiz I',100])
while 1:
    ogrNo=int(input('Öğrenci Numarasını Giriniz (çıkmak için 0 giriniz):'))
    if ogrNo!=0:
        for getir in kayitliOgrenciler:
            if ogrNo==getir[0]:
                print (getir[1]+''+getir[2]+' nin '+getir[3]+' notu:'+str(getir[4]))
                break
        else:
            print (str(ogrNo)+' nolu öğrencinin kayıtlı notu yok')
    else:
        print ('Kendi isteğiniz ile programı sonlandırdınız...')
        break
