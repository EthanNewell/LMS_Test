import time
 
 
class MailClient:
    def __init__(self):
        self.GLOBAL_DATA = {'Global': {}, 'South America': {}, 'North America': {},
                            'Europe': {}, 'Asia': {}, 'Australia': {}, 'Other': {}}
 
    def register(self, server):
        login = input('Введите логин: ')
        if login.lower() == 'отменить команду':
            print('Команда отменена')
            return False
        password = input('Введите пароль: ')
        if password.lower() == 'отменить команду':
            print('Команда отменена')
            return False
        while login in self.GLOBAL_DATA[server].keys():
            print(f'Пользователь на сервере {server} с логином {login} уже есть, придумайте другой')
            login = input('Введите логин: ')
            if login.lower() == 'отменить команду':
                print('Команда отменена')
                return False
            password = input('Введите пароль: ')
            if password.lower() == 'отменить команду':
                print('Команда отменена')
                return False
        self.GLOBAL_DATA[server][login] = {}
        self.GLOBAL_DATA[server][login]['password'] = password
        self.GLOBAL_DATA[server][login]['mail'] = []
        print('Вы успешно зарегистрировались!')
        return login, password
        
    def read_mails(self, login, server):
        if len(self.GLOBAL_DATA[server][login]['mail']) == 0:
            print('У вас нет новых сообщений')
        else: 
            for i in self.GLOBAL_DATA[server][login]['mail']:
                print(f'''Сообщение от пользователя {i[0]}:
{i[1]}''')
                time.sleep(3)
                print('-----------------------------------')
            print('Все сообщения просмотрены')
            self.GLOBAL_DATA[server][login]['mail'] = []
        
    def write_mail(self, login, server):
        who = input('Кому хотите написать письмо?')
        if who.lower() == 'отменить команду':
            print('Команда отменена')
            return False
        while who not in self.GLOBAL_DATA[server]:
            print(f'Пользователя на сервере {server} с логином {who} не существует, повторите ввод')
            who = input()
            if who.lower() == 'отменить команду':
                print('Команда отменена')
                return False
        text = input('''Введите текст сообщения:
''')
        self.GLOBAL_DATA[server][who]['mail'].append([login, text])
        print(f'Сообщение пользователю {who} успешно отправлено')
        return True
 
    
def main():
    now_server = False
    now_login = False
    now_password = False
    print('''Ты попал на самый профессиональный почтовый сервис!
Если ты здесь - ты точно особенный.''')
    print('''Список команд:
1)Стандартные:
    Войти на сервер
    Выйти с сервера
    Войти в аккаунт
    Выйти из аккаунта
    Создать аккаунт
    Проверить почту
    Написать письмо
    Отменить команду(когда одна из команд запущена)
    Выйти с сервиса
        ''')
    print('Правило: нельзя устанавливать имя сервера, логин или пароль на: отменить команду')
    MAIN_COMAND = MailClient()
    while True:
        comand = input('Введите команду: ').lower().strip()
        if comand == 'войти на сервер':
            print('Список доступных серверов:')
            print(', '.join(MAIN_COMAND.GLOBAL_DATA.keys()))
            server = input('Введите имя нужного сервера: ')
            while server not in MAIN_COMAND.GLOBAL_DATA:
                print('Такого сервера не существует, повторите ввод')
                server = input()
                if server.lower() == 'отменить команду':
                    print('Команда отменена')
                    break
            if server in MAIN_COMAND.GLOBAL_DATA:
                print(f'Вы успешно вошли на сервер {server}')
                now_server = server
        elif comand == 'выйти с сервера':
            if now_server is False:
                print('Вы еще не на сервере')
            else:
                print(f'Вы вышли с сервера {now_server}')
                now_server = False
                now_login = False
                now_password = False
        elif comand == 'создать аккаунт':
            if now_server is not False:
                sys_answer = MAIN_COMAND.register(now_server)
                if sys_answer is not False:
                    now_login, now_password = sys_answer
            else:
                print('Вы не вошли на сервер')
        elif comand == 'войти в аккаунт':
            if now_server is False:
                print('Вы не зашли на сервер')
            else:
                login = input('Введите логин: ')
                if login.lower() == 'отменить команду':
                    print('Команда отменена')
                    continue
                password = input('Введите пароль: ')
                if password.lower() == 'отменить команду':
                    print('Команда отменена')
                    continue
                else:
                    while True:
                        if login not in MAIN_COMAND.GLOBAL_DATA[server].keys():
                            print('Произошла ошибка! Повторите ввод')
                            login = input('Введите логин: ')
                            if login.lower() == 'отменить команду':
                                print('Команда отменена')
                                continue
                            password = input('Введите пароль: ')
                            if password.lower() == 'отменить команду':
                                print('Команда отменена')
                                continue
                        elif MAIN_COMAND.GLOBAL_DATA[server][login]['password'] != password:
                            print('Произошла ошибка! Повторите ввод')
                            login = input('Введите логин: ')
                            if login.lower() == 'отменить команду':
                                print('Команда отменена')
                                continue
                            password = input('Введите пароль: ')
                            if password.lower() == 'отменить команду':
                                print('Команда отменена')
                                continue
                        else:
                            now_login = login
                            now_password = password
                            print('Вы успешно вошли!')
                            break
        elif comand == 'выйти из аккаунта':
            print('Вы вышли из аккаунта')
            now_login = False
        elif comand == 'написать письмо':
            if now_server is False or now_login is False:
                print('Для того, чтобы написать письмо нужно войти на сервер и в аккаунт')
            else:
                sys_answer = MAIN_COMAND.write_mail(now_login, now_server)
        elif comand == 'проверить почту':
            if now_server is False or now_login is False:
                print('Для того, чтобы проверить почту нужно войти на сервер и в аккаунт')
            else:
                sys_answer = MAIN_COMAND.read_mails(now_login, now_server)
        elif comand == 'выйти с сервиса':
            print('Выход...')
            break
        else:
            print('Команда не распознана, повторите ввод')
 
 
main()
