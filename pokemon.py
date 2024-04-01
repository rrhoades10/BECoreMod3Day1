# creating a class for individual pokemon
class Pokemon():
    def __init__(self, name, type_, special_attack):
        self.name = name
        self.type_ = type_
        self.special_attack = special_attack

    def make_sound(self):
        print(f"{self.name} makes a cool {self.name} sound")