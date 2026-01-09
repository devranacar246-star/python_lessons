# output variables

text = "Python is wonderful"
print(text)  #function_name()

x = "Python" 
y = "is"
z = "wonderful"

print(x,y,z)
print(x+y+z) # virgül yerine + kullanılacaksa string ifadenin sonuna bir boşluk eklnemesi okunmayı kolaylaştırır

a = 7
b = 12
c = "Python"
print(a+b)

print(a,b,c) # farklı veri tipleri virgülle yazdırılabilir ancak + ile yazdırılamaz

# global variables

text = "marvellous" # functionun içinde olmayan variablelara global variable denir

def my_function(): 
    text = "fantastic" # functionların içindeki variablelara local variable denir
    print("Pyhton is "+text)

my_function() # functionlar çağırılmadığı sürece çalışmaz
print("Python is "+text)

# eğer functionun içinde aynı isimle variable varsa function çağırıldığında local variable kullanılır

def myFunction():
    global x 
    x = "fantastic"

myFunction()
print("Python is "+x)

# why variables

number = 7
print(number)
number = 19
print(number)

number = number+2 # değişken atamalarında sağdan sola bir akış vardır.
print(number)