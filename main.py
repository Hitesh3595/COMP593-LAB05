import sys

from poke_api import get_pokemon
from pastebin_api import create_paste


def get_pokemon_name():
    """Gets pokemon name from command line"""
    if len(sys.argv) < 2:
        print("Please provide the pokemon name.")
        exit()
    return sys.argv[1]


def create_paste_using_pokemon_info(pokemon_name, pokemon_info):
    """
    Create a paste using given pokemon information

    Args:
        pokemon_name (str): name or poke-dex of pokemon
        pokemon_info (dict): information about pokemon
    """
    title = f"{pokemon_name.capitalize()}'s Abilities"
    abilities = []
    for ability_obj in pokemon_info["abilities"]:
        abilities.append(ability_obj["ability"]["name"])

    body = "\n".join(abilities)
    expiration = "1M"
    publicly_listed = False
    create_paste(title, body, expiration, publicly_listed)
    return


def main():
    pokemon = get_pokemon_name()
    pokemon_info = get_pokemon(pokemon)
    create_paste_using_pokemon_info(pokemon, pokemon_info)


if __name__ == "__main__":
    main()
