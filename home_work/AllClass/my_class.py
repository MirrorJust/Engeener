import datetime


class Human:
    def __init__(self, id_man, name, old, birthday):
        self.__id = id_man
        self.__name = name
        self.__old = old
        self.__birthday = datetime.datetime.strptime(birthday, "%d.%m.%Y").strftime("%d.%m.%Y")

    def get_info(self):
        return self.__id, self.__name, self.__old, self.__birthday

    def print_info(self):
        print(f'Номер жетона: {self.__id}\n'
              f'Имя: {self.__name}\n'
              f'Возраст: {self.__old}')


class Company:
    def __init__(self, id_company, list_human=None):
        if list_human is None:
            list_human = []
        self.__list_human = list_human
        self.__id_company = id_company

    def add_human(self, *args):
        try:
            for i in args:
                if not isinstance(i, Human):
                    raise TypeError(f'В параметр введен не верный тип данных: {type(i)}')
                self.__list_human.append(i)
        except TypeError as e:
            print(f'Ошибка добавления:\n{e}')

    def del_human(self, obj):
        try:
            if not isinstance(obj, Human):
                raise TypeError(f'В параметр введен не верный тип данных: {type(obj)}')
            for i in self.__list_human:
                if obj.get_info()[0] == i.get_info()[0]:
                    self.__list_human.remove(i)
        except TypeError as e:
            print(f'Ошибка удаления:\n{e}')

    def print_company_human_info(self):
        counter = 1
        for i in self.__list_human:
            print(f'Человек № {counter} в роте:\n'
                  f'\tНомер жетона: {i.get_info()[0]}\n'
                  f'\tИмя: {i.get_info()[1]}\n'
                  f'\tВозраст: {i.get_info()[2]}\n'
                  f'\tДата рождения {i.get_info()[3]}')
            counter += 1

    def get_company_human_info(self):
        all_human_company = []
        for i in self.__list_human:
            human_company = {
                'id_man': i.get_info()[0],
                'name_man': i.get_info()[1],
                'old_man': i.get_info()[2],
            }
            all_human_company.append(human_company)

        return all_human_company


class Regiment:
    def __init__(self, list_company=None):
        if list_company is None:
            list_company = []
        self.__list_company = list_company

    def add_company(self, *args):
        try:
            for i in args:
                if not isinstance(i, Company):
                    raise TypeError(f'Ошибка введенного типа данных: {type(i)}')
                self.__list_company.append(i)
        except TypeError as e:
            print(f'Ошибка добавления роты:\n\t{e}')

    def del_company(self, obj):
        for i in self.__list_company:
            if obj == i:
                self.__list_company.remove(i)

    def print_all_human_regiment(self):
        for i in self.__list_company:
            for y in i.get_company_human_info():
                print(f'Номер жетона: {y["id_man"]}, имя: {y["name_man"]}, возраст: {y["old_man"]}')
