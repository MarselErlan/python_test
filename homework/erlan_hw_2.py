class Boss:
    def __init__(self, name, time_work, salary):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('name should be string')
        if isinstance(time_work, str):
            self.time_work = time_work
        else:
            raise ValueError('time_work should be string')
        if isinstance(salary, int):
            self.salary = salary
        else:
            raise ValueError('salary should be integer')


    def dinner(self, eat):
        self.salary -= eat


    def __str__(self):
        return f'name:{self.name}\n'\
               f'time_work:{self.time_work}\n' \
               f'salary:{self.salary}$\n'


work = Boss(name='Alex', time_work='10:00-15:00', salary=1000)
work.dinner(100)
print(work)

class Workman(Boss):
    def __init__(self, name, time_work, salary, product):
        super().__init__(name, time_work, salary)
        if isinstance(product, int):
            self.product = product
        else:
            raise ValueError('product should be integer')

    def should_have(self):
        return f'should have a pager {workman}'

    def __str__(self):
        return super(Workman, self).__str__() + f'must sell a product: {self.product}\n'



workman = Workman(name='Dima', time_work='09:00-16:00', salary=500, product=2)
print(workman.dinner(50))
print(workman.should_have())
print(workman)



class Scrubwoman(Workman):
    def __init__(self, name, time_work, salary, product,  paper):
        super().__init__(name, time_work, salary, product,)
        if isinstance(paper, int):
            self.paper = paper
        else:
            raise ValueError('paper should be integer')


    def __str__(self):
        return super(Scrubwoman, self).__str__() + f'evaluation paper : {self.paper}'

scrubwoman = Scrubwoman(name='Aika', time_work='15:00-16:00', salary=300, product=0,  paper=5)
print(scrubwoman.dinner(40))
print(scrubwoman)
