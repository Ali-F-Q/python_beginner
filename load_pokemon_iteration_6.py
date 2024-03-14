"""
ECOR 1042
Case study: iterative, incremental development of a pokemon game
that uses Python's str, list, set and dict types.

Last edited: May12, 2023

Copy right: Dr. Rami Sabouni

Iteration 5:
- Demonstrate that we can read a line from a text file and split 
  the line into a list of words.
- The first line read from the csv file will be the table header and
  every line after is data from the table.
- The values in each line is stored into a dictionary.
- Fix the value type for each item
- Add the dictionary to our final list
- This is repeated until every line has been read and processed.
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
    
    pokemons_list = [] #Create empty list

    first_line = True
    count = 0
    for line in in_file:
        count += 1

        # For each line, first remove any leading or trailing punctuation,
        # then convert it word to lower case.
        #
        # Examples:
        #  'Hello,'.strip(string.punctuation) returns 'Hello'
        #  'World\n'.strip() returns 'World'
        #  'Hello'.lower() returns 'hello'
        line = line.strip()
        line = line.lower()
        
        # Split each line into a list of words.
        # By default, the split method removes all whitespace; e.g.,
        # '  Hello,    world   '.split() returns this list:
        #
        #    ['Hello,', 'world']
        #
        # and not:
        #
        #    ['  Hello,', '    world   ']
        #
        # Notice that the punctuation marks have not been removed.
        line = line.split(',') 

        # All three statements can be combined into one:
            # line = line.strip().lower().split(',')
        
        if first_line:
            # print(line) #to show columns
            first_line = False
            table_header = line
        else:
            pokemon = {}    
            pokemon[table_header[0]] = line[0]
            pokemon[table_header[1]] = int(line[1])
            pokemon[table_header[2]] = int(line[2])
            pokemon[table_header[3]] = int(line[3])
            pokemon[table_header[4]] = int(line[4])
            pokemon[table_header[5]] = int(line[5])
            pokemon[table_header[6]] = line[6]
            pokemon[table_header[7]] = line[7]
            pokemon[table_header[8]] = int(line[8])

            # pokemons_list.append(pokemon) # Adds the dictionary to the end of the list
            pokemons_list += [pokemon] # Adds the dictionary to the end of the list

    in_file.close()
    return pokemons_list

# Main script    
if __name__ == "__main__":
    file_name = 'pokemon_test.csv'
    
    # Load the values from the csv file
    pokemons = load_pokemon(file_name)
    print(pokemons)
