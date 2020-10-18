import os.path
import contact as cont


filename = 'dict.txt'


def main():
    dict = {}

    if os.path.isfile(filename):
        f = open(filename, 'r')
        for line in f:
            name, number, email = line.split()
            dict[name] = cont.Contact(name, number, email)
        f.close()

    while True:
        print('Что вы хотите сделать?')
        print('1. Найти контакт')
        print('2. Добавить контакт')
        print('3. Удалить контакт')
        print('4. Вывести список всех контактов')
        print('5. Выйти')
        print()

        n = input('Ваш выбор: ')
        if n == '1':
            s = input('Введите имя: ')
            if s not in dict:
                print('Контакт не найден')
            else:
                name, number, email = str(dict[s]).split()
                print('Имя: {}'.format(name))
                print('Телефон: {}'.format(number))
                print('Email: {}'.format(email))

        elif n == '2':
            name = input('Введите имя: ')
            number = input('Введите телефон: ')
            email = input('Введите email: ')
            dict[name] = cont.Contact(name, number, email)

        elif n == '3':
            name = input('Введите имя: ')
            if name not in dict:
                print('Контакт не найден')
            else:
                dict.pop(name)
                print('Контакт удален')

        elif n == '4':
            print('\nСписок контактов:\n')
            for contact in dict:
                print(str(dict[contact]))
            print()

        elif n == '5':
            f = open(filename, 'w')
            for contact in dict:
                f.write(str(dict[contact]) + '\n')
            f.close()
            break

        else:
            print('Ошибка! Введите номер желаемого действия')

main()
