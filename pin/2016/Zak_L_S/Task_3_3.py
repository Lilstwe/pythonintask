#Задача 3. Вариант 3

#Напишите программу, которая выводит имя "Чарльз Лютвидж Доджсон", и
#запрашивает его псевдоним. Программа должна сцеплять две эти строки и
#выводить полученную строку, разделяя имя и псевдоним с помощью тире.

#Zak L.S.
#7.04.2017

name = "Чарльз Лютвидж Доджсон"
tire = " - "
print(name)
ps = input("Под каким псевдонимом вы его знаете ? ")
if ps == "Льюис Кэрролл":
    print("Совершенно верно! " + name + tire + ps)
else:
    print("Извините, вы ошиблись.")