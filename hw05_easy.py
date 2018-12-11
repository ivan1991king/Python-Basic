# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os
import sys
import shutil

def create_dirs(dirname):
    if dirname == '.':    # создание 9 папок только в рамках easy
        i = 1
        os.path.join(os.getcwd(), dirname)
        while i < 10:
            path = (f"dir_{i}")
            try:
                os.mkdir(path, mode=0o777)
            except OSError:
                print("Создать директорию %s не удалось" % path)
            else:
                print("Успешно создана директория %s " % path)
            i += 1
    else:
        try:
            os.mkdir(dirname, mode=0o777)
        except OSError:
            print("Создать директорию %s не удалось" % dirname)
        else:
            print("Успешно создана директория %s " % dirname)

def delete_dirs(dirname):
    if dirname == '.':    # удаление 9 папок только в рамках easy
        i = 1
        os.path.join(os.getcwd(), dirname)
        while i < 10:
            path = (f"dir_{i}")
            try:
                os.rmdir(path)
            except OSError:
                print("Удалить директорию %s не удалось" % path)
            else:
                print("Успешно удалена директория %s " % path)
            i += 1
    else:
        try:
            os.rmdir(dirname)
        except OSError:
            print("Удалить директорию %s не удалось" % dirname)
        else:
            print("Успешно удалена директория %s " % dirname)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_of_dirs(dirname):
    os.path.join(os.getcwd(), dirname)
    print(next(os.walk('.'))[1])



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_current_file():
    cur_file = sys.argv[0]
    newfile = cur_file + '.dupl'
    shutil.copy(cur_file, newfile)
    try:
        newfile = cur_file + '.dupl'
        shutil.copy(cur_file, newfile)
    except OSError:
        print("Скопировать текущий файл не удалось" % path)
    else:
        print("Успешно скопирован текущий файл %s " % newfile)
def main():
    create_dirs('.')
    delete_dirs('.')
    list_of_dirs('.')
    copy_current_file()
if __name__ == "__main__":
    main()