import requests

GET_POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(pokemon):
    """
    Gets the pokemon.

    Args:
        pokemon (str): name or poke-dex of pokemon
    
    Return:
        if pokemon found:
            pokemon info (abilities, moves, species)
        if pokemon not found:
            None
    """
    pokemon = str(pokemon).strip().lower()
    print(f"Getting information for {pokemon}...",end="")
    response = requests.get(GET_POKEMON_URL + pokemon)
    if response.status_code == 200:
        print("success")
        return response.json()
    else:
        print("failure")
        print(f"Response code: {response.status_code} ({response.reason})")
    return None

