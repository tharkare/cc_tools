import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    game_library = test_data.GameLibrary()     # Initialize a new GameLibrary

json_file_name = "test_data.json"

with open(json_file_name, 'r') as reader:
    game_json_data = json.load(reader)

print(game_json_data)
count = 0
    ### Begin Add Code Here ###
    #Loop through the json_data
    #use for loop, not while loop
     #Create a new Game object from the json_data by reading
     #  title
     #  year
     #  platform (which requires reading name and launch_year)
    #create game object
    #Add that Game object to the game_library
    ### End Add Code Here ###

    ###return game_library

#Part 2
input_json_file = "test_data.json"
with open(input_json_file, 'r') as reader:
    game_load = json.load(reader)
print(game_load)
### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
