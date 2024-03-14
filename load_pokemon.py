"""
ECOR 1042
Case study: iterative, incremental development of a pokemon game
that uses Python's str, list, set and dict types.

Last edited: May12, 2023

Copy right: Dr. Rami Sabouni

Final Iteration:
- Demonstrate that we can read a line from a text file and split 
  the line into a list of words.
- The first line read from the csv file will be the table header and
  every line after is data from the table.
- The values in each line is stored into a dictionary.
- Fix the value type for each item
- Add the dictionary to our final list
- This is repeated until every line has been read and processed.
- Create a function to add the total stats for each pokemon
"""

def load_pokemon(file_name : str) -> list[dict]:
    # Function body not shown
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
    
    
	string_elements = [0, 6, 7]	# string_elements = ["name", "type1", "type2"]
    in_file = open(file_name, 'r')
    pokemons_list = [] #Create empty list
    first_line = True
    for line in in_file:
        line = line.strip().lower().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            pokemon = {}
            for i in range(len(table_header)):
                if i not in string_elements:
                    pokemon[table_header[i]] = int(line[i])
                else:
                    pokemon[table_header[i]] = line[i]

            pokemons_list.append(pokemon) # Adds the dictionary to the end of the list
    in_file.close()
    return pokemons_list

def add_stat_total(pokemons : list[dict]) -> None:
    """ Adding the calculated pokemon power to each dictionary

    Preconditions: pokemons is a list of dictionaries containing Pokemon data with keys 'attack'
    'defense', 'speed', and 'hp'
    
    Examples:
    add_stat_total([{'Name': 'Bulbasaur', 'Type 1': 'grass', 'Type 2': 'poison',
                     'Generation': '1', 'Pokedex Number': 1, 'attack': 49,
                     'defense': 49, 'speed': 45, 'hp': 45}])

    >>>[{'Name': 'Bulbasaur', 'Type 1': 'grass', 'Type 2': 'poison', 
         'Generation': '1', 'Pokedex Number': 1, 'attack': 49,
         'defense': 49, 'speed': 45, 'hp': 45, 'stat_total': 188}]
    """
    for i in range(0, len(pokemons)):
        # Summing the pokemon stat
        stat_total = pokemons[i]['attack'] + pokemons[i]['defense'] + pokemons[i]['speed'] + pokemons[i]['hp']
        # Updating the pokemon dictionary
        pokemons[i].update({'stat_total': stat_total})

# Main script    
if __name__ == "__main__":
    file_name = 'pokemon.csv'
    # Load the values from the csv file
    pokemons = load_pokemon(file_name)
    print(pokemons)
    # print each dictionary in a new line
    for pokemon in pokemons:
        print(pokemon)
    # Add the stats column to each dictionary
    add_stat_total(pokemons)
    # print each dictionary in a new line
    for pokemon in pokemons:
        print(pokemon)

        
    
