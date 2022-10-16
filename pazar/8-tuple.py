# PYTHON TUPLE

# Python' da tuple listeleri, list' e benzer ancak tuple icindeki elemanlar degisitirilemez.
# Yani tuple listesine ekleme, silme, guncelleme yapilamaz.

meyve = ("erik", "cilek", "kiraz")
print(meyve) 


# Tuple Liste Elemanlarini Guncelleme
# Tuple liste elemanlari degistirilemez ama baska bir liste turune cevrilerek guncelleme yapilabilir.

a = ("erik", "cilek", "karpuz")
b = list(a)
b[0] = "elma"
a = tuple(b)

print(a)


# Tuple Elemanlarina Erisim
# Listelerdeki gibi her bir elemana soldan itibaren 0'dan baslayarak indeks numarasi ile ulasilabilir. 
# Aynı sekilde sagdan -1. indeks numarasindan baslanarak elemana ulasilabilir.

message = ('Herkese', 'merhaba', '.', 'Nasilsiniz', '?', 'Iyi', 'misiniz')

print(message[1])   
print(message[3])  
print(message[-1])  
print(message[-3])  

