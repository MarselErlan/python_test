class Drink:
    def __init__(self, name, condition, capacity, bottle, cost):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('name should be string')
        if isinstance(condition, str):
            self.condition = condition
        else:
            raise ValueError('condition should be string')
        if isinstance(capacity, float):
            self.capacity = capacity
        else:
            raise ValueError('capacity should be float')
        if isinstance(bottle, str):
            self.bottle = bottle
        else:
            raise ValueError('bottle should be string')
        if isinstance(cost, int):
            self.cost = cost
        else:
            raise ValueError('cost should be integer')


    def sum_drink(self, sum):
        self.cost += sum

    def __str__(self):
        return f'types drink - {self.name}\n' \
               f'temperature a condition - {self.condition}\n' \
               f'capacity bottle - {self.capacity}\n' \
               f'types bottle - {self.bottle}\n' \
               f'cost drink - {self.cost}\n'

drink = Drink(name='drink', condition='warm-cold', capacity=2.0, bottle="glazed-plastic", cost=0)
drink.sum_drink(3000)
print(drink)

class Vodka(Drink):
    def __init__(self, name, condition, capacity, bottle, cost):
        super().__init__(name, condition, capacity, bottle, cost)
        self.name = name
        self.condition = condition
        self.capacity = capacity
        self.bottle = bottle
        self.cost = cost


    def __str__(self):
        return f'types drink - {self.name}\n' \
               f'temperature a condition - {self.condition}\n' \
               f'capacity bottle - {self.capacity}\n' \
               f'types bottle - {self.bottle}\n' \
               f'cost drink - {self.cost}\n'


    def choose(self):
        print("choose vodka:")

vodka = Vodka(name='serebrom', condition='cold', capacity=0.7, bottle="glazed-",  cost=0)
vodka.sum_drink(1200)
vodka.choose()
print(vodka)

class Joice(Drink):
    def __init__(self, name, condition, capacity, bottle, cost):
        super().__init__(name, condition, capacity, bottle, cost)
        self.name = name
        self.condition = condition
        self.capacity = capacity
        self.bottle = bottle
        self.cost = cost

    def choose(self):
        print("choose joice:")

    def __str__(self):
        return f'types drink - {self.name}\n' \
               f'temperature a condition - {self.condition}\n' \
               f'capacity bottle - {self.capacity}\n' \
               f'types bottle - {self.bottle}\n' \
               f'cost drink - {self.cost}\n'

joice = Joice(name='Rich', condition='warm', capacity=1.0, bottle="plastic",  cost=0)
joice.sum_drink(1800)
joice.choose()
print(joice)

class Travel_bag(Vodka, Joice):
    def __init__(self, name, condition, capacity, bottle, cost):
        super().__init__(name, condition, capacity, bottle, cost)
        self.name = name
        self.condition = condition
        self.capacity = capacity
        self.bottle = bottle
        self.cost = cost

    def choose(self):
        print("bought for travel:")

    def __str__(self):
        return f'types drink - {self.name}\n' \
               f'temperature a condition - {self.condition}\n' \
               f'capacity bottle - {self.capacity}\n' \
               f'types bottle - {self.bottle}\n' \
               f'cost drink - {self.cost}\n'

travel_bag = Travel_bag(name='serebrom and Rich', condition='warm and cold', capacity=2.0, bottle="glazed and plastic",  cost=0)
travel_bag.choose()
print(travel_bag)
