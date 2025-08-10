## 1. Quyidagi matndan mashina nomlarini ajrating: txt = 'MsaatmiazD'
txt = 'MsaatmiazD'
print(txt[::2])

txt = 'MsaatmiazD'
print(txt [9:0:-2])

## 2. Quyidagi matndan shaxs qayerdan ekanligini ajrating: txt = "I'm John. I am from London"
txt = "I'm John. I am from London"
print(txt[20::])

## 3. foydalanuvchi kiritgan matnni teskari qilib yozadigan dastur yarating
txt = "London"
print(txt[::-1])

# 4. Berilgan soz palindrom (oldin va orqadan oqiganda bir xil) ekanligini tekshiradigan dastur yozing
so#z = "anna"
if soz == soz[::-1]:
    print("Bu so'z palindrom.")
else:
    print("Bu so'z palindrom emas.")

## 5. 5 ta meva nomidan iborat ro‘yxat yarating va uchinchi mevani chop eting.
mevalar = ["nok", "olma", "anor", "limon", "mandarin"]
print(mevalar[2])


## 6. Ikkita sonlar ro‘yxatini yarating va ularni birlashtiring.

ls1 = [2,7,5,1,3,6,4]
ls2 = [9,0,8,10,11]
ls1.append(ls2)
print(ls1)


## 6. Ikkita sonlar ro‘yxatini yarating va ularni birlashtiring.

ls1 = [2,7,5,1,3,6,4]
ls2 = [9,0,8,10,11]
ls1.append(ls2)
print(ls1)

## 6. Ikkita sonlar ro‘yxatini yarating va ularni birlashtiring.

ls1 = [2,7,5,1,3,6,4]
ls2 = [9,0,8,10,11]
ls1.extend(ls2)
ls1


## 7. Berilgan ro‘yxatdan birinchi, o‘rta va oxirgi elementlarni ajratib, yangi ro‘yxatga joylang.

ranglar = ["oq", "yashil", "kuk", "pushti","qora"]
ranglar2 = (ranglar [::2])
print(ranglar2)


## 8. Shaharlar ro‘yxatida "Paris" bor yoki yo‘qligini tekshiring va natijani chop eting.

shaharlar = ["Tashkent", "London", "Paris", "Moscow", "New York"]
if "Paris" in shaharlar:
    print("ro'yhatda bor")
else:
    print("ro'yhatda yo'q")


##9. Sonlardan iborat ro‘yxatni hech qanday sikl (loop) ishlatmasdan ikki marta takrorlab yangi ro‘yxat yarating.

list1 = [2,1,5,3,4,7,6,9]
list2 = list1 + list1
print(list2)


##10. Sonlardan iborat ro‘yxatda birinchi va oxirgi elementlarning o‘rnini almashtiring.

sonlar = [3,9,6,4,7]
sonlar[0], sonlar[-1]=sonlar[-1], sonlar[0]
print(sonlar)
