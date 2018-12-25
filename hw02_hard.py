# coding: utf-8

# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?
#


text = "This function drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(), passing args and kws straight through. By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments. In this case, it is purely a convenience function so you don’t have to explicitly import pdb or type as much code to enter the debugger. However, sys.breakpointhook() can be set to some other function and breakpoint() will automatically call that, allowing you to drop into the debugger of choice."

import string

text = text.lower()

# Слова
for punct in string.punctuation:
    while punct in text:
        text = text.replace(punct, "")
words = text.split(" ")
print(words)

# Буквы английского алфавита
leters = []
for ascii in string.ascii_lowercase:
    if ascii in text:
        leters.append(ascii)

print(f"Количество слов: {len(words)}")
print(f"Количество английских букв: {len(leters)}")



# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра


text1 = "This function drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(), passing args and kws straight through. By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments. In this case, it is purely a convenience function so you don’t have to explicitly import pdb or type as much code to enter the debugger. However, sys.breakpointhook() can be set to some other function and breakpoint() will automatically call that, allowing you to drop into the debugger of choice."
text2 = "This manual is organized from the inside out: it first describes the built-in functions, data types and exceptions, and finally the modules, grouped in chapters of related modules."

text1 = text1.lower()
text2 = text2.lower()

# Слова

for punct in string.punctuation:
    while punct in text1:
        text1 = text1.replace(punct, "")
words1 = set(text1.split(" "))

for punct in string.punctuation:
    while punct in text2:
        text2 = text2.replace(punct, "")
words2 = set(text2.split(" "))

words = []
for word in words1:
    if word in words2:
        words.append(word)

words = set(words)
print(words)
print(f"Количество одинаковых слов - {len(words)}")

# EXTRA
# Есть два словаря. Один это рецепт блюда, второй это список продуктов, которые есть в ходильнике.
#
# Ключ это название продукта, значение - это количество.
#
# Нужно сравнить два словаря и дать словарь, в котором будет список покупок
# Если для рецепта всё есть, то сказать что ничег

recipe = {"яблоко":1, "банан":3, "киви":3, "арбуз":1}
refrigerator = {"персик":2, "банан":2, "груша":5, "слива":10, "арбуз":3}
need = {}

for key, value in recipe.items():
    if key in refrigerator:
        if refrigerator[key] < value:
            need[key] = value - refrigerator[key]
    else:
        need[key] = value

print(f"Нужно докупить: {need}")