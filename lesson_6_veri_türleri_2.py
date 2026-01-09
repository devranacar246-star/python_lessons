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
Bilgisayar dünyasında her şey bitlerden oluşur bu bitler 0 ve 1 ler bir bittir.
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

name = b"python" #bytes 
print(type(name))
print(name)

# bknz: ASCII Table

Name = bytes("ş","utf-8")
print(type(Name))
print(Name)

isim = bytes("şakir","utf-8")
print(isim)


z = bytearray([65])
print(type(z))
print(z)


soyad = bytearray(b"acar")
print(type(soyad))
print(soyad)

mem = memoryview(bytes(5)) #veri manipülasyonu, optimizasyon vvb. ram'i daha aktif daha verimli kullanabilmek için memoryview kullanılır.

print(type(mem))
print(mem)