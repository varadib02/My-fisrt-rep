import math


#bekeres
def bekerse():
    be=input("Kérek szöveget: ")
    szam=int(input("Kérek számot: "))
    #kiíras
    print(f"A bekért szöveg: {be}")

#gyök
def gyok_hatvanyozas():
    szam = 2
    gy=math.sqrt(szam)
    print(f"Gyöke {gy}")
#hatványozás
    menyivel=int(input("hatványozás (hányadikon): "))
    hatv=math.pow(szam,menyivel)
    print(f"{hatv}")

#fix elem bekérése
#listába tárolás
def lista():
    n=5
    lista = []
    for i in range(0,n):
        be_adat=input(f"Kérem az {i+1} elemet: ")
        #listához hozzáadás
        lista.append(be_adat)
    #kiírás adatonként, lista végéig 
    for i in range(len(lista)):
        print(lista[i])

