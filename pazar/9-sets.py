# PYTHON SET

# Python' da set listeleri, list' e benzer ancak set icindeki elemanlar siralanamaz (sort) ve indekslenemez.
# Yani set elemanlarına 0,1 şeklinde indeks numaralari ile ulasilamaz. 
# Dolayisiyla set 'e eklenen bir elemanın set listesi icinde hangi sirada olacagi bilinmez. 
# Ayrıca set icindeki elemanlar tekrarlanamaz. Her bir elemandan sadece bir tane olmalıdır. Tekrarlanan elemanlar silinir.

cars = {"BMW", "Mustang", "Audi"}
print(cars) 


# Set'2 Eleman Ekleme
# Set listesine tek bir eleman eklemek için add() metodunu, birden fazla eleman eklemek icin ise update() metodu kullanilabilir.

cars2 = {"BMW", "Mustang", "Audi"}
cars2.add("Skoda") 

print(cars2) 


# Set Elemanlarini Silme
# Set' den bir eleman silmek için remove() ya da discard() metodu kullanilabilir.

cars3 = {"BMW", "Mustang", "Audi"}
cars3.remove("Audi") 

print(cars3) 

#-------------------------------------------------

cars4 = {"BMW", "Mustang", "Audi"}
cars4.discard("Mustang") 

print(cars4) 




