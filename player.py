class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.party = []
        

    def __str__(self):
        return "I'm {} and I'm {} years old".format(self.name, self.age)
