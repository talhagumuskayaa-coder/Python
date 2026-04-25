# ==========================================
#                   SETS
# ==========================================

# unique elements, unordered / Tekil ve Sırasız

myList = [10,20,30,10,20,40,10,20,40]
print(len(myList)) # 9 Elemanlı Bir Listemiz Var

mySet = set(myList)
print((mySet)) # Listede Eğer Aynı Elemandan Birkaç Adet Varsa Set, Birden Fazla Bulunan Elemanı Bir Kez Yazdırmamızı Sağlar.

mySet = {10,20,30,10,20,40,10,20,40}
print((mySet)) # Yine Aynı Şekilde Aynı İki Eleman Listeye Koyamıyoruz.

mySet.add(50)
#print(mySet[0]) --> Yapamayız Çünkü Setlerde Sözlüklerde de Olmadığı Gibi İndeks Mantığı Yok.

mySet2 = {30,40,50,60,70}

print(mySet.union(mySet2)) # 'union' Fonksiyonu İki Setimizi Birleştirmeye Yardımcı Olur.
print(mySet.intersection(mySet2)) # 'intersection' Fonksiyonu İki Setin Kesiştiği Kümeyi Çıktılar

countryList = ["DE", "FR", "TR", "TR", "FR", "DE", "NL", "TR"] # Kaç Ülkeye Satış Yapıldığını Bulmak İstiyoruz?
print(len(countryList)) # Bu Bize Kaç Kez Satış Yapıldığı Bilgisini Çıktılar
print(len(set(countryList))) # Bu Çıktı İse Sorumuza Cevap Verir. ---> 4

emptySet = {}
print(type(emptySet)) # Boş Set Oluşturamıyoruz, Python Bunu Sözlük Olarak Çıktılar.

emptySet = set() # İlk Olarak Boş Bir Set Listesi Oluşturabiliyoruz.
print(type(emptySet))
emptySet.add(10)
emptySet.add(10)
emptySet.add(10) # Bu Şekilde de Boş Olan Setimizin İçine Sonradan Değerler Ekleyebiliriz
emptySet.add(20)
emptySet.add(30)

emptyList = []
emptyList.append(10)
emptyList.append(20) # Bu Şekilde de Boş Olan Listemizin İçine Sonradan Değerler Ekleyebiliriz.
emptyList.append(30)
print(emptyList)

emptyDictionary = {}
emptyDictionary["a"] = 10 # Bu Şekile de Boş Olan Sözlüğümüzün İçine Sonradan Değerler Ekleyebiliriz.
emptyDictionary["b"] = 20
print(emptyDictionary)


