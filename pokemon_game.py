"""
ECOR 1042
Case study: iterative, incremental development of a pokemon game
that uses Python's str, list and dict types.

Last edited: May16, 2023

Copy right: Dr. Rami Sabouni

Game engin and starting point of the interactive user interface
"""
# # Option 1
# import load_pokemon
# file_name = 'pokemon_test.csv'
# pokemons = load_pokemon.load_pokemon(file_name)
# load_pokemon.add_stat_total(pokemons)

# Option 2
from load_pokemon import load_pokemon, add_stat_total
# file_name = 'pokemon_test.csv'
# pokemons = load_pokemon(file_name)
# add_stat_total(pokemons)

# # Option 3
# from load_pokemon import *
# pokemons = load_pokemon(file_name)
# add_stat_total(pokemons)

allowed_instructions = ['L', 'D', 'A', 'Q']
def start_menu() -> None:
    """
    Prints the start menu containing possible inputs for the user
    """
    print("\nWelcome to Pokemon Game!")
    print("(L)oad Pokemons")
    print("(D)isplay Pokemons")
    print("(A)dd Pokemon's stats")    
    print("(Q)uit")

if __name__ == '__main__':
    quit = False
    pokemons = []
    file_loaded = False
    start_menu()
    choice = input("\nChoice: ")
    while not quit:
        if choice.upper() in allowed_instructions:
            if choice.upper() == 'L':  #Load pokemon choice
                file_name = input("What is the file name?: ")
                pokemons = load_pokemon(file_name)
                print("{0} loaded!\n".format(file_name))
                file_loaded = True
            elif choice.upper() == 'Q':    #Quiting the program
                    quit = True
            else:
                if file_loaded:
                    if choice.upper() == 'D':    #Display pokemons choice
                        print("Displaying Pokemons...")
                        for pokemon in pokemons:
                            print(pokemon)
                    elif choice.upper() == 'A':    #Add pokemon's stats
                        add_stat_total(pokemons)                
                        print("Pokemon stats were added to dictionaries.")
                else:
                    print("\nFile must be loaded first!!!\n")
                
            if not quit:
                start_menu()
                choice = input("\nChoice: ")
        else:
            choice = input("Invalid Input!!\nEntere a valid choice: ")

    print("Exiting program...")
            





