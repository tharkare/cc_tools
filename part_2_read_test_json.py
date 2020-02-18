import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    game_library = test_data.GameLibrary()     # Initialize a new GameLibrary
    json_file_name = "test_data.json"
    with open(json_file_name, 'r') as reader:
        game_json_data = json.load(reader)
        ### Begin Add Code Here ###
        #Loop through the json_data
        #use for loop, not while loop
         #Create a new Game object from the json_data by reading
         #  title
         #  year
         #  platform
    for x in range(0, 3):
        game_title = game_json_data["title"][x]
        game_year = game_json_data["year"][x]
        game_plat_year = game_json_data["platform"][x]["launch_year"]
        game_plat_name = game_json_data["platform"][x]["name"]
        game_platform = test_data.Platform(game_plat_name, game_plat_year)
        new_game = test_data.Game(game_title, game_platform, game_year)
        game_library.add_game(new_game)
    #create game object
    #Add that Game object to the game_library
    ### End Add Code Here ###
    return game_library

#Part 2
### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
input_json_file = "data/test_data.json"
my_game_library = make_game_library_from_json(input_json_file)
print(my_game_library)
### End Add Code Here ###