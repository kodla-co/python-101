# PYTHON DICTIONARY

# Python veri tiplerinden olan dictionary yani sözlük veri yapisi key ve value seklinde verilerin saklanabilecegi bir veri yapisidir.

# Dictionary liste elemanlarina key ve value degerlerine göre ulasilik elemanlar uzerinde guncelleme yapilabilir.

ogrenci = {
    "numara": "123",
    "ad": "Asya",
    "soyad": "Duzgun"
}

print(ogrenci) 


# Dictionary Elemanlarina Erisim
# Dictionary elemanlarinin value bilgisine köseli parantezler icerisine yazilan key ile ulasilabilir.

ogrenci = {
    "numara": "123",
    "ad": "Asya",
    "soyad": "Duzgun"
}

print(ogrenci["numara"]) 
print(ogrenci["ad"])     
print(ogrenci["soyad"])

# Koseli parantez yerine get() metodu da kullanilabilir.

ogrenci = {
    "numara": "123",
    "ad": "Asya",
    "soyad": "Duzgun"
}

numara = ogrenci.get("numara")
ad = ogrenci.get("ad")
soyad = ogrenci.get("soyad")


# Dictionary Elemanlarini Guncelleme
# Key bilgisi ile ulasilan bir elemanin value degeri degistirilebilir.

ogrenci = {
    "numara": "123",
    "ad": "Asya",
    "soyad": "Duzgun"
}

ogrenci["numara"] = 789
print(ogrenci)


# Dictionary' e Yeni Eleman Ekleme
# Yeni bir eleman eklemek icin olmayan bir key bilgisinin eklenmesi yeterlidir.

ogrenci = {
    "numara": "123",
    "ad": "Asya",
    "soyad": "Duzgun"
}

ogrenci["cinsiyet"] = "K"
print(ogrenci)


# Dictionary' den Eleman Silme
# pop() metodu ile sozluk veri yapisindan belirtilen key bilgisi ile veri silinebilir.

ogrenci = {
    "numara": "123",
    "ad": "Asya",
    "soyad": "Duzgun"
}

ogrenci.pop("soyad")
print(ogrenci)

#----------------------------------------------------------------------------------------------------------------------


# Ic ice Dictionary Tanimlama

# Tanimlanan bir sozluk verisi bir baska sozluk veri yapisi icine alinabilir.

ogrenciler = {
    'asya': {
        'yas': 20,        
        'email': 'asya@gmail.com',
        'address': 'Trabzon',
        'phone': '1234455'
    },
    'nil': {
        'age': 25,
        'email': 'nil@unicrow.com',
        'address': 'Trabzon',
        'phone': '1892939'
    }
}

print(ogrenciler['nil'])

