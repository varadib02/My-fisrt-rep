import math

#bekeres
be=input("Kérek szöveget")
szam=int(input("Kérek számot"))
#kiíras
print(f"A bekért szöveg: {be}")
#gyök
gy=math.sqrt(szam)
print(f"Gyöke {gy}")
#hatványozás
menyivel=int(input("hatványozás (hányadikon): "))
hatv=math.pow(szam,menyivel)
print(f"{hatv}")
