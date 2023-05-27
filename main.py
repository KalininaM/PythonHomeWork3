# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint

n = int(input("Введите количество элементов в массиве: "))
data = [randint(1, 10) for i in range(1, n + 1)]
print(data)
x = int(input("Введите число: "))
data_1 = [int(x == data[i]) for i in range(len(data))]
print(f'Число {x} в массиве {data} встречается {sum(data_1)} раз(а)')

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
n = int(input("Введите количество элементов в массиве: "))
data = [randint(1, 10) for i in range(1, n + 1)]
print(data)
x = int(input("Введите число: "))
index_element = 0
min_element = data[0]
for i in range(len(data)):
    if data[i] < x: 
        min_element = data[i]
        index_element = i
print(f"Самый близкий по величине элемент к заданному числу {data[index_element]}")

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# *Пример:*
# ноутбук    12
dict_1 = {
    "AEIOULNSTRАВЕИНОРСТ": 1, 
    "DGДКЛМПУ": 2, 
    "BCMPБГЁЬЯ": 3, 
    "FHVWYЙЫ": 4, 
    "KЖЗХЦЧ": 5, 
    "JXШЭЮ": 8, 
    "QZФЩЪ": 10
}
count = 0
word = input("Введите слово: ").upper()
for i in word:
    for k, v in dict_1.items():
        if i in k:
            count += v
print(f"Стоимость слова {word}: {count}")