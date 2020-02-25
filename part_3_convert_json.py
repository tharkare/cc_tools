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
new_level_26 = cc_classes.CCLevel()

new_level_26.level_number = game_json_data[0]["level_number"]
new_level_26.time = game_json_data[0]["time"]
new_level_26.num_chips = game_json_data[0]["num_chips"]
new_level_26.upper_layer = game_json_data[0]["upper_layer"]

for json_field in game_json_data[0]["optional_fields"]:
    field_type = json_field["field_type"]
    print(field_type)
    if field_type == "hint":
        new_hint_field = cc_classes.CCMapHintField(json_field["hint"])
        new_level_26.add_field(new_hint_field)
    elif field_type == "password":
        new_password_field = cc_classes.CCEncodedPasswordField(json_field["password"])
        new_level_26.add_field(new_password_field)
    elif field_type == "title":
        new_title_field = cc_classes.CCMapTitleField(json_field["title"])
        new_level_26.add_field(new_title_field)
    elif field_type == "monsters":
        monsters = []
        for json_monster in json_field["monsters"]:
            x = json_monster["x"]
            y = json_monster["y"]
            new_monster_coord = cc_classes.CCCoordinate(x, y)
            monsters.append(new_monster_coord)
        new_monster_field = cc_classes.CCMonsterMovementField(monsters)
        new_level_26.add_field(new_monster_field)

new_level_pack.add_level(new_level_26)
print(new_level_26)

#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(new_level_pack, "data/tharkare_cc1.dat")
test_dat = cc_dat_utils.make_cc_level_pack_from_dat("data/tharkare_cc1.dat")
print(test_dat)