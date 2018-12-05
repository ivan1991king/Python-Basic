# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    pass

#Решение Задания-1:

def fibonacci(n, m):
        row = [1, 1]
        for i in range(m-2):
            row = row + [row[-1] +row[-2]]
        return row[n-1:]
print(fibonacci(4,8))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    pass

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

#Решение Задания-2:

def sort_to_max(origin_list):
    i = 0
    j = 1
    while j < len(origin_list):
        while i < (len(origin_list)-1):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
            i += 1
        j += 1
        i = 0
    return origin_list
print([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

#Решение Задания-3:

def filter1(func, list1):
    list2=[]
    for i in list1:
        if func(i):
            list2.append(i)
    return list2

print(list(filter1(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))        #пример

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

#Решение Задания-4:

# В параллелограмме все стороны равны

import math
#Задаем координаты точек:
A1 = ['A1', 0, 0]
A2 = ['A2', 0, 6]
A3 = ['A3', 4, 6]
A4 = ['A4', 4, 0]

def parall(A1, A2, A3, A4):

    # Напишшем функцию для определения длин сторон
    def length(A, B):
        d = math.sqrt((B[1]-A[1])**2+(B[2]-A[2])**2)
        print(f"Длина стороны {A[0]}{B[0]} составляет {d}")
        return d
    a = length(A1, A2)
    b = length(A2, A3)
    c = length(A3, A4)
    d = length(A1, A4)
    if a == c and b == d:
        print("Заданные точки являются вершинами параллеограмма")
    else:
        print("Заданные точки НЕ являются вершинами параллеограмма")

parall(A1, A2, A3, A4)