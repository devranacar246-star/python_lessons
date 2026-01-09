x = 2
y = 22.22
z = 2j

print("int:",x,"\nfloat:",y,"\ncomplex:",z) # \n komutu bir satır aşşağıya indirir.

a = 19E4 # Float için E yi destekler # 19 x 10^4 anlamına gelir 
print(a)

b = -5j 
print(b)

# complex sayı int ve float a dönüştürülemez


pi = 3.14159

radius_of_circle = float(input("Yarıçarp: ")) #inpu kullanıcıdan girdi alınmasını sağlar

area_of_circle = pi*radius_of_circle*radius_of_circle

circumference_of_circle = 2*pi*radius_of_circle

print("Alan:",area_of_circle)
print("Çevre",circumference_of_circle)


number1 = int(input("birinci sayıyı gir:"))
number2 = int(input("ikinci sayıyı gir:")) 

sum = number1 + number2

print("toplam:",sum)