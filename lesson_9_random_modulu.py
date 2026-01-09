x = int ("7") # içerisinde sadece sayı bulunan bir string float yya da integer a çevrilebilir.

print(x)
print(type(x))




# import random
# print(random.random()) # bu şekilde bırakılırsa rastgele sayı bilgisiyarın sistem saatine göre verilir ve hep değişir

"""
Varsayılan değeri sistem saatinden çekmesinin sebebi zaman saniye bazında sürekli değişmesidir. 
Bu yüzden seed değerei sürekli değişir ve her seferinde farklı bir sayı üretilir.
Ancak biz seed değerini atayınca bir sabir sayı üzerinden hep aynı rastgele sayıyı üretiyor.
"""

# import random

# random.seed(2)
# print(random.random())

# print(random.random())

# print(random.random())






# import random

# print(random.random())

# state = random.getstate() # bir sonraki random sayının durumunu almayı sağlar

# print(random.random())
# random.setstate(state) # bir sonraki random sayının durumunu kaydedilen sayıya dönüştürür

# print(random.random())

# print(random.random())






# import random

# print(random.getrandbits(8)) # 8 bit boyutunda rastgele bir tam sayı üretir





# import random 

# print(random.randrange(1,10)) # [1,9] aralığında rastgele bir sayının verilmesini sağlar




# import random 

# print(random.randrange(1,10,3)) # 3. parametre artış miktarını belirtir




# import random

# print(random.randint(1,5)) # randint 2. parametrenin de dahil edilmesini sağlar