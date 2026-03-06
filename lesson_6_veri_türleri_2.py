my_bool = True #boolean type
myBool = False #boolean type

x = None # null #None type

print(type(my_bool))
print(type(myBool))
print(type(x))

print(my_bool)
print(myBool)
print(x)

"""
Bilgisayar dünyasında her şey bitlerden oluşur bu bitler 0 ve 1 lerdir ve bunlar bir bittir.
Bilgisayarlar sadece 0 ve 1 bitlerinden anlar.
örneğin "100" 3 bittir.

8 bit bir araya gelerek byte'ı oluşturur

1000 byte = 1 kb
1000 kb = 1 mb
1000 mb = 1 gb
1000 gb = 1 tb

"""

import sys
y = 7 # int
print(sys.getsizeof(y)) 

"""
C dilinde yazılsaydı 4 byte yani 32 bit kaplayacaktı ancak python da 28 byte yer kaplar.
Python'un bu kadar fazla yer kaplamasının nedeni, 7 sayısını düz bir sayı olarak değil, içinde şunları barındıran bir nesne olarak saklamasıdır:

ob_refcnt → kaç yerde kullanıldığı (referans sayacı)
ob_type → nesnenin tipi (int olduğu bilgisi)
ob_digit → asıl sayı değeri

Bu yüzden Python kullanımı kolay ama bellek açısından C'ye göre daha "pahalı" bir dildir.
"""

name = b"python" #bytes 
print(type(name))
print(name)
"""
str vs bytes farkı nedir?
str metin iken ve bellekte unicode iles aklanırken bytes ile doğrudan ham veri (0-255 arası sayılar) içerir ve byte olarak saklanır

b"python" == bytes([112, 121, 116, 104, 111, 110])
p=112, y=121, t=116, h=104, o=111, n=110 (ASCII karşılıkları)
"""
# bknz: ASCII Table

Name = bytes("ş","utf-8")
print(type(Name))
print(Name)

isim = bytes("şakir","utf-8")
print(isim)

print(isim.decode("utf-8")) #encode → karakter sayıya dönüşür ("ş" → \xc5\x9f)
                            #decode → sayı karaktere dönüşür (\xc5\x9f → "ş")

"""
Neden b"ş" yazamıyoruz?
ş harfi standart ASCII'de yoktur. ASCII sadece İngilizce karakterleri kapsar (0-127).
Bu yüzden b"ş" yazarsan Python hata verir. Türkçe karakteri bytes'a çevirmek için encoding belirtmen gerekir:

b""
Sadece ASCII karakterlerle çalışır
Encoding belirtemezsin

bytes("...", encoding)
Her karakterle çalışır
Encoding belirtmek zorundasın
"""


z = bytearray([65])
print(type(z))
print(z)


soyad = bytearray(b"acar")
print(type(soyad))
print(soyad)

"""
bytearray, bytesin düzenlenebilir versiyonudur. 
İkisi de aynı işi yapar ama bytearray üzerinde değişiklik yapabilirsin.
"""

mem = memoryview(bytes(5)) #veri manipülasyonu, optimizasyon vb. ram'i daha aktif daha verimli kullanabilmek için memoryview kullanılır.

print(type(mem))
print(mem)