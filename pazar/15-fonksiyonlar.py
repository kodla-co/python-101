# FONKSIYONA PARAMETRE GONDERME
# Fonksiyonlara parametre yani disardan bilgi gonderilerek o bilgi fonksiyon icinde kullanilabilir.

def islem(a,b,c):  
    print(a + b + c + 4)

islem(5,5,6)


# FONKSIYONDAN GERI BILGI GONDERME
# Bilgiyi fonksiyon icinde print ile yazdirmak yerine, fonksiyondan bilgiyi geri dondurerek fonksiyon disinda print ile bilgiyi ekrana yazdirabiliriz.

def islem(a):
    return a + 3

print(islem(3))

