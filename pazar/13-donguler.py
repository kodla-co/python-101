# PYTHON'DA DONGULER
# Python'da kullanilan for ve while olmak uzere 2 tane dongu tipi vardir.

# Python' da For Donguleri
# Python for donguleri, bir eleman grubundaki (list, tuple, dictionary, set ya da string) elemanlara ulasmak icin kullanilir.

# Python List
# Python list verileri uzerinde for dongusu ile her bir elemana ulasilabilir.

sayilar = [1,2,3,4,5]
for a in sayilar:
    print(a)        
    

isimler = ['apo','emin','nil']
for isim in isimler:
    print(f'benim adim {isim}')


# Python String
# String bir veri bir karakter dizisidir ve string içcndeki her bir karaktere ulasmak icin for dongusu kullanilabilir.

name = 'Nil'
for n in name:
    print(n)


# Python Dictionary
# Python dictionary verileri uzerinde for dongusu ile her bir elemanin key ve value bilgileri alinabilir.

sayilar = {'sayi1':1, 'sayi2':2, 'sayi3':3}
for key,value in sayilar.items():
    print(key, value) 


# Range Fonksiyonu
# range() fonksiyonu belirli aralikta bulunan sayilari gostermek icin kullanilir.

for i in range(5):
    print(i)
    print('Selam')


for i in range(10,15):
    print(i)


for i in range(50,100,10):
    print(i)


# --------------------------------------------------------------------------------------------------------------------------------

# PYTHON WHILE DONGUSU
# While dingusunde belirtilen bir kosul dogru oldugu surece while blogu icinde tanimlanan kod satirlari tekrarlatilabilir.

a = 1
while a < 5:
    print(a)
    a += 1

# Break ve Continue 
# Break komutu donguyu sonlandirir.
# Continue komutu dongunun o turunu sonlandirir ve bir sonraki turdan devam eder.

x = 0
while x < 5:    
    x+=1
    if x == 2:
        continue
    print(x)

x = 0
while x < 5:    
    x+=1
    if x == 2:
        break
    print(x)


