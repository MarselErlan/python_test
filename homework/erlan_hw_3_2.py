class Best_friends:
    def __init__(self, name,  gender, contemporary, long_time):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('name should be stringer')
        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('gender should be stringer')
        if isinstance(contemporary, bool):
            self.contemporary = contemporary
        else:
            raise ValueError('contemporary should be bool')
        if isinstance(long_time, int):
            self.long_time = long_time
        else:
            raise ValueError('long_time should be integer')




    def __str__(self):
        return f'name:{self.name}\n' \
               f'gender:{self.gender}\n' \
               f'contemporary:{self.contemporary}\n' \
               f'long_time:{self.long_time}\n'


class Boki(Best_friends):
    def __init__(self, name, gender, contemporary, long_time):
        super().__init__(name, gender, contemporary, long_time)

    def surname(self, family):
        return f'Surname is  {family}'

    def __str__(self):
        return super(Boki, self).__str__()
boki = Boki( name="Bakbergen", gender="M", contemporary=True, long_time=12)
print(boki.surname('Abdimannapov'))
print(boki)


class Ajo(Best_friends):
    def __init__(self, name, gender, contemporary, long_time):
        super().__init__(name, gender, contemporary, long_time)

    def surname(self, family):
        return f'Surname is  {family}'
    def __str__(self):
        return super(Ajo, self).__str__()

ajo = Ajo( name="Akjol", gender="M", contemporary=True, long_time=12)
print(ajo.surname('Dosmatov'))
print(ajo)



class Alman(Best_friends):
    def __init__(self, name, gender, contemporary, long_time):
        super().__init__(name, gender, contemporary, long_time)

    def surname(self, family):
        return f'Surname is  {family}'

    def __str__(self):
        return super(Alman, self).__str__()

alman = Alman( name="Almanbet", gender="M", contemporary=True, long_time=11)
print(alman.surname('Baktybekov'))
print(alman)
