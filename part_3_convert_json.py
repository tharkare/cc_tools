import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file
json_file_name = "tharkare_cc1.json"
with open(json_file_name, 'r') as reader:
    game_json_data = json.load(reader)

#Convert JSON data to CCLevelPack
level_number_26 = game_json_data[0]["level_number"]
time_26 = game_json_data[0]["time"]
num_chips_26 = game_json_data[0]["num_chips"]
upper_layer_26 = game_json_data[0]["upper_layer"]
lower_layer_26 = game_json_data[0]["lower_layer"]
optional_fields_26 = game_json_data[0]["optional_fields"]

new_level_pack = cc_classes.CCLevelPack()
new_level_26 = cc_classes.CCLevel()
new_clone_26 = cc_classes.CCCloningMachineControl(5, 5, 15, 15)

new_level_26.level_number = level_number_26
new_level_26.time = time_26
new_level_26.num_chips = num_chips_26
new_level_26.upper_layer = upper_layer_26
#new_level_26.optional_fields = optional_fields_26

new_level_pack.add_level(new_level_26)

#Save converted data to DAT file
file_writer = open("data/final_level.dat", "wb")
final_level = cc_dat_utils.write_level_to_dat(new_level_26, file_writer)