x = str("Hello python")
print(x)
print(type(x))

y = str(False)
print(y)
print(type(y))

z = str(7)
print(z)
print(type(z))

t = int(7.19)
print(type(t))
print(t)

k = int(False)
l = int(True)
print(type(k))
print(k)
print(type(l))
print(l)

m = float(7)
print(type(m))
print(m)

# metinsel ifadeler int ya da floata dönüştürülemez!

n = complex()
print(type(n))
print(n)

p = complex(2,3) # sıralı ikililerden ilki reel kısmı ikincisi sanal kısmı belirtir
print(type(p))
print(p)

r= complex('4-3j')
print(r)


liste = list(("skoda","nissan","volvo")) # fonkisyonun içinde bir parantez daha olması gerektiğini unutma

print(liste)
print(type(liste))

my_tuple = tuple(("skoda","nissan","volvo")) # fonkisyonun içinde bir parantez daha olması gerektiğini unutma

print(my_tuple)
print(type(my_tuple))

my_set= set(("skoda","nissan","volvo")) # fonkisyonun içinde bir parantez daha olması gerektiğini unutma
my_frozen = frozenset (("skoda","nissan","volvo")) # fonkisyonun içinde bir parantez daha olması gerektiğini unutma

print(my_set)
print(type(my_frozen))

print(my_frozen)
print(type(my_frozen))

my_range = range(7)
print(type(my_range))
print(my_range)

my_dict = dict(name="Devran", age=19)
print(type(my_dict))
print(my_dict)


s = bool(-5)
e = bool(0)
f = bool()
g = bool(7)


print(type(s))
print(s)
print(type(e))
print(e)
print(type(f))
print(f)
print(type(g))
print(g)
