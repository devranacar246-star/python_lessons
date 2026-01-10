# print("hello")
# print("It's alright")
# print('he is called"big boy"')
# print('he is called \'big boy\'')

# text = "python"

# text2 = """ this is so good
#             life is good
#             I'm a variable
#             multilina strings
#         """
# # 3 tırnak yerine 3 tek tırnak da kullanılabilirdi



# cars = ["bmw","volvo","skoda","nissan"]
# print(cars[0])
# print(cars[1])
# print(cars[2])
# print(cars[3])



# text = "Hello, Python!"
# print(text[0])
# print(text[5])
# print(text[13])


"""Stringlerde döngü kullanımı"""

# text = "Python is weird"
# for x in text:
#     print(x)



"""Stringlerde uzunluk"""

# text = "Python is weird"

# print(len(text)) # virgül soru işareti vb işaretler ve boşluk ifadeleri de uzunluğa dahil edilir



"""Stringlerde arama komutu in ve not in"""

# text = "The best languages in life are free!"

# print("free" in text) # eğer text içinde free varsa True değerini yoksa False değerini verir
# print("expensive" in text)

# search = "best" # bir variable içine alıp da arama yapabiliriz
# print(search in text)

# if search in text:  # döngülerde de kullanabiliriz
#     print("Yes, 'best' is present") 

# search2= "expensive"

# if search2 in text:  # if sadece True değeri için çalışır bu yüzden bu ifade yazdırılmaz
#     print("Yes, 'expensive' is present")  

# if search not in text:
#     print("Yes, 'best' is present") 

# if search2 not in text:  # in var mı? sorusunu ararken not in  yok mu? sorusunu arar
#     print("No, 'expensive' is not present")

# print(search2 not in text) # True değerini döndürür çünkü yok mu sorusunun cevabı evet yoktur yani 1 yani true dur
# print(search not in text) # False değerini döndürür çünkü yok mu sorusunun cevabı hayır vardır yani 0 yani false