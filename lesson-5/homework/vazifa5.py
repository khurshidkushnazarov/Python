## 1. Kabisa yili funksiyasi (Leap year):
year = int(input('Yilni kiriting'))

if year%4==0:
    if year%100 == 0:
        if year%400 == 0:
            print('kabisa yili')
        else:
            print('kabisa yili emas')
    else:
        print('Kabisa yili')
else:
    print('kabisa yili emas')

### 1.  """ Berilgan yil kabisa yili (kabisa) ekanligini aniqlaydi.

   ## Yil kabisa yili bo'lishi uchun quyidagi shartlar bajarilishi kerak:
   ## - 4 ga bo‘linishi kerak, va
   ## - 100 ga bo‘linmasligi kerak, agar 400 ga ham bo‘linmasa.

def kabisa_yilmi(yil):
    if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
        return True
    else:
        return False
yil = int(input("Yilni kiriting: "))

if kabisa_yilmi(yil):
    print(f"{yil} kabisa yilidir.")
else:
    print(f"{yil} kabisa yili emas.")


#   2.Shart operatorlari mashqi:
# Berilgan butun son n uchun quyidagi shartli amallarni bajaring:
# Agar n toq bo‘lsa, "Weird" deb chiqaring
# Agar n juft va 2 dan 5 gacha (ikkalasini ham qo‘shib) bo‘lsa, "Not Weird" deb chiqaring
# Agar n juft va 6 dan 20 gacha (ikkalasini ham qo‘shib) bo‘lsa, "Weird" deb chiqaring
# Agar n juft va 20 dan katta bo‘lsa, "Not Weird" deb chiqaring


n = int(input("Butun sonni kiriting: "))
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

# 3. Ikki butun son a va b berilgan. Bu ikkala son oralig‘idagi barcha juft sonlarni toping. a va b ham kiritiladi (inclusive).
# Cheklov: sikl (loop) ishlatmang.
def juft_sonlar(a, b):
    start = min(a, b)
    end = max(a, b)
    if start % 2 != 0:
        start += 1
        juftlar = list(range(start, end + 1, 2))
    return juftlar
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

natija = juft_sonlar(a, b)
print("Juft sonlar:", natija)

