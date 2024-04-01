from pokemon import Pokemon
from team import Team

my_team = Team()
while True:
    action = input("What would you like to do? (catch, view, choose, quit): ").lower()
    if action == "quit":
        print("Well i guess you'll never be a Pokemon Master, N00B... （︶^︶）")
        break

    try: 
        if action == "catch":
            name = input("Who are you catching? ")
            type_ = input("What is the typing? ")
            spesh = input("What is the pokemon's special attack? ")
            my_team.catch_pokemon(Pokemon(name, type_, spesh))
            print(f"Congratulations! You caught a {name}")
        elif action == "view":
            my_team.view_team()

        elif action == "choose":
            name = input("Who will you send out? ")
            my_team.i_choose_you(name)

    except Exception as e:
        print(f"an error occurred: {e}")
print("Saving....please don't turn off the power....")
print("BOODALEEE")

