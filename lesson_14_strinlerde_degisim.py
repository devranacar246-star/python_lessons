"""modify strings"""

# text = "python is doing well"
# print(text.upper()) # Upper case yani hepsini büyük harfe çevirir

# text2 = "Python is doing WELL"
# print(text.lower()) # Lower case yani hepsini küçük harfe çevirir



"""strip metodu"""

#white space'lere karşı kourunmak için strip metodu kullanılır 

# text = "    python is doing well     "
# print(text)
# print(text.strip()) # başta ve sondaki white spaceleri kaldırır.



"""replace metodu"""

# text = "Devran iyi birisi"
# print(text.replace("D","K")) # birinci parametre metindeki değişecek karekteri ikincisi yerine gelecek karekteri temsil eder



"""split metodu"""

# text = "Hello Python, java, c#"
# result = text.split(",") # split metodunun içindeki parametreye kadar olan kısmı ayırır
# print(result)