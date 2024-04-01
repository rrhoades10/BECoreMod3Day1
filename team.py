class Team():
    def __init__(self):
        self.team = []

    def catch_pokemon(self, pokemon):
        self.team.append(pokemon)

    def i_choose_you(self, name):
        for pokemon in self.team:
            if pokemon.name == name:
                print(f"I CHOOSE YOU! {name}")
                break
        else:
            print(f"You haven't caught {name} yet!")
    
    def view_team(self):
        if not self.team:
            print("You haven't caught any pokemone yet....noob!")
        else:
            for pokemon in self.team:
                print(f"{pokemon.name} is a {pokemon.type_} type and its special attack is {pokemon.special_attack}")


        
        