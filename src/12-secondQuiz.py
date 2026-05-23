# 1) Aşağıdaki kodun çıktısı ne olacaktır?
from operator import index

x = 5
y = 3
z = 6
print(x > y and z > x)

#--------------------------------------------------------------

# Sonuç 'True'(1) Dönecektir.

#--------------------------------------------------------------

# 2) Aynı değerlerle kod şu şekilde değiştilirse çıktı ne olacaktır?
print(x < y or z > y)

#--------------------------------------------------------------

# Sonuç 'True'(1) Dönecektir.

#--------------------------------------------------------------

# 3) Aşağıdaki kodun çıktısı ne olacaktır?
yas = 20

if yas < 18:
    print("18 yaşından küçüksünüz")
elif yas >= 18 and yas < 30:
    print("18 ile 30 yaş arasında bir gençsiniz")
elif yas >= 30 and yas < 40:
    print("30 ve 40 arasına gelmişsiniz")
else:
    print("40 yaşından daha büyüksünüz")

#--------------------------------------------------------------

# Sonuç "18 ile 30 yaş arasında bir gençsiniz" Çıktılayacaktır.

#--------------------------------------------------------------

#4) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}

#--------------------------------------------------------------

if "c" in my_dictionary.values():
    print("'c' in the list")

#--------------------------------------------------------------

#5) Aşağıdaki sözlükte, anahtarlar içinde a harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}

#--------------------------------------------------------------

if "a" in my_other_dictionary.keys():
    print("'a' in the list")

#--------------------------------------------------------------

# 6) Aşağıdaki listedeki sayılardan sadece çift sayı olanları yazdıran bir kod yazınız.
my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]

for num in my_numbers:
    if num % 2 == 0:
        print(num)

#--------------------------------------------------------------

#7) Aşağıdaki listedeki sayılar bir dairenin yarı çapını vermektedir.
#Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2πr)  π 3.14 alınabilir.

r_list = [3,2,5,8,4,6,9,12]

#--------------------------------------------------------------

π = 3.14
daire_cevre = []

for r in r_list:
    daire_cevre.append(2 * π * r)
print(daire_cevre)

#--------------------------------------------------------------

#8) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur.
# Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.
age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]

#--------------------------------------------------------------

age_list = []

for (name,age) in age_name_list:
    age_list.append(age)
print(age_list)

#--------------------------------------------------------------

#9) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız
metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]

#--------------------------------------------------------------
from random import randint

print(metal_list[randint(0,len(metal_list)-1)])

#--------------------------------------------------------------

#10) Aşağıdaki kodun çıktısı ne olacaktır?
number_list = [5,7,18,21,20,10,405,24]
 # [num % 2 == 0 for num in number_list]

#--------------------------------------------------------------

# Çıktı ---> [F,F,T,F,T,T,F,T]



