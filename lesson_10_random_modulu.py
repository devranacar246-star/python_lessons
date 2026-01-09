import random

# myList = ["black","white","orange","purple","blue","green"]
 
# print(random.choice(myList)) # choice metodu listeden rastgele bir elemanı döndürdü




# text = "python"
# print(random.choice(text)) # choice metodunun içine string konulursa içindeki bir harfi rastgele döndürür




# myList = ["black","white","orange","purple","blue","green"]
 
# print(random.choices(myList,weights=[10,1,1,1,1,1], k=20)) # choices metodunda weights parametresi ile listenin hangi elemanının ağırlıkta olması gerektiğini  3. parametremiz ise kaç tane eleman döndüreceğini belirler



# myList = ["skoda","bmw","audi","nissan","toyota","ford"]

# random.shuffle(myList) # serideki elemanları rastgele sıralar ve listeyi değiştirir 
# print(myList)



# myList = ["skoda","bmw","audi","nissan","toyota","ford"]

# print(random.sample(myList, k=3)) #sample shuffledaki gibi listeyi değiştirmez. burdaki 2. parametre kaç tane seriden elemanı rastgele alacağını belirler.




#print(random.random()) # random metodu 0 ile 1 arasında rastgele ondalıklı bir sayı döndürür.




# print(random.uniform(30,70)) # uniform verilen aralıklar arasında rastgele nir ondalıklı sayı döndüren metotdur



print(random.triangular(30,70,68)) # triangular da uniform gibidir ancak burada 3. bir parametre eklenebilir ve bu 3. parametre ağırlığın hangi tarafta olması gerektiğini belirtir. eğer 3. parametre girilmezse eşit olasılıkla sayo döndürür
