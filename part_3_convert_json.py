import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file
json_file_name = "tharkare_cc1.json"
with open(json_file_name, 'r') as reader:
    game_json_data = json.load(reader)

#Convert JSON data to CCLevelPack
new_level_pack = cc_classes.CCLevelPack()
new_level = cc_classes.CCLevel()
new_level_pack.add_level(new_level)
print(new_level_pack)

#Save converted data to DAT file