# PYTHON KARAKTER DIZILERI : STRINGS

#Python'da karater dizileri '' veya "" ile tanimlanir.

# "deneme" veya 'deneme' tanimlamasi aynidir. 
# Bazi durumlarda tek tirnak karakteri, karakter dizisinin bir elemani gibi gosterilmek istenebilir.

text = "Asya'nin kitabi"
print(text)

# ------------------------------------------------------------------------------------------------------

# STRING BIRLESTIRME

# Tanimlanan string ifadeler + operatoru ile birlestirilebilir. 

name = 'Muberra'
surname = 'BULBUL'
person = "Merhaba" + " " + name + " " + surname
print(person)


# PYTHON VERI TIPI DONUSUMU

a = input("1. sayiyi giriniz: ")
b = input("2. sayiyi giriniz: ")
toplam = int(a) + int(b)
print(toplam)
print(type(toplam))

# Python input() fonksiyonu ile satirdan okunan deger sayısal bir deger olsa da python icin string bir veri tipi olarak algilanir.

# Kontrol edelim => print(type(a)) | (type(a)

# Dogru sonuc alabilmek icin a ve b degiskenlerinin number veri turune donusturulmesi gerekir.

toplam = int(a) + int(b)
print(toplam)

#Ayni islemin ondalıklı olarak yapilmasi istendiginde int() fonksiyonu yerine float() fonksiyonunu kullanarak degerleri float veri tipine cevirebiliriz.

toplam = float(a) + float(b)
print(toplam)

#Boolean
#Boolean veri turunden string veri turune donusum yapilmak istenirse;

isPerson = True
print(type(isPerson))


# boolean => string

isAnimal = False
isAnimal = str(isAnimal)   
print(isAnimal)            
print(type(isAnimal))      


