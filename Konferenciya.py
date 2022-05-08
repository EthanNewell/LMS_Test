import datetime as dt
from random import choice
 
 
class Konferencia:
 
    def __init__(self):
        self.elem0 = dict()
 
    def zadatvremya(self, time, vrem, dlit, name):
        time = time.split('.')
        time = dt.datetime(int(time[-1]), int(time[-2]), int(time[-3]))
        vrem = vrem.split(':')
        delta_time1 = dt.timedelta(hours=int(vrem[0]), minutes=int(vrem[1]))
        time = time + delta_time1
        dlit = dlit.split(', ')
        dlit = dt.timedelta(hours=int(dlit[0]), minutes=int(dlit[1]))
        okonch = time + dlit
        self.elem0[name] = time, okonch
 
    def vernut(self, name):
        return self.elem0[name]
 
    def vernutvse(self):
        return self.elem0
 
    def delete(self, name):
        del self.elem0[name]
 
    def proverka(self, time, vrem, dlit):
        time = time.split('.')
        time = dt.datetime(int(time[-1]), int(time[-2]), int(time[-3]))
        vrem = vrem.split(':')
        delta_time1 = dt.timedelta(hours=int(vrem[0]), minutes=int(vrem[1]))
        time = time + delta_time1
        dlit = dlit.split(', ')
        dlit = dt.timedelta(hours=int(dlit[0]), minutes=int(dlit[1]))
        okonch = time + dlit
        for i in self.elem0:
            if (time <= self.elem0[i][0]) and (okonch <= self.elem0[i][1])\
                    and (okonch >= self.elem0[i][0]):
                return False
            elif (time >= self.elem0[i][0]) and (time <= self.elem0[i][1]):
                return False
        return True
 
    def vremyapererv(self):
        time0 = dt.datetime(3000, 1, 1)
        time1 = dt.datetime(1, 1, 1)
        if len(self.elem0) > 1:
            for i in self.elem0:
                if self.elem0[i][1] < time0:
                    time0 = self.elem0[i][1]
            for i in self.elem0:
                if self.elem0[i][0] > time1:
                    time1 = self.elem0[i][0]
            return time1 - time0
        else:
            return'У вас нет достаточного количества докладов'
 
 
class Doklad(Konferencia):
 
    def vernutdoklad(self, chislo):
        a = []
        for i in range(chislo + 1):
            a.append(i)
        a[0] = 'Гран-При'
        print('Ваш доклад получен')
        print(f'Вы заняли МЕСТО {choice(a)}!!!!!!!!!!!!!!!ПОЗДРАВЛЯЮ!!!!!')
 
 
def main():
    while True:
        print('Добрый день, вас приветствует создатель вашего расписания конференции.')
        print('Что вы хотите сделать?')
        r = Konferencia()
        d = Doklad()
        while True:
            print('1)Создать новый доклад-------2)Показать время определенного доклада'
                  '---3)Показать все доклады и их время---------4)Удалить доклад--------'
                  '5)Показать время самого продолжительного перерыва между докладами-----'
                  '6)Создать новую конференцию------'
                  '----7)Отправить один из ваших докладов на конкурс)')
            s = int(input())
            if s == 1:
                print('Название этого доклада')
                name = input()
                print('Его дата в формате: ЧЧ.MM.ГОД')
                data = input()
                print('Его время в формате: ЧЧ:ММ')
                time = input()
                print('Длительность вашего доклада в формате: число часов, число минут')
                dlit = input()
                if r.proverka(data, time, dlit):
                    r.zadatvremya(data, time, dlit, name)
                    print('Поздравляю, вы создали новый доклад!')
                else:
                    print('ВНИМАНИЕ!ЭТОТ ДОКЛАД ПЕРЕКРЫВАЕТ ВРЕМЯ ДРУГОГО!!!!!!'
                          'ОН НЕ БУДЕТ СОЗДАН......')
            if s == 2:
                print('Название этого доклада')
                for i in r.vernutvse():
                    print(f'{i}')
                name1 = input()
                print(f'Начало:{r.vernut(name1)[0].strftime("%d.%m.%Y %H:%M")}, '
                      f'Окончание:{r.vernut(name1)[1].strftime("%d.%m.%Y %H:%M")}')
            if s == 3:
                for i in r.vernutvse():
                    print(f'{i} : Начало:{r.vernutvse()[i][0].strftime("%d.%m.%Y %H:%M")},'
                          f' Окончание:{r.vernutvse()[i][1].strftime("%d.%m.%Y %H:%M")}.')
            if s == 4:
                print('Название этого доклада')
                for i in r.vernutvse():
                    print(f'{i}')
                name3 = input()
                r.delete(name3)
            if s == 5:
                print(r.vremyapererv())
            if s == 6:
                print('Вы точно хотите это сделать?')
                otvet = input()
                if otvet == 'Да':
                    break
            if s == 7:
                print('Какой доклад вы хотите отправить?')
                for i in r.vernutvse():
                    print(f'{i}')
                print(f'ИТААААККК ВАШ ДОКЛАД С ИМЕНЕМ {input()} ОТПРАВЛЯЕТСЯ НА КОНКУРС!!!!!!!')
                d.vernutdoklad(len(r.vernutvse()))
# Запустите main()
