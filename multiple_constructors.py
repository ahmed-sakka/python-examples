import random 

class Cheese(object):
    def __init__(self, num_holes=0):
        "defaults to a solid cheese"
        self.number_of_holes = num_holes

    def __repr__(self):
        return str(self.number_of_holes)

    @classmethod
    def random(cls):
        return cls(random.randint(0, 100))

    @classmethod
    def slightly_holey(cls):
        return cls(random.randint(0, 33))

    @classmethod
    def very_holey(cls):
        return cls(random.randint(66, 100))
    
    @classmethod
    def cheese10(cls):
        return cls(10)

if __name__ == "__main__":
    gouda = Cheese()
    emmentaler = Cheese.random()
    leerdammer = Cheese.slightly_holey()
    custom1 = Cheese(10)
    print custom1.number_of_holes
    custom2 = Cheese.cheese10()
    print custom2.number_of_holes

    print gouda, emmentaler, leerdammer, custom1, custom2
