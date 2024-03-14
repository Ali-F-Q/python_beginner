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
- Create a function to write the list of dictionaries to a csv file
"""

def load_pokemon(file_name : str) -> list[dict]:
    """Return a list of dictionaries containing unique pokemon data read from file_name
    
    Preconditions: file_name has the following columns
                   ['name', 'attack', 'defense', 'hp', 'pokedex_number',
                    'speed', 'type1', 'type2', 'generation']
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
        # Alternative method:
        # pokemons[i]['stat_total'] = stat_total

def upload_pokemon(pokemons : list[dict], file_name : str) -> None:
    """Write Pokemon data into a text file with name file_name containing
    name, attack, defense, hp, speed, pokedex_number, type1, type2, generation and stat_total data
    in csv format
    
    Preconditions: pokemons is a list of dictionaries containing Pokemon data
    with keys: 'attack', 'defense', 'hp', 'Name', 'stat_total', 'Pokedex Number', 'speed', 'Type 1', 'Type 2', and 'Generation'
    
    Examples:
    upload_pokemon([{'Name': 'Bulbasaur', 'Type 1': 'grass', 'Type 2': 'poison',\
                     'Generation': '1', 'Pokedex Number': 1, 'attack': 49, \
                     'defense': 49, 'speed': 45, 'hp': 45, 'stat_total': 188}], 'pokemon_test.csv')
    >>>pokemon_test.txt file is created containing
    'attack,defense,hp,name,pokedex_number,speed,type1,type2,generation, stat_total
    49,49,45,Bulbasaur,1,45,grass,poison,1, 188
    '
    """
    # Open the file for writing
    in_file = open(file_name, 'w')
    
    # Retreive the headers of the table from the dictionary's keys
    table_header = list(pokemons[0].keys())

    # Create the table heads in the resulting csv file
    i = 0
    for head in table_header:
        # Check if this is the last head and add new line
        # Otherwise, add a comma
        if i == len(table_header) - 2:
            in_file.write(head+"\n")
        else:
            in_file.write(head+",")
        i += 1

    # Iterate over every dictionary in the list of pokemons
    for pokemon in pokemons:
        i = 0
        # Iterate over every item in the dictionary
        for i in range(len(pokemon)):
            if i < len(pokemon) - 1:
                # write the value to the file then add a comma at the end.
                in_file.write("{0},".format(pokemon[table_header[i]]))
            else:
                # if this is the last item in the dictionary, add a new line instead of a comma
                in_file.write("{0}\n".format(pokemon[table_header[i]]))
    in_file.close()

# Main script    
if __name__ == "__main__":
    file_name = 'pokemon.csv'
    
    # Load the values from the csv file
    pokemons = load_pokemon(file_name)

    # print each dictionary in a new line
    for pokemon in pokemons:
        print(pokemon)

    # Add the stats column to each dictionary
    add_stat_total(pokemons)
    
    # print each dictionary in a new line
    for pokemon in pokemons:
        print(pokemon)
    
    # Write the list of dictionaries to a file
    upload_pokemon(pokemons, 'pokemon_test.csv')