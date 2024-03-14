from load_pokemon import *
from pokemon_game import *
import check

print("****** Pokemon Game unit testing code ******")

test_file =  "pokemon_test.csv"

print("1- Check if the returned type is a list")
check.equal(isinstance(load_pokemon(test_file), list), True)
check.equal(isinstance(load_pokemon(test_file), dict), False)
check.summary()

print("2- Check if the number of elements in the returned list is of the correct length")
check.equal(len(load_pokemon(test_file)), 7)
check.summary()

print("3- Check if the correct values are stored in the returned list")
pokemons_details = load_pokemon(test_file)
check.equal(pokemons_details[0], {'name': 'abomasnow', 'attack': 132, 'defense': 105,
                                  'hp': 90, 'pokedex_number': 460, 'speed': 30, 'type1': 'grass',
                                  'type2': 'ice', 'generation': 4})
check.summary()
print("4- Check if the Health value is added and calculated correctly in the resulting list from add_stat_total")
# print(load_pokemon(test_file))
pokemons_details_with_stats = load_pokemon(test_file)
add_stat_total(pokemons_details_with_stats)
check.equal(pokemons_details_with_stats[0].get("Health"), 357)
check.equal(pokemons_details_with_stats[0].get("stat_total"), 357)
check.summary()

