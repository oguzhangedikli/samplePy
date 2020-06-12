a=int(input("1. sayı:\t"))
b=int(input("2. sayı:\t"))
c=int(input("3. sayı:\t"))

if (a>b and a>c):
    print("En büyük sayı",a)
elif(b>a and b>c):
    print ("En büyük sayı",b)
elif(c>a and c>b):
    print ("En büyük sayı",c)
else:
    print("Bütün sayılar aynı")
