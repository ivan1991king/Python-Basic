# ФИО  - Куркин Иван
# == Лото ==

import random


class Game:  # получение бочонка из мешка и вычисление остатка бочонков
    def __init__(self):
        self.bochonki = [i for i in range(1, 91)]

    def hod(self):
        i = random.randint(0, len(self.bochonki) - 1)
        rez_bochonok = self.bochonki[i]
        self.bochonki.remove(rez_bochonok)
        return rez_bochonok

    def count(self):
        rez_count = len(self.bochonki)
        return rez_count

class Card:  # оформление билета и методов с ним
    def __init__(self):
        numbers = sorted(random.sample(range(1, 91), 15))  # числа для карточки
        numbers1 = numbers.copy()
        karta = []
        for y in range(3):
            line = []
            for i in range(9):
                line = line + [0]
            x = sorted(random.sample(range(9), 5))  # рандомные позиции для чисел в 1 строке билета
            list_y = []
            for _ in x:
                y = random.randint(0, len(numbers1) - 1)
                list_y = list_y + [numbers1[y]]
                numbers1.remove(numbers1[y])
            list_y.sort()  # получили 5 рандомных чисел по возрастанию для 1 строки билета
            k = 0
            for j in x:
                line[j] = list_y[k]  # поставили рандомные числа из набора на рандомные места в строке билета
                k += 1
            karta = karta + [line]  # составили билет
        self.karta = karta
        self.numbers = numbers
        print(numbers)

    def __str__(self):       # Выведем  билет в отформатированном виде
        result = ""
        for j in range(3):
            for i in range(9):
                if self.karta[j][i] == 0:
                    result += "  "
                elif self.karta[j][i] == -1:  # для зачеркивания
                    result += "- "
                elif self.karta[j][i] < 10:
                    result += " " + str(self.karta[j][i])
                else:
                    result += str(self.karta[j][i])
                result += " "
            result += "\n"  # перенос строк билета
        return result.rstrip()  # удалим посл пустую строку

    def check_number(self, number):
        if number in self.numbers:
            return True
        else:
            return False

    def del_number(self, number):
        self.numbers.remove(number)
        for j in range(3):
            for i in range(9):
                if self.karta[j][i] == number:
                    self.karta[j][i] = -1


# напишем декоратор для карточки (просто попробовал)
def name_card(func):
    def wrapper(*arg):
        func(*arg)
        print("--------------------------")
    return wrapper

@name_card
def show_card(any_card, whos_cart):
    print("----" + str(whos_cart) + "------")
    print(any_card)


my_card = Card()
comp_card = Card()


def show_all_cards():
    show_card(my_card, "Мой билет")
    show_card(comp_card, "Билет компьютера")


# напишем функцию для 1 раунда
def round():
    bochonok = game.hod()
    #bochonok = int(input("Введи нужный номер боченка: ")) #- хорошо для проверки
    count = game.count()
    print(f"\n\nНовый бочонок: {bochonok} (осталось {count})")
    if comp_card.check_number(bochonok) == True:  # зачеркивает у компьютера при совпадении
        comp_card.del_number(bochonok)
    show_all_cards()
    decision = input("Выберите: 1 - зачеркнуть цифру, 2 - продолжить, 3 - выйти ")
    while decision != "3":
        if decision == "1":
            if my_card.check_number(bochonok) == True:
                my_card.del_number(bochonok)
                break
            else:
                print("Вы проиграли!\nИгра окончена")
                exit()
        elif decision == "2":
            if my_card.check_number(bochonok) == False:
                break
            else:
                print("Вы проиграли!\nИгра окончена")
                exit()
    else:
        print("Игра окончена")
        exit()
    count -= 1


show_all_cards()

start = input("Начнем игру? y/n ")
if start == 'y' and 'yes' and 'Y':
    game = Game()
    while not my_card.numbers == [] or comp_card.numbers == []:
        round()
        continue
    else:
        if my_card.numbers == [] and comp_card.numbers == []:
            print("Ничья!")
        elif comp_card.numbers == []:
            print("Победил компьютер!")
        elif my_card.numbers == []:
            print("Вы победили!")
else:
    print("Игра окончена")
