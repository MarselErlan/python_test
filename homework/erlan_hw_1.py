class Animal:
    def __init__(self, name,  blood, size, speed, color, teeth, skin, feeds, length, weight):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('name should be string')
        if isinstance(blood, str):
            self.blood = blood
        else:
            raise ValueError('blood should be string')
        if isinstance(size, str):
            self.size = size
        else:
            raise ValueError('size should be string')
        if isinstance(speed, int):
            self.speed = speed
        else:
            raise ValueError('speed should be int')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('color should be str')
        if isinstance(teeth, int):
            self.teeth = teeth
        else:
            raise ValueError('teeth should be int')
        if isinstance(skin, str):
            self.skin = skin
        else:
            raise ValueError('skin should be str')
        if isinstance(feeds, str):
            self.feeds = feeds
        else:
            raise ValueError('feeds should be str')
        if isinstance(length, float):
            self.length = length
        else:
            raise ValueError('length should be integer')
        if isinstance(weight, int):
            self.weight = weight
        else:
            raise ValueError('weight should be integer')


    def __str__(self):
        return f'name: {self.name}\n' \
               f'blood: {self.blood}\n' \
               f'size: {self.size}\n' \
               f'max speed: {self.speed}km/h\n' \
               f'color: {self.color}\n' \
               f'teeth: {self.teeth}\n' \
               f'skin: {self.skin}\n' \
               f'feeds: {self.feeds}\n' \
               f'length: {self.length}m\n' \
               f'weight: {self.weight}kg'
mammals = Animal(name='mammals_bear', blood='warm_blooded', size='big', speed=56, color='brown', teeth=42, skin='wool', feeds='omnivorous', length=2.8, weight=600)
print(mammals)


class Birds(Animal):
    def __init__(self, name, blood, size, speed, color, teeth, skin, feeds, length, weight, wingspan):
        super().__init__(name, blood, size, speed, color, teeth, skin, feeds, length, weight)
        if isinstance(wingspan, float):
            self.wingspan = wingspan
        else:
            raise ValueError('wingspan should be integer')

    def __str__(self):
        return super(Birds, self).__str__() + f'\nwingspan : {self.wingspan}m'
#
birds1 = Birds(name='birds_seagull', blood='warm_blooded', size='small', speed=110, color='white', teeth=0, skin='feather', feeds='little fishes, insects', length=0.6, weight=2, wingspan=1.6)
print(birds1)
print('''


''')

class Zoo_show:
    def __init__(self, cost, start, finish, animals, types_1, types_2):
        if isinstance(cost, int):
            self.cost = cost
        else:
            raise ValueError('cost should be int')
        if isinstance(start, float):
            self.start = start
        else:
            raise ValueError('start should be integer')
        if isinstance(finish, float):
            self.finish = finish
        else:
            raise ValueError('finish should be integer')
        if isinstance(animals, str):
            self.animals = animals
        else:
            raise ValueError('animals should be str')
        if isinstance(types_1, str):
            self.types_1 = types_1
        else:
            raise ValueError('types_1 should be str')
        if isinstance(types_2, str):
            self.types_2 = types_2
        else:
            raise ValueError('types_2 should be str')


    def __str__(self):
        return f'average cost: {self.cost}\n' \
               f'the show starts: {self.start}\n' \
               f'and finish: {self.finish}\n' \
               f'for example there will be animals: {self.animals}\n' \
               f'there will be two shows \ntypes_1: {self.types_1}\n' \
               f'types_2: {self.types_2}\n'

zoo_show = Zoo_show(cost=500, start=10.35, finish=11.35, animals="Bear, Tiger, Elephant, Monkey,  Lion, etc", types_1="mammals", types_2="birds")
print(zoo_show)
print("shoose mammals or birds")
class Ticket(Zoo_show):
    def __init__(self, cost, start, finish, animals, types_1, types_2):

        super().__init__(cost, start, finish, animals, types_1, types_2)
        if isinstance(types_1, str):
            self.types_1 = types_1
            self.types_2 = types_2

            if types_1 == input():
                print("the show with mammals_bear")
                print("your ticket-->600 KGS")
            else:
                print("your ticket-->400 KGS")
                print("the show with birds_seagull")
        else:
            raise ValueError('cap should be str')



    def __str__(self):
        return f'the show starts: {self.start}\n' \
               f'and finish: {self.finish}\n'






ticket = Ticket(cost=500, start=11.35, finish=12.35, animals="Bear, Tiger, Elephant, Monkey,  Lion, etc", types_1="mammals", types_2="birds")
print(ticket)
