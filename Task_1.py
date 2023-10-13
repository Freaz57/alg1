import operator
from datetime import datetime
from random import randint


class List:

    def __init__(self, Length):
        self.name = self.get_random_list(Length)
        self.length = Length

    def get_random_list(self, l):
        '''
        Заполнение случайными числами списка длиной l
        :param l:
        :return:
        '''
        a = [0] * l
        for i in range(l):
            a[i] = randint(1, 100)
        return a

    def print_list(self):
        '''
        Вывод на экран списка в строку
        :return:
        '''
        for i in range(self.length):
            print(self.name[i], end=" ")
        print()

    def buble_sort(self, direct):
        '''
        Сортировка списка методом пузырька
        :param direct:
        '1' - по убыванию, '-1' - по возрастанию
        :return:
        '''
        if direct == 1:
            a = operator.lt
            #  стандартный модуль operator с функциями, соответствующими операторам.Оператору < соответствует
            # функция operator.lt, > - operator.gt.
        elif direct == -1:
            a = operator.gt
        else:
            print('Не верно задан параметр ')

        for i in range(self.length):
            for g in range(self.length - 1):
                if a(self.name[g], self.name[g + 1]):
                    self.name[g], self.name[g + 1] = self.name[g + 1], self.name[g]

    def quick_sort(self, startPos, endPos):
        '''
        Быстрая сортировка методом Хоара
        :param startPos:
        начальная позиция
        :param endPos:
        конечная позиция
        :return:
        '''
        pivot = self.name[((startPos + endPos) // 2)]
        left = startPos
        right = endPos
        while left <= right:
            while self.name[left] < pivot:
                left += 1
            while self.name[right] > pivot:
                right -= 1
            if left <= right:
                if left < right:
                    self.name[left], self.name[right] = self.name[right], self.name[left]
                left += 1
                right -= 1
        if left < endPos:
            self.quick_sort(left, endPos)
        if startPos < right:
            self.quick_sort(startPos, right)

    def bin_search(self, value, left, right):
        '''
        Двумерный поиск в списке
        :param value:
        :param left:
        :param right:
        :return:
        '''
        if left > right:
            return -1
        mid = (right - left) // 2 + left
        if value > self.name[mid]:
            return self.bin_search(value, mid + 1, right)
        elif value < self.name[mid]:
            return self.bin_search(value, left, mid - 1)
        else:
            return mid


n = int(input("Длина списка: "))
rnd_lst = List(n)
# print("До сортировки: ", end=" ")
# rnd_lst.print_list()
# print("Укажите направление сортировки: '1' - по убыванию, '-1' - по возрастанию: ", end=" ")
# direction = int(input())
# print('Отсортированный методом пузырька: ', end=" ")
begin_time = datetime.now()
rnd_lst.buble_sort(1)
end_time = datetime.now()
print("Метод пузырька время - ", end_time - begin_time)

rnd_lst2 = List(n)

begin_time = datetime.now()
rnd_lst2.quick_sort(0, n - 1)
end_time = datetime.now()
print("Метод Хоара время - ", end_time - begin_time)
# rnd_lst.print_list()
# s = int(input('Искомый элемент: '))
# print(rnd_lst.bin_search(s, 0, n - 1))
