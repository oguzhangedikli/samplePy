kayitliOgrenciAdlari=['Fatma Ece MERCAN', 'Furkan PARMAKSIZ', 'Ahmet ÖZDEMİR']
istek=1
while istek!=0:

    print ('')
    print ('')
    print ('Menu:')
    print ('1 - Kayıtları Listele')
    print ('2 - Kayıtl Ekle')
    print ('3 - İlk Kayıtı Göster')
    print ('4 - Son Kayıtı Göster')
    print ('5 - Sıra no ile Kayıt Ara')
    print ('0 değeri - Programı Sonlandır...')
    istek=int(input('Tercihinizi giriniz:'))
    if istek==1:
        print ('')
        print ('KAYITLARIN LİSTESİ')
        print ('---------------------')
        i=0
        while i<len(kayitliOgrenciAdlari):
            print (kayitliOgrenciAdlari[i])
            i=i+1
    elif istek==2:
        print ('')
        print ('KAYIT EKLEME')
        print ('---------------------')
        eklenen=input('Eklemek istediğiniz Kayıtı giriniz: ')
        kayitliOgrenciAdlari.append(eklenen)
        print (eklenen+' isimli kayıt listeye eklendi...')
    elif istek==3:
        print ('')
        print ('LİSTEDEKİ İLK KAYIT')
        print ('---------------------')
        print (kayitliOgrenciAdlari[0])
    elif istek==4:
        print ('')
        print ('LİSTEDEKİ SON KAYIT')
        print ('---------------------')
        print (kayitliOgrenciAdlari[-1])
    elif istek==5:
        print ('')
        print ('KAYIT SIRASI ile ARAMA')
        print ('---------------------')
        goster=int(input('Listenin Kaçıncı üyesini görmek istiyorsunuz?'))
        print ('Listede '+str(goster)+'. inci sıradaki kayıt: '+kayitliOgrenciAdlari[goster-1])
    else:
        print('İsteğiniz üzerine program sonlandırıldı')
        break
