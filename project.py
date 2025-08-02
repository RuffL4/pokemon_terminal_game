import pokemons as p
from player import Player
import random
from colorama import Fore
import battle


def main():
    player = create_player()
    choose_starter(player)
    while True:
        try:
            print("What do u want to do?")
            print("Type 1 if you want to battle")
            print("Type 2 if you want to go to pokemon center to heal your pokemons")
            print("Type 3 if you want to get information about your pokemon")
            choice = int(input("Your Choice: "))
            if choice == 1:
                battle.battle(player)
            elif choice == 2:
                pokemon_center(player)
            elif choice == 3:
                pokemon_information(player)
            else:
                print("No type right number")
        except ValueError:
            print("No type the right number for the activity!")
            continue


def create_player():
    print("Hey trainer!")
    player = Player(input("What's your name? "), input("How old are you? "))
    return player


def choose_starter(player):
    print("Now it's time to choose your first pokemon!")
    print(f"You can choose: ")
    starter_pokemons = [p.Bulbasaur, p.Charmander, p.Squirtle]
    for i, starter in enumerate(starter_pokemons):
        print(f"{Fore.RED}{i + 1}. {starter.class_info()}{Fore.RESET}")
    while True:
        try:
            choice = int(input("Your choice (1-3):  "))
            for i, starter in enumerate(starter_pokemons):
                if choice == i+1:
                    print(f"{starter.__name__} is a great choice!")
                    first_pokemon = starter(input(f"How do u want to call your {starter.__name__}: "))
                    player.party.append(first_pokemon)
                    return first_pokemon
            print("No, press 1 for Bulbasaur, 2 for Charmander, 3 for Squirtle")
        except ValueError:
            print("No, press 1 for Bulbasaur, 2 for Charmander, 3 for Squirtle")
            continue


def pokemon_center(player):
    for pokemon in player.party:
        if pokemon.current_hp < pokemon.max_hp:
            pokemon.current_hp = pokemon.max_hp
            print(f"{pokemon.__class__.__name__} was healed! {pokemon.__class__.__name__} current hp is: {pokemon.current_hp}/{pokemon.max_hp}")
    print("Every pokemon is full hp!")


def pokemon_information(player):
    for pokemon in player.party:
        print(pokemon.self_info())


if __name__ == "__main__":
    main()
