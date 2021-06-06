class Rider:
    def __init__(self, name):
        self.name = name

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

r = Rider("a-san")

uma = Horse("makibao-", r)

print(uma.rider.name)

