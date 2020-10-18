class Contact:
    def __init__(self, name, number, email):
        self.__name = name
        self.__number = number
        self.__email = email

    def get_name(self):
        return 'Имя: {}'.format(self.__name)

    def get_number(self):
        return 'Телефон: {}'.format(self.__number)

    def get_email(self):
        return 'Email: {}'.format(self.__email)

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return '{} {} {}'.format(self.__name, self.__number, self.__email)