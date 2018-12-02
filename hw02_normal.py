# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

# Решение Задачи-1:
import math
s_list = [2, -5, 8, 9, -25, 25, 4]
print(s_list)
i=0
while i < len(s_list):
    if s_list[i] >= 0:
        k = math.sqrt(s_list[i])
        if k.is_integer():      #проверяем, если значение корня целое число
            s_list[i] = int(k)
        else:
            s_list[i:i+1] = []
            i -= 1      #восстанавливаем правильную последовательность в списке
    else:
        s_list[i:i + 1] = []
        i -= 1
    i += 1
print(s_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# Решение Задачи-2:
today = str(input("Введите сегодняшнюю дату в формате dd.mm.yyyy: "))
date = today[0:2]
month = today[3:5]
year = today[6:10]
dd = {"01": "первое", "02": "второе", "03": "третье", "04": "четвертое", "05": "пятое", "06": "шестое", "07": "седьмое",
      "08": "восьмое", "09": "девятое", "10": "десятое", "11": "одиннадцатое", "12": "двенадцатое", "13": "тринадцатое",
      "14": "четырнадцатое", "15": "пятнадцатое", "16": "шестнадцатое", "17": "семнадцатое", "18": "восемннадцатое",
      "19": "девятнадцатое", "20": "двадцатое", "21": "дведцать первое", "22": "двадцать второе",
      "23": "двадцать третье", "24": "двадцать четвертое", "25": "двадцать пятое", "26": "двадцать шестое",
      "27": "двадцать седьмое",  "28": "двадцать восьмое", "29": "двадцать девятое",
      "30": "тридцатое", "31": "тридцать первое"}
mm = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня",
      "07": "июля", "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря"}
print("Сегодня:", dd[date], mm[month], year, "года")

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

# Решение Задачи-3:
import random
print("\n\n")
n = int(input("Введите количество элементов в списке: "))
e_list=[]
i=0
while i < n:
    dig = random.randrange(-100, 101)
    e_list = e_list + [dig]
    i += 1
print(e_list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

# Решение Задачи-3:
print("\n\n")
#lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst = [3, 0, 0, 12, 3, 2, 1, 7, 7, 9, 66, 65]
print("Исходный список:", lst)
i= 0
lst2 = []       #список с неповторяющимеся элементами
lst3 = []       #список с повторяющимеся элементами
while i < len(lst):
    if lst[i] in lst[0:i]:
        k = []
        z = [lst[i]]
    else:
        k = [lst[i]]
        z = []
    lst2 = lst2 + k
    lst3 = lst3 + z
    i += 1
print("Список с неповторяющимеся элементами: ", lst2)
print("Список с повторяющимеся элементами: ", lst3)
