# Belli bir fonksiyonu yerine getiren PYTHON STRING METOTLARI

# SPLIT METODU
# Karakter dizisinde belirtilen bir
# karaktere göre parcalama islemi yapar.

message1 = 'Merhaba nasilsiniz'
message1 = message1.split(' ')
# message1 = message1.split()

print(message1)

# # UPPER METODU
# # Karakterleri buyuk harfe cevirir.

message2 = 'Hello'
message2 = message2.upper()
print(message2)


# # LOWER METODU
# # Karakterleri kucuk harfe cevirir.

message3 = 'HELLO'
message3 = message3.lower()
print(message3)


# # TITLE METODU
# # Karakter dizisindeki her kelimenin bas harfini buyuk harfecçevirir.

message4 = 'merhaba nasilsiniz'
message4 = message4.title()
print(message4)


# # STRIP METODU
# # Karakter dizisinin eger varsa basindaki
# ve sonundaki bosluk karakterlerini siler.

name = "   muberra   "
x = name.strip()
print("benim adim" + " " + x)  


# # REPLACE METODU
# # Karakter guncellemesi icin kullanilir.

message = "Unicrow sirketinde calisiyorum"
message = message.replace("calisiyorum", "calismiyorum")
print(message)


# FIND METODU
# Verilen string ifade icinde arama yapar ve buldugu ilk indeks numarasini dondurur. Eger aralinan degeri bulamazsa -1 degerini dondurur.

text = "Benim adim Mars Mars"
a = text.find("Mars")
print(a)


# INDEX METODU
# Verilen string ifade icinde arama yapar ve buldugu ilk indeks numarasini dondurur. Eger aralinan degeri bulamazsa hata dondurur.

text = "Benim adim Mars"
a = text.index("adim")
print(a)