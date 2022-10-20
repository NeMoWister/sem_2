import operator


class lab4:
    '''Структура'''

    def __init__(self, gosnum, model, secondname, date, mon, year):
        self.gosnum = gosnum
        self.model = model
        self.secondname = secondname
        self.date = date
        self.mon = mon
        self.year = year

    def display_type_a(self):
        print('Госномер: {}, Модель {}, Фамилия: {}, День, Месяц, Год: {}.{}.{}'.format(self.gosnum, self.model, self.secondname, self.date, self.mon, self.year))


def fromcons(bd):
    print("Введите значения через проблел или слитно в формате: Госномер, Модель, Фамилия, Дата угона.")
    n, i, j, k = input().split(' ')
    k, t, r = k.split('.')
    bd.append(lab4(n, i, j, k, t, r))


bd = []
print('Сколько записей вы хотите завести?')
k = int(input())
for i in range(k):
    fromcons(bd)
bd = sorted(bd, key=operator.attrgetter('year', 'mon', 'date'))
for k in range(len(bd)):
    bd[k].display_type_a()
