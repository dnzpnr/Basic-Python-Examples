# Soru 1:

# 0 sayısı girene kadar sayı girişini sağlayan ve bu sayıların ortalamasını hesaplayan programı yazın.
# Bir sayı giriniz (Çıkış için 0'a basın):  5
# Bir sayı giriniz (Çıkış için 0'a basın):  a
# Hatalı değer girdiniz. Yeniden tam sayı değeri girin.
# Bir sayı giriniz (Çıkış için 0'a basın):  4
# Bir sayı giriniz (Çıkış için 0'a basın):  3
# Bir sayı giriniz (Çıkış için 0'a basın):  0
# Çıkış yaptınız.
# Girilen sayıların ortalama değeri: 4.0



i = 1
sum_of_all_entered_numbers = 0
count = 0
while i != 0:
    try:
        i = int(input('Bir sayı giriniz (Çıkış için 0\'a basın):'))
    except ValueError:
        print('Hatalı değer girdiniz. Yeniden tam sayı değeri girin.')
        continue
    if i != 0:
        sum_of_all_entered_numbers += i
        count += 1
        continue
    else:
        if count == 0:
            print('Girilen sayıların ortalama değeri: 0.0')
        else:
            print('Girilen sayıların ortalama değeri: ' + str(sum_of_all_entered_numbers/count))
        
  
    


# Soru 2:

# Girilen n sayısının kendisinden hariç en büyük pozitif tam bölenini bulan programı yazın.
# Bir n değerini giriniz: 24
# 24 sayısının kendisi hariç en büyük böleni: 12



from math import sqrt

n = int(input('Bir n değerini giriniz: '))

for i in range(3,round(sqrt(n))+1):
    if n%2 == 0:
        print(str(n) +' sayısının kendisi hariç en büyük böleni: ' + str(n//2))
        break
    elif n % i == 0:
        print(str(n) +' sayısının kendisi hariç en büyük böleni: ' + str(n//i))
        break
    else:
        continue
        
        


 
 
 
 
 

# Soru 3:

#100-999 arasındaki basamak değerlerinin küplerinin toplamının kendisine eşit olan sayıların 
#çift olanlarını bir listeye basın ve aritmetik ortalamasını alın.
# 325.25

# 1 2 2 != 1 + 8 + 8
# 1 5 3 == 1 + 125 + 27

# 1 5 3 % 10 -> 3 153 // 10
# 1 5 % 10 -> 5
# 1 % 10 -> 1



import statistics

myList = []

for sayi in range(100,999):
    if (sayi % 10)**3 + (int(sayi/10) % 10)**3 + (int(sayi/100))**3 == sayi and sayi % 2 == 0:
        myList.append(sayi)
        continue

print(statistics.mean(myList))




# Soru 4:

# Bir k sayısı tek ise 3 ile çarpılıp 1 ekleniyor, çift ise 2 ile bölünüyor.
# İşlem, k sayısı 1 olana kadar devam ediyor. Bu işlemin kaç adım sürdüğü,
# işlem sırasında k sayısının aldığı en yüksek değeri k sayısının hangi sayıdan sonra
#  hep çift olarak 1’e ulaştığını bulan programı yazın.

# Beklenen Çıktı
# Bir k sayısı giriniz: 10
# 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
# Uzunluk: 7
# Serinin en büyük değeri: 16
# Seri, hangi sayıdan sonra 1'e kadar hep çift gitmiş: 16



biggestNumber = 0
k = int(input('Bir k sayısı giriniz: '))
hepCift = 0
if k in [1,2,4,8]:
    hepCift = k
else:
    hepCift = 16
while k != 1:
    if k % 2 == 0:
        if k > biggestNumber:
            biggestNumber = k
        k = k//2
        continue
    else:
        k = k*3 + 1
        if k > biggestNumber:
            biggestNumber = k
        continue
print('Serinin en büyük değeri: ' + str(biggestNumber))
print('Seri, hangi sayıdan sonra 1\'e kadar hep çift gitmiş: ' + str(hepCift))





# Soru5:

# 0 değeri girilene kadar girilen bir sayının negatif mi yoksa pozitif mi olduğunu ekrana yazdırmak.

''' CEVAP 5

k = int(input('Bir sayi giriniz: '))

while k != 0:
    if k < 0:
        print('negatif')
    elif k > 0:
        print('pozitif')
    k = int(input('Bir sayi giriniz: '))
    continue
print('tebrikler, oyun bitti!!!')

'''

#Soru 6:
# Girilen a sayısının girilen b sayısına tam bölünüp bölünmediğini sorgulayan ve diğer tam bölenleri liste şeklinde yazdıran programı yazın.
# İPUCU 1: Bir sayının tam bölenlerini liste döndüren fonksiyonu yazabilirsiniz.

# Beklenen Çıktı:
# Bir sayı giriniz:  24
# Az önce girdiğiniz sayı için bölen değeri giriniz:  4
# 24 sayısı 4 sayısına tam bölünmektedir.
# Diğer tam bolenler: [2, 3, 6, 8, 12]

'''CEVAP 6

sayi = int(input('Bir sayi giriniz: '))

bolenSayi = int(input('Az önce girdiğiniz sayı için bölen değeri giriniz: '))

tamBolenlerListesi = []

for i in range(2,sayi):
    if sayi % i == 0:
        tamBolenlerListesi.append(i)
    else:
        continue

if sayi % bolenSayi == 0:
    print(str(sayi) + 'sayisi' + str(bolenSayi) + 'sayisina tam bolunmektedir.')
    tamBolenlerListesi.remove(bolenSayi)
    print('Diger tam bolenler: ' + str(tamBolenlerListesi))
else:
    print(str(sayi) + 'sayi' + str(bolenSayi) + 'sayisina tam bolunmemektedir!!!')
    

'''
























