"""escape characters"""

# text = "python is \"doing\" well" # tek tırnaktan veya çift tırnaktan önce backslash konulursa kaçırma gerçekleşir
# text2 = "python is \\ doing well" #  tek backslash hata verdirtirdi o yüzden çift backslash kullanılmalı

# print(text)
# print(text2)



"""\n karakteri"""

# text = "İyilik\niyidir" # \n karakterinden sonra boşluk kullanmak metinlerin aynı hizada alt alta gelmemesine neden olacak
# print(text)



"""\r \t karakterleri"""

# \r karakterini python okuduktan sonra imleci başa getirir ve geri kalan kısmı yeniden önceki yazılan kısmın üstüne yazar
# \t karakteri 1 tablık boşluk bırakır

# text = "Hello\rPython"
# print(text) # hello 5 karakterden oluşuyorken python 6 karakterden oluşacağı için sonuç sadece Python olacaktır

# text2 = "Devran\rAcar"
# print(text2)

# text3 = "Hello\tPython"
# print(text3)



"""\b komutu"""

# \r komutu gibi çalışır ancak imleci başa değil bir karakter geriye getirerek üstüne yazdırma yapar

# text = "Hello\bPython"
# print(text)



"""Octal sayılar"""

# 2 li sayı sisteminden bahsetmiştik octal sayılar ise 8 li sayı sistemidir ve ASCII karakterlerin bir octal değeri vardır

# text = "\120\171\164\150\157\156" #Python'un octal sayılarla karşılığı
# print(text)



"""Hexadecimal Sayılar"""

# 2 li sayı sisteminden bahsetmiştik hexadecimal sayılar ise 16 li sayı sistemidir ve ASCII karakterlerin bir hexadecimal değeri vardır. burada hexadecimal olduğunu belli etmek için değerden önce x yazılmalıdır.

# text = "\x50\x79\x68\x6F\x6E" # 16'lık sistemde 10 ve sonrasındaki 16 ya kadar olan sayılar sırasıyla A,B,C,D,E, ve F olarak belirlenmiştir
# print(text)