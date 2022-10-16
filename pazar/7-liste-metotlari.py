# LISTE METOTLARI

# Listeye Eleman Ekleme
# Python listelerinin sonuna bir eleman eklemek icin append() metodu kullanilir.

meyveler = ["elma", "armut", "kiraz"]
meyveler.append("erik")
print(meyveler) 

# Python listelerinde belirtilen bir indeks'e eleman eklemek icin insert() metodu kullanilir.

meyveler = ["elma", "armut", "kiraz"]
meyveler.insert(2,"erik")
print(meyveler) 


# Listeden Eleman Silme
# Python listelerinden eleman silmek için kullanilabilecek farkli metotlar vardir.

# Listeden bir eleman silmek için remove() metodu kullanilabilir.

meyveler = ["elma", "armut", 4]
meyveler.remove(4)
print(meyveler) 

# Python listelerinde belirtilen bir indeks' deki elemani silmek için pop() metodu kullanilir. 
# Eger indeks numarasi belirtilmezse listenin son elemani silinir.

meyveler = ["elma", "armut", "kiraz"]
meyveler.pop(1)
print(meyveler) 

# del() metodu ile herhangi bir indeks numarasindaki eleman silinebilir.

meyveler = ["elma", "armut", "kiraz"]
del meyveler[2]
print(meyveler) 


# Liste Elemanlarini Siralama
# Liste elemanlarini siralamak icin sort() metodu kullanilir.

sayilar = [1, 10, 5, 16, 4, 9, 10]
harfler = ['a', 'g', 's', 'b', 'y', 's']

sayilar.sort() 
harfler.sort() 

print(sayilar)
print(harfler)

# Liste elemanlari reverse() metodu ile tersten yazdirilabilir.

sayilar = [1, 10, 5, 16]

sayilar.reverse() 

print(sayilar)


# Min() ve Max() Metodu
# Bir liste icindeki minimum ve maksimum deger sayısal veya alfabetik olarak alinabilir.

sayilar = [1, 10, 5, 16, 4, 9, 10]
harfler = ['a', 'g', 's', 'b', 'y', 'a', 's']

print(min(sayilar))
print(max(harfler))


# Count Metodu
# Bir liste icinde tekrarlayan elemanlarin sayisini belirlemek icin count() metodu kullanilabulir.

sayilar = [1, 10, 5, 16, 4, 9, 10]
harfler = ['a', 'g', 's', 'b', 'y', 'a', 's']
print(sayilar.count(10))
print(harfler.count('a'))



