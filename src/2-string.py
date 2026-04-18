# ==========================================
#                   STRİNG
# ==========================================

print("Hello World") # Ekrana Çıktı Vermemizi Sağlar

myName = "talha" # Değişken Oluşturup Buna String Değeri Verebiliriz
print(myName) # Atadığımız İsim Değişkenini Çağırdığımızda Çıktı Olarak Döner

print('Hello World') # String'imizi Çift Tırnağa Alabildiğimiz Gibi Tek Tırnağa'da Alabiliriz

print("A" + "B" + "C") # Stringlerde Toplama Sembolü Stringleri Yan Yana Dizer

myNick = "Talha"
mySurname = "Gumuskaya"
print(myNick + mySurname) # Kelimeleri Bitişik Bir Biçimde Yazdı.
print(myNick + " " + mySurname) # " " Bu Şekilde De Kelimeler Arası Toplama Sırasında Boşluk Bırakabiliriz.

print(myNick * 5) # Yan Yana 5'er Kez Stringi Bitişik Bir Biçimde Yazdırır

# '.' İşlevi

name = "talha gumuskaya"
print(name.capitalize()) # Değişkenimizden Sonra '.' Koymak String'e Farklı İşlevler Verebilecek Fonksiyonları Gösterir
print(name.title()) # Her Kelimenin İlk Harfi Büyük Harfle Başlar
print(name.lower()) # Her Harfi Küçük Yazar
print(name.upper()) # Her Harfi Büyük Yazar
print(name.count("a")) # Değişkene Verdiğiniz String'in İçinde Belirlediğiniz Bir Harf'in Kaç Tane Olduğunu Çıktı Verir.

print(len(name)) # Kelimemizde Kaç Karakter Olduğunu Çıktılar
print(len(name) - 1)  # Kelimemizin Karakter Uzunluğundan 1 Eksilttik

# Escape Characters
print("Talha \nGumuskaya") # '\n' Çıktıda Bir Alt Satıra İnmemizi Sağladı.
print("Talha \tGumuskaya") # '\t' Çıktıda Kelimeler Arasına Boşluk Koyar.

# İNDEX

myString = "Talha Gumuskaya" # İndex, Atadığımız Değişkendeki Her Harfi Bir Dizin Olarak Belleğe Kaydeder.
print(myString[4]) # Gördüğünüz Gibi 4. İndex 'a' Harfine Karşılık Geliyor. [x] Parametresiyle İndex Alınır.
print(myString[0:4]) # Belirlediğimiz İndex Aralığındaki Harfleri Çıktı Verir

myName = "James Hetfield"
print(myName[len(myName)-1]) # "James Hetfield" Stringinin 13. İndeksindeki 'd' Harfini Yazdırır.
print(myName[-1]) # Sondan 1. İndeksi Yazdırır

# Slicing ----- //Önemli Terimler: Starting İndex, Stopping İndex, Stepping Size

barcode = "ABCDE123123987"

#print(barcode[#starting index : #stopping index : #stepping size])

print(barcode[3::]) # İlk 3 Harfi Kaldırıp Çıktı Verdi
print(barcode[:3:]) # 3. İndekste Durmasını Söylüyoruz
print(barcode[::2]) # İki İndeks Arasındaki Harfi Almayarak Atlaya Atlaya Çıktı Verir.
print(barcode[::-1]) # Tüm Stringi Tersten Yazdırır.
print(barcode[3:5:]) # 3. İndeksten Başlayıp 4. İndekse Kadar Yazar.

print(name.index("a")) # Belirtilen Harfin Bulunduğu İlk İndeks Numarasını Verir.
