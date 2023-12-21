# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
#
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os
from Task4 import create_files

def rename_file(new_name, digits, source_ext, dest_ext, range_name, path='.'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(source_ext):
            old_name = os.path.splitext(filename)[0]
            if range_name:
                old_name_substring = old_name[range_name[0]:range_name[1]]
            else:
                old_name_substring = ""
            new_filename = f"{old_name_substring}{new_name}" \
                           f"{str(counter).zfill(digits)}{dest_ext}"
            os.rename(os.path.join(path, filename),
                      os.path.join(path, new_filename))
            counter += 1


if __name__ == '__main__':
    create_files('.txt',4)

files = os.listdir(r'C:\Users\Maks\PycharmProjects\pythonProject3\sem7\test_rename')
for file in files:
        print(file)

batch_rename('NEW_', 3, '.txt', '.md', [0, 3],
                 r'C:\Users\Maks\PycharmProjects\pythonProject3\sem7\test_rename')
