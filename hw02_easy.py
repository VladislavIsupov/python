# coding: utf-8

__author__ = 'Владислав'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
#
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
#
# Подсказка: воспользоваться методом .format()

print("Задача-1")

fruits = ["яблоко", "банан", "киви", "арбуз"]

i = 1
for fruit in (fruits):
    print(f"{i}{fruit:>7}")
    i += 1


#
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
#

print("\nЗадача-2")

fruits  = ["яблоко", "банан", "киви", "арбуз"]
fruits2 = ["персик", "банан", "груша", "слива", "арбуз"]

for fruit in (fruits2):
    while fruit in fruits:
        fruits.remove(fruit)

i = 1
for fruit in (fruits):
    print(f"{i}{fruit:>7}")
    i += 1


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("\nЗадача-3")

int_list = [3, 8, 7, 20]
new_list = []

for element in int_list:
    if element % 2 == 0:
        new_list.append(int(element / 4))
    else:
        new_list.append(element * 2)

print(f" произвольный список: {int_list}, новый список {new_list}")