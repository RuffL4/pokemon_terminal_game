import pokemons as p
import random
from colorama import Fore



def battle(player):
    wild_pokemon = generate_wild_pokemon()
    print(f"A wild pokemon appered! It is:\n{Fore.RED}{wild_pokemon.class_info()}{Fore.RESET}")
    selected_pokemon = select_your_pokemon(player)
    if selected_pokemon is None:
        print("You have no Pokémon available to fight. Battle canceled.")
        return
    while wild_pokemon.is_alive():
        if selected_pokemon.is_dead():
            selected_pokemon = select_your_pokemon(player)
            if selected_pokemon is None:
                print("You lost the battle! Please go to pokemon center and heal your pokemons")
                return
        action = input("type: attack for attacking the wild pokemon or switch for switching your pokemon: ").lower()
        if action == "attack":
            your_damage_turn(wild_pokemon, selected_pokemon)
            if wild_pokemon.is_alive():
                wild_damage_turn(wild_pokemon, selected_pokemon)
        elif action == "switch":
            if len(available_pokemons(player, selected_pokemon)) > 0:
                selected_pokemon = select_your_pokemon(player, selected_pokemon)
                print(f"You switched to {selected_pokemon.__class__.__name__}")
            else:
                print("You cant switch to another pokemon!")
        else:
            print("You must type 'attack' or 'switch'")
    if wild_pokemon.is_dead() and not_partymember(player, wild_pokemon):
        print("congratulations you won!")
        catch_pokemon(player, wild_pokemon)
    else:
        print(f"You cant catch this wild {wild_pokemon.__class__.__name__} because you have already one {wild_pokemon.__class__.__name__}")


def generate_wild_pokemon():
    wild_pokemons = [cls for cls in p.Pokemon.__subclasses__()]
    wild_pokemon_class = random.choice(wild_pokemons)
    return wild_pokemon_class()


def select_your_pokemon(player, current_pokemon=None):
    living = available_pokemons(player, exclude=current_pokemon)
    if len(living) == 1:
        chosen = living[0]
        print(f"{chosen.__class__.__name__} was chosen because it's the only one available!")
        return chosen
    if len(living) == 0:
        return
    print_pokemon_list(living)
    while True:
        try:
            choice = int(input(f"Your choice (1-{len(living)}): "))
            if 1 <= choice <= len(living):
                chosen = living[choice - 1]
                print(f"You chose {chosen.__class__.__name__}")
                return chosen
            print(f"Please enter a number between 1 and {len(living)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def available_pokemons(player, exclude=None):
    return [pokemon for pokemon in player.party if pokemon.is_alive() and pokemon != exclude]


def your_damage_turn(wild_pokemon, selected_pokemon):
    damage = selected_pokemon.attack - (wild_pokemon.defence - 40)
    wild_pokemon.take_damage(damage)
    print(f"wild {wild_pokemon.__class__.__name__} took {damage} damage")
    print(f"wild {wild_pokemon.__class__.__name__}'s current hp is {wild_pokemon._current_hp}")


def wild_damage_turn(wild_pokemon, selected_pokemon):
    damage = wild_pokemon.attack - (selected_pokemon.defence - 20)
    selected_pokemon.take_damage(damage)
    print(f"Your {selected_pokemon.__class__.__name__} took {damage} damage")
    print(f"Your {selected_pokemon.__class__.__name__}'s current hp is {selected_pokemon._current_hp}")


def catch_pokemon(player, wild_pokemon):
    while True:
        choice = input(f"Do u want to catch this wild {wild_pokemon.__class__.__name__}? (yes/no) ").lower()
        if choice == "yes":
            wild_pokemon.name = input(f"How do you want to call your {wild_pokemon.__class__.__name__}: ")
            player.party.append(wild_pokemon)
            print(f"{wild_pokemon.__class__.__name__} was caught!")
            return
        elif choice == "no":
            return
        else:
            print("you have to type yes or no!")


def not_partymember(player, wild_pokemon):
    for pokemon in player.party:
        if pokemon.__class__.__name__ == wild_pokemon.__class__.__name__:
            return False
    return True


def print_pokemon_list(pokemons):
    print("Available Pokémon:")
    for i, p in enumerate(pokemons, 1):
        print(f"{Fore.GREEN}{i}. {p.self_info()}{Fore.RESET}")
