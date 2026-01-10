"""String formatlama"""

"""format metodu"""

# age = 20
# name = "Devran ACAR"
# text = "My name is Devran ACAR, I am "
# text2 = "My name is Devran ACAR, I am {}".format(age)
# text3 = "My name is {}, I am {}".format(name,age)
# text4 = "I am {1}, My name is {0}".format(name,age)

# print(text+str(age))
# print(text2)
# print(text3)
# print(text4)



"""f-string kullanımı"""


# age = 20
# name = "Devran ACAR"
# text = f"My name is {name}, I am {age}"
# print(text) # "My name is Devran ACAR, I am 20"

# price = 19.47519
# text2 = f"The price is {price} turkish lira"
# text3 = f"The price is {price:.1f} turkish lira" # f floatın kısaltması 1 ise virgülden sonra sadece bir basamağın alınacağı anlamına gelir ve bir basamak alacağı için yuvarlama işlemei yapacaktır
# text4 = f"The price is {price:.2f} turkish lira" 
# text5 = f"The price is {price:.3f} turkish lira" 

# print(text2) # "The price is 19.47519 turkish lira"
# print(text3) # "The price is 19.5 turkish lira"
# print(text4) # "The price is 19.48 turkish lira"
# print(text5) # "The price is 19.475 turkish lira"



"""örnek uygulama"""

midterm_exam_score = input("Enter the midterm exam grade:")
final_exam_score = input("Enter the final exam grade:")
average_score = (float(midterm_exam_score) + float(final_exam_score))/2

result = f"your midterm exam score is {midterm_exam_score}\nyour final exam score is {final_exam_score}\nyour average score is {average_score}"

print(result)







