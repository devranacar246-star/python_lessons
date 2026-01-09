name = "devran" # string - str

age = 20 # integer - int

weight = 75.78 # float data type

comp = 2j # complex data type

my_list = ["apple","grape","cherry","watermelon","lemon","banana"] # list data type

my_tuple = ("red","blue","white","black","pink","orange") # complex data type

my_range = range(7) # range data tpye [0,6]

my_dict = {"name":"Devran","age":34} # dict data type anahtar-değer çiftlerinden oluşur

my_set = {"apple","grape","cherry","watermelon","lemon","banana"} #set data type anahtar -değer çfitlerinden oluşmaz tek değer tutar

my_frozen = frozenset({"red","blue","white","black","pink","orange"})  # frozenset data tpye 


print("isim:",name,"yaş:",age,"kilo:",weight,"karmaşık sayı:",comp)
print(my_list)
print(my_tuple)
print(my_range)
print(*my_range) # * işareti ile bütğn aralık yazdırılabilir
print(my_dict)
print(my_set)
print(my_frozen)

print(type(name))
print(type(age))
print(type(weight))
print(type(comp))
print(type(my_list))
print(type(my_tuple))
print(type(my_range))
print(type(my_dict))
print(type(my_set))
print(type(my_frozen))