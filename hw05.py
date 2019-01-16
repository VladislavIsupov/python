
__author__ = 'Владислав Исупов'

import os
#import sys

#EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Создаем папки
for i in range(9):
    dir_name = f"dir_{i+1}"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

# Удаляем папки
for i in range(9):
    dir_name = f"dir_{i+1}"
    if os.path.exists(dir_name):
        os.rmdir(dir_name)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for i in (os.listdir(".")):
    if os.path.isdir(i):
        print(i)

#HARD

# Задание-1
#
# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить
