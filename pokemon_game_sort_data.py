#Project idea 2: Pokemon
#Iteration 2: sort_data
#SaPP

def sort_pokemon_bubble(pokemons : list, column : str) -> None:
    """Sort the list pokemons by column attribute in ASCENDING order using bubble sort
    
    Preconditions:
        -pokemons is a list of dictionaries containing Pokemon data with keys 'attack'
        'defense', 'speed', and 'hp'
        - column corresponds to one of the keys in the dictionaries
    """
    num_pokemon = len(pokemons)
    
    for i in range(num_pokemon - 1):
        swapped = False
        
        for j in range(num_pokemon - i - 1):
            if pokemons[j][column] > pokemons[j + 1][column]:
                swapped = True
                pokemons[j], pokemons[j + 1] = pokemons[j + 1], pokemons[j]  
        
        if not swapped:
            return

def sort_pokemon_selection(pokemons : list, column : str) -> list:
    """Sort the list pokemons by column attribute in ASCENDING order using selection sort
    
    Preconditions:
        -pokemons is a list of dictionaries containing Pokemon data with keys 'attack'
        'defense', 'speed', and 'hp'
        - column corresponds to one of the keys in the dictionaries
    """  
    num_pokemon = len(pokemons)
    
    for i in range(num_pokemon):
        min_index = i
        
        for j in range(i + 1, num_pokemon):
            
            if pokemons[j][column] < pokemons[min_index][column]:
                min_index = j
        
        pokemons[i], pokemons[min_index] = pokemons[min_index], pokemons[i]
        
if __name__ == '__main__':
    #Test code
    from load_pokemon import load_pokemon
    
    file_name = 'pokemon.csv'
    pokemons = load_pokemon(file_name)
    
    column = input("Which column would you like to sort by using selection sort?: ")
    sorted_pokemons = sort_pokemon_selection(pokemons, column)
    for pokemon in sorted_pokemons:
        print(pokemon)
    
    column = input("Which column would you like to sort by using bubble sort?: ")
    sorted_pokemons = sort_pokemon_bubble(pokemons, column)
    for pokemon in sorted_pokemons:
        print(pokemon)
    