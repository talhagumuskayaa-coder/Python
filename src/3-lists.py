# ==========================================
#                   LİSTS
# ==========================================

# List

myString = "Hello Python"
print(myString.split()) # Split Fonksiyonu Bizim String'imizi List Tipine Çevirdi.

# myString[0] = "a" ----> Bu Özelliğe 'Immutability' Denir.

myList = [10, 20, 30] # Tek Bir Değişken İçerisine Liste Oluşturabiliyoruz.
x = 10
y = 20
z = 30

myList = [x, y, z]
print(myList)

print(myList[0]) # Oluşturduğumuz Listedeki Elemanlara Bu Şekilde Tek Tek De Ulaşabiliriz.

print(type(myList)) # Type'ı 'List' Olarak Verdi
print(type(myList[0])) # Type'ı 'Int' Olarak Verdi

myList[0] = 100 # Liste İçerisindeki Bir Değeri Değiştirebiliriz. ---> Mutability
print(myList[0])
print(myList[-1]) # Son Elemanı Bu Şekilde Çıktılayabiliriz.

myList.append(80) # 'Append' Fonksiyonu Listeye Sonradan Değerler Eklememizi Sağlar. Eklenen Değer En Son İndeks Olur.
print(myList)
print(myList.count(100)) # Listede Kaç Adet 100 Sayısı Varsa Onun Miktarını Çıktı Verir.
print(myList.index(100)) # Belirttiğimiz Sayının Kaçıncı İndekste Olduğunu Bize Çıktılar
myList.insert(1, 50) # Append'den Farkı Ekleyeceğimiz Sayının İndeksini De Belirleyebiliyoruz
print(myList)
myList.remove(50) # Çıkartmak İstediğimiz Değeri Çıkartır.
myList.reverse() # Tüm Listeyi Tersten Sıralar
myList.sort() # Listeyi Küçükten Büyüğe Doğru Sıralayacaktır.
print(myList)

# Kullanıcıdan İnput Alma

x = input("Enter x: ") # 'input' Kullanıcıdan Input Almadan Önce Kullandığımız Komuttur.
print(x)
y = input("Enter y: ") # Integer Bir Değer De Girsek 'input' Komutu Bunu String Olarak Algılayarak Çıktı Veriyor.
print(y)

inputList = []
inputList.append(x)
inputList.append(y)
print(inputList)

print(inputList[1] * 2) # inputList Listesindeki 1. İndeksteki Sayıları Bitişik Şekilde Yazar.
print(int(inputList[1]) * 2)  # 'int' Parametresi İle Listedeki Değerleri Integer Olarak Çarptık.

# Veri Tipini Değiştirmek

myInteger = 50
str(myInteger) # Değer String'e Döndü
print(type(myInteger))

myString = "40"
int(myString) # Girdiğimiz String Değişkenini İnteger'a Döndürdü
print(type(myString))

float(myString) # Girdiğimiz Değişkeni Float'a Döndürdü
print(type(myString))

# List İleri Seviye

nameList = ["talha", "atil", "ahmet", "mehmet"] # Sadece String Tutan Liste
floatList = [3.14, 2.5, 10.2, 100.123] # Sadece Float Değeri Tutan Liste

mixedList = ["talha", 1, 3.14]
print(type(mixedList)) # Karışık Veri Tiplerini Tek Bir Listede Tutabiliyoruz

list1 = [10,20,30]
list2 = [40,50,60]

print(list1 + list2) # 2 Listeyi Yan Yana Sıralar Ve Yeni Bir Liste Oluşur.
print(list1 * 2) # 1. Listedeki Elemanları Tekrar Sıraladığı Bir Liste Oluşturur.

print(type(mixedList[0])) # Karışık Listeden İndeks Seçip Çıktılayınca Veri Tipini Python Anlayarak Çıktı Verir

# NestedList (Liste İçinde Liste)

myNestedList = [10,20,3.14,"talha", [1,2,3]] # Liste İçinde Liste
print(myNestedList[0])
print(myNestedList[2])

print(myNestedList[4]) # Listenin İçindeki Listeyi Kaçıncı İndeksteyse Çıktı Olarak Tüm Listeyi Tüm Değerleriyle Verir
print(myNestedList[4][1]) # Liste İçerisindeki Listenin İçindeki Değerlerden 1. İndeks Numarasına Sahip Değeri Çıktılar.

lastList = ["a","b","c", ["c","d","e"],"f"]
print(len(lastList)) # Listeyi Tek Başına Bir Eleman Sayarak 5 Elemanlı Bir Liste Uzunluğu Çıktılar.

firstList = [10,20,30,40,50,60,70]
print(firstList[2::]) # İlk 2 Elemanı Alma Devamını Çıktıla
print(firstList[:5:]) # 5. Elemana Kadar 5. Eleman Dahil Çıktılar
print(firstList[::2]) # Arada 1 Eleman Boşluk Bırakarak Atlaya Atlaya Çıktı Verir.
print(firstList[1:6:2]) # İlk Elemanı Alma, 1 Elemanlık Boşluk Bırakarak 6. Elemana Kadar Çıktıla
