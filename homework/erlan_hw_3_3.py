class Cinema():
    pass




class Starbaks():
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('name should be stringer')

    def __str__(self, name):
        self.name = name
        if len(name) > 5:
            print(name[:5])
your_name = Starbaks(name="erlann")
print(your_name)