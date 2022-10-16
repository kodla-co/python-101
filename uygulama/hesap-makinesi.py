print("HESAP MAKINESI")

def toplama(a,b):
    return a + b

def cikarma (a,b):
    return a - b

def carpma(a,b):
    return a * b

def bolme(a,b):
    return a / b

print("Hangi islemi yapmak istersiniz")
print("1 - Toplama islemi")
print("2 - Cikarma islemi")
print("3 - Carpma islemi")
print("4 - Bolme islemi")

secilen = input("Istediginiz islemin numarasini yaziniz: ")

sayi1 = float(input("Birinci sayiyi giriniz: "))
sayi2 = float(input("Ikinci sayiyi giriniz: "))

if secilen == "1":
    veri = toplama(sayi1, sayi2)
    print(veri)

elif secilen == "2":
    veri = cikarma(sayi1, sayi2)
    print(veri)

elif secilen == "3":
    veri = carpma(sayi1, sayi2)
    print(veri)

elif secilen == "4":
    veri = bolme(sayi1, sayi2)
    print(veri)

else:
    print("Boyle bir islem numarasi yok")



