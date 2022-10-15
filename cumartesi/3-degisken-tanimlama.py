# PYTHON DEGISKEN TANIMLAMA

# Geçici olarak veri saklamak için oluşturulan alanlara degisken denir.

# Tanımlanan degiskenler bellekte tanımlanan geçici alanlardır.

# Degisken isimleri rakam ile baslayamaz.

# name1 => gecerli
# _name => gecerli
# 4name => hatalı, gecersiz

# Komut isimleriyle tanimlama yapilamaz. if ya da for kelimesi değisken ismi olamaz.

# Kucuk buyuk harf duyarliligi vardir.

name = 'Muberra'
name = 'BULBUL'

print(name)


#  Python acisindan sorun yok ama degisken isimlerinde Turkce karakter kullanmamaliyiz.


a = 20
b = 20
c = a + b
d = b - a

print(a)  # 20
print(b)  # 20
print(c)  # 40
print(d)  # 0

# Degiskenkere sozel bir atama (string) islemi yaparken tek tirnak ya da cift tirnak kullanilabilir.

animal = "Cat"
name = 'Mars'

print(animal + " " + name)

# Degiskenlere sayisal bir atama yaparken tirnak isareti kullanirsak ne olur?


# Degisken icerisinde var olan bir deger yeni bir atamayla degistirilebilir.

# x = 10   
# y = 20  
# x = 40   # x icinde bulunan 10 degeri silinir ve 40 degeri aktarilir.
# x += 10  # x degiskeni uzerine 10 degeri eklenmis olur ve sonuc 50 olur. (x = x + 10)

# Python'da ayri satirlarda yapilan degisken tanimlamasi ayni satirda da yapilabilir.

x, y, cat = 1, 2.3, 'Mars'

print(x)
print(y)
print(cat)







