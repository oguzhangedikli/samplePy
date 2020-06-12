a=int(input("İlk Sayıyı Giriniz:"))
b=int(input("İkinic Sayıyı giriniz:"))

print("Değiştirilmeden önceki hali: {},{}".format(a,b))

a,b=b,a

print ("Değiştirildikten sonraki hali: {},{}".format(a,b))
