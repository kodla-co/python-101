# PYTHON KOSUL IFADELERI

# Python'da If Blogu

# Bir kosulun True ya da False olan sonucuna gore farkli kod bloklari olusturmak icin If komutu kullanilir.

a = 20
b = 40
if b > a:
        print("b, a'dan büyüktür")


# Python'da Elif Blogu

a = 20
b = 20
if b > a:
        print("b, a'dan büyüktür")
elif a == b:
        print("a ile b eşittir")


# # Python'da Else Blogu

a = 20
b = 10
if b > a:
        print("b, a'dan büyüktür")
elif a == b:
        print("a ile b eşittir")
else:
        print("a, b'den büyüktür")

# --------------------------------------------------------

# Python'da If Bloklari

# Bir if blogu icinde baska bir if blogu baslatilabilir.

username = 'muberrabulbulaa'
password = '1234'

if (username == 'muberrabulbul'):
        if (password == '1234'):
                print('Hoş geldiniz')
        else:
                print('parola yanlis')
else:
        print('username yanlis')

# # Kosul İfadelerinde And ve Or Operatorleri

username = 'muberrabulbul'
password = '12345'

if (username == 'muberrabulbul') and (password == '12345'):
        print('Hos geldiniz')      
else:
        print('username ya da parola yanlis')

