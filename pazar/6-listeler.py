# LISTELER

# Python'da 4 farkli liste tipi vardir.
# 1) List       => Elemanlari siralanabilir, guncellenebilir. Her bir eleman liste icerisinde birden fazla tekrarlanabilir.
# 2) Tuple      => Elemanlari siralanabilir ancak guncellenemez ve her bir eleman liste icerisinde birden fazla tekrarlanabilir.
# 3) Set        => Elemanlari siralanmaz ve indekslenemez. Her bir elemandan liste icinde sadece bir tane olabilir.
# 4) Dictionary => Key ve value seklinde deger alirlar. Ayni key bilgisiyle birden fazla eleman olamaz.

# String veri tipindeki her bir karakter bir grubun yani string karakter dizisinin bir elemanidir. 
# Her bir elemana indeks numarasi ile ulasilabilir.


#LISTE TANIMLAMA
# Liste elemanlari farkli veri tipinde olabilir.

liste1 = [1, 2, 3]
liste2 = [1, 2.0, "uc"]


# İki farkli listeyi bir liste icinde de gruplanabilir.
numbers = liste1 + liste2
print(numbers)


# Liste icinde farkli listeler de tanimlanabilir.
liste3 = [[1,2,3],[4,5,6],[7,8,9],10]
print(liste3[1])


# Listelerde Eleman Sayisi
# Eleman sayiis len() metodu ile bulunabilir.
# Ayni metot string ifadeler iicin de kullanilip karakter sayisi ogrenilebilir.

sayi = ['bir','iki','uc']
sayilar = [[1,2,3],[4,5,6],[7,8,9],10]

print(len(sayi)) 
print(len(sayilar)) 

metin = "Bugun guzel bir gun"
print(len(metin)) 


# Liste Elemanlarina Erisim

# Listelerdeki her bir elemana soldan itibaren 0'dan baslayarak indeks numarasi ile ulasilabilir. 
# Aynı sekilde sagdan -1. indeks numarasindan baslanarak elemana ulasilabilir.

liste = ["1", "iki", 3.5, True] 

print(liste[1])
print(liste[-2])


# Liste icinde bir baska liste tanimlandiginda ise alt liste elemani icinde [ ] kullanilmasi gerekir. 

liste = [[1,2,3],[4,5,6],[7,8,9],10]

print(liste[0])     
print(liste[2][1]) 


# Liste Parcalama
# Listeden tek bir eleman secmek yerine bir aralik belirtilip eleman grubunu secilebilir.

message = ['Herkese', 'merhaba', '.', 'Benim', 'adim', 'Asya']
print(message[3:6]) 


# Liste Elemanlarini Guncelleme
# Liste elemanlari guncellenmek istendiginde oncelikle elemanın secilmesi gerekir.

cars = ['BMW','Mustang','Audi','Skoda']
cars[1] = 'BMW M5'
print(cars) 



