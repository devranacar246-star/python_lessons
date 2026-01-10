"""string methods"""

"""Capitalize metodu"""

# Stringin ilk karakterini büyük harfe çevirir

# text = "welcome to my world. how is it going"
# result = text.capitalize()
# print(result)



"""Casefold metodu"""

# casefold lower gibi çalışır. stringdeki bütün harfleri küçültür ancak lowerdan daha güçlüdür ASCII karakterleri dışındaki karakterlere de etki edebilir ancak lowerdan daha yavaş çalışır.

# text = "WELCOME to my WORLD. how is it going"
# result = text.casefold()
# print(result)



"""title metodu"""

# Her kelimenin ilk karakterini büyük harflerle yazar. alfabetik olmayan her karakterden sonraki harfi büyük karaktere çevirir.

# text = "welcome to my world. how is it going"
# result = text.title()
# print(result) # "Welcome To My World. How Is It Going"

# text2 = "wels324ome to m439y wo45tld. ho5w is it going"
# result2 = text2.title()
# print(result2) # "Wels324Ome To M439Y Wo45Tld. Ho5W Is It Going"



"""swapcase metodu"""

# Büyük karakteri küçük karaktere küçük karakteri büyük karaktere çevirir.

# text = "Welcome To My World. How İs İt Going"
# result = text.swapcase()
# print(result) # "wELCOME tO mY wORLD. hOW i̇S i̇T gOING"



"""islower metodu"""

# bir stringdeki bütün karakterler küçük ise bize True değerinin döndürülmesini sağlar

# text = "welcome to my world. how is it going"
# result = text.islower() # True

# if(result):
#     print("tüm harfleriniz küçük harf")
# else:
#     print("tüm harfleriniz küçük harf değil")



"""isupper metodu"""

# bir stringdeki bütün karakterler büyük ise bize True değerinin döndürülmesini sağlar

# text = "HELLO PYTHON "
# result = text.isupper() # True

# if(result):
#      print("tüm harfleriniz büyük harf")
# else:
#     print("tüm harfleriniz büyük harf değil")



"""center metodu"""

# stringi ortalar

# text = "Hello Python"
# result = text.center(30,"-") #center içine iki paramtere alır ilk parametre kaç birimlik bir uzunluk için ortaya alacağı ikinci parametre ise stringimiz dışındaki birimlere hangi ifadenin geleceğini belirler. hiçbir şey yazılmaz ise boşluk kabul edilir.
# print(result)

