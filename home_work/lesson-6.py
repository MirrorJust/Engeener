class Human:
    def __init__(self, gender, old, employment, name):
        self.gender = gender
        self.old = old
        self.employment = employment
        self.name = name

    def see_info(self):
        print(f'Статус занятости - {self.employment}\n'
              f'Возраст - {self.old}\n'
              f'Пол - {self.gender}')

    def see_name(self):
        print(self.name)


class Child(Human):
    def __init__(self, gender, old, employment, name, speech, walk, location):
        super().__init__(gender=gender, old=old, employment=employment, name=name)
        self.speech = speech
        self.walk = walk
        self.location = location

    def see_info(self):
        super().see_info()
        print(f'Может говорить? {self.speech}\n'
              f'Может ходить? {self.walk}')

    def location_change(self, v_location):
        self.location = v_location

    def see_location(self):
        print(f'Текущее положение ребенка - {self.location}')


class Woman(Human):
    def __init__(self, gender, old, employment, name, hair_length):
        super().__init__(gender=gender, old=old, employment=employment, name=name)
        self.hair_length = hair_length

    def see_info(self):
        super().see_info()
        print(f'Длина волос - {self.hair_length}')


class Man(Human):
    def __init__(self, gender, old, employment, name, biceps_in_centimeters):
        super().__init__(gender=gender, old=old, employment=employment, name=name)
        self.biceps_in_centimeters = biceps_in_centimeters

    def see_info(self):
        super().see_info()
        print(f'Размер бицухи - {self.biceps_in_centimeters}')


class Bus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def see_passengers(self):
        name_pass = []
        for i in self.passengers:
            name_pass.append(i.see_name())
        return name_pass

    def add_passenger(self, obj):
        self.passengers.append(obj)

    def del_passenger(self, obj):
        self.passengers.remove(obj)

    def change_station(self, name_location):
        for passenger in self.passengers:
            passenger.location_change(name_location)


# child1 = Child('male', 7, 'no', "Jonh Pol",  1, 1, 'home')
# child2 = Child('female', 10, 'no', "Cristy", 1, 1, 'home')
# bus_general = Bus()
#
# bus_general.add_passenger(child1)
# bus_general.add_passenger(child2)
#
# bus_general.see_passengers()
#
# child1.see_location()
# bus_general.change_station('school')
# child1.see_location()
