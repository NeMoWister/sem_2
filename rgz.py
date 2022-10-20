import operator
import random


class typeA:
    """Структура БД"""

    def __init__(self, name, bith, oklad):
        self.name = name
        self.bith = bith
        self.oklad = oklad

    def display_type_a(self):
        print('Имя: {}, Дата рождения {}, Оклад: {}'.format(self.name, self.bith, self.oklad))

    def outd(self):
        s = str(self.name) + ' ' + str(self.bith) + ' ' + str(self.oklad) + '\n'
        return s


def rand_bd():
    indata = open('in.txt', 'w')
    for k in range(200):
        i, j = random.randint(1000, 10000), random.randint(1970, 2000)
        a = {1 : 'Максим',
             2 : 'Олег',
             3 : 'Пётр',
             4 : 'Григорий',
             5 : 'Влад'}
        n = random.randint(1,5)
        outd = str(a[n]) + ' ' + str(j) + ' ' + str(i) + '\n'
        indata.write(outd)
    indata.close()


def incons(instock):
    print("Введите номер заменяемой записи")
    k = int(input())
    print("Введите значения через проблел или слитно")
    n, i, j = input().split(' ')
    instock[k] = typeA(n, i, j)


def read_bd():
    indata = open('in.txt')
    for line in indata:
        line = line.strip()
        n, i, j = line.split(' ')
        instock.append(typeA(n, i, j))
    indata.close()


def printcons(instock):
    for k in range(len(instock)):
        pr = instock[k]
        pr.display_type_a()


def wbd(instock):
    outdata = open('in.txt', 'w')
    for k in range(len(instock)):
        s = instock[k]
        outdata.write(s.outd())
    outdata.close()


def prnum(instock):
    print('Введите номер выводимой записи')
    k = int(input())
    instock[k].display_type_a()


def sortby(instock):
    a = {1 : 'name',
         2 : 'bith',
         3 : 'oklad'}
    print('Введите параметр сортировки. 1 - по имени, 2 - по году, 3 - по размеру оклада')
    k = int(input())
    instock = sorted(instock, key=operator.attrgetter(a[k]))
    instock = list(reversed(instock))
    return instock

instock = []

#rand_bd()

read_bd()
incons(instock)
prnum(instock)
printcons(instock)
instock = sortby(instock)
printcons(instock)
wbd(instock)