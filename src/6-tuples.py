# ==========================================
#                  TUPLES
# ==========================================

myList = [10, "a", "b", 3.14]
print(myList[0])

# Tuple

myTuple = (10, "a", "b", 3.14)
print(type(myTuple)) # Tuple Veri Tipini Çıktıladı.

print(myTuple[0]) # İndeks Değerine Göre Değerimizi de Çıktıladı.
# myTuple[0] = 100 --> İmmutability Özelliği Bu Veri Tipinde de Var (Değiştirilemez)

# --- Neden Kullanalım Ne Gereği Var? ---

print(myTuple.index(10)) # Parametre Olarak Belirlediğimiz Değerin Kaçıncı İndekste Olduğunu Çıktılar
print(myTuple.count(10)) # Listede Kaç Tane '10' Değeri Var Onun Sayısını Verir

resultTuple = (10,20,30,40)

resultList = list(resultTuple)
print(resultList)



