class Patient:
    def __init__(self, first_name, second_name, surname,
                 city, phone_num, additional_phone_num, procedure=[]):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__surname = surname
        self.__city = city
        self.__phone_num = phone_num
        self.__additional_phone_num = additional_phone_num
        self.__procedure = procedure

    def get_name(self):
        return self.__first_name

    def set_name(self, name):
        self.__first_name = name

    def get_second_name(self):
        return self.__second_name

    def set_second_name(self, second_name):
        self.__second_name = second_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_procedure(self):
        list_procedure = []
        for i in self.__procedure:
            list_procedure.append([i.get_name_pr(),
                                   i.get_data_pr(),
                                   i.get_name_doc(),
                                   i.get_price_pr()])
        return list_procedure

    def set_procedure(self, list_pr: list):
        for i in list_pr:
            self.__procedure.append(i)

    def get_phone_num(self):
        return self.__phone_num

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    def get_additional_phone_num(self):
        return self.__additional_phone_num

    def set_additional_phone_num(self, additional_phone_num):
        self.__additional_phone_num = additional_phone_num


class Procedure:
    def __init__(self, name_pr, data_pr, name_doc, price_pr):
        self.__name_pr = name_pr
        self.__data_pr = data_pr
        self.__name_doc = name_doc
        self.__price_pr = price_pr

    def get_name_pr(self):
        return self.__name_pr

    def set_name_pr(self, name_pr):
        self.__name_pr = name_pr

    def get_data_pr(self):
        return self.__data_pr

    def set_data_pr(self, data_pr):
        self.__data_pr = data_pr

    def get_name_doc(self):
        return self.__name_doc

    def set_name_doc(self, name_doc):
        self.__name_doc = name_doc

    def get_price_pr(self):
        return self.__price_pr

    def set_price_pr(self, price_pr):
        self.__price_pr = price_pr


def create_patient():
    new_patient = Patient('Lex', 'Bronkov', 'Strnovich', 'LA', 6609844, 66998442)
    return new_patient


def create_procedure_for_patient(patient):
    first_procedure = Procedure('врачебный осмотр', '22.04.2024', 'Ирвин', 2580)
    second_procedure = Procedure('рентгеноскопия', '22.04.2024', 'Джемисон', 500)
    third_procedure = Procedure('анализ крови', '22.04.2024', 'Смит', 200)

    patient.set_procedure([first_procedure, second_procedure, third_procedure])
    return patient


def all_cost_procedure(patient):
    general_sum = 0
    for list_pr in patient.get_procedure():
        general_sum += list_pr[3]

    return general_sum


def get_info(patient):
    print(f'Имя пациента: {patient.get_name()}\n'
          f'Фамилия пациента: {patient.get_second_name()}\n'
          f'Отчество пациента: {patient.get_surname()}\n'
          f'Город проживания пациента: {patient.get_city()}\n'
          f'Телефон пациента: {patient.get_phone_num()}\n'
          f'Телефон для экстренной связи с близкими: {patient.get_additional_phone_num()}')

    print('-----------------------------')

    print('Пройденные процедуры: ')
    i = 1
    for list_pr in patient.get_procedure():
        print(f'{i}) {list_pr[0]}')
        i += 1

    print('-----------------------------')

    print(f'Общая стоимость процедур составляет: {all_cost_procedure(patient)}')


patient_John = create_patient()
create_procedure_for_patient(patient_John)
get_info(patient_John)
