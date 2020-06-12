a=input("Bir sayı giriniz")
ciftsayi=0
for i in range (0,int(a),2):
    if (i%6!=0):
        ciftsayi=i+ciftsayi
        print(i)
print(ciftsayi)    
