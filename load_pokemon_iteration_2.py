"""
ECOR 1042
Case study: iterative, incremental development of a pokemon game
that uses Python's str, list, set and dict types.

Last edited: May12, 2023

Copy right: Dr. Rami Sabouni

Iteration 2:
- Demonstrate that we can open a text file and read and print
  the text, one line at a time.
"""

def load_pokemon(file_name : str) -> list[dict]:
    """Return a list of dictionaries containing unique pokemon data read from file_name
    
    Preconditions: file_name has the following columns
                   ['name', 'attack', 'defense', 'hp', 'pokedex_number',
                    'speed', 'type1', 'type2', 'generation']
    >>> load_pokemon("pokemon_test.csv")
    [{'name': 'abomasnow', 'attack': 132, 'defense': 105, 'hp': 90,
    'pokedex_number': 460, 'speed': 30, 'type1': 'grass', 'type2': 'ice',
    'generation': 4},
    {Next item},
    ...]
    """
    in_file = open(file_name, 'r') 

    for line in in_file:
        print(line)

    in_file.close()

    return []

# Main script    
if __name__ == "__main__":
    file_name = 'pokemon_test.csv'
    
    # Load the values from the csv file
    pokemons = load_pokemon(file_name)
    
    
    
