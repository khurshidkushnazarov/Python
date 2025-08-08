## 1.kvadratning perimetri va yuzi
a = int(input("Kvadratning tomonini kiriting: "))
perimetr = 4 * a
yuza = a * a
print("Perimetri:", perimetr)
print("Yuzasi:", yuza)

## 2.doiraning uzunligini topish
d = float(input("Aylana diametrini kiriting:"))
p = 3.14
c = p*d
print("Aylananing uzunligi:",c)

## 3. 2ta sonni o'rtachasini topish
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
ortacha = (a + b) / 2
print("Ortacha qiymat:", ortacha)

## 4.Ikkita son a va b berilgan. Ularning yig‘indisi, ko‘paytmasi va har birining kvadratini toping.
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
yigindi = a + b
kopaytma = a * b
sonkv1 = a**2
sonkv2 = b**2
print("yigindisi:", yigindi)
print("kopaytmasi:", kopaytma)
print("birinchi son kvadrati:", sonkv1)
print("ikkinchi son kvadrati:", sonkv2
