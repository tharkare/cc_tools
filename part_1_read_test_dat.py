from cc_dat_utils import make_cc_level_pack_from_dat

#Part 1
input_dat_file = "data/pfgd_test.dat"

#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
#print the resulting data

pfgd_test = make_cc_level_pack_from_dat(input_dat_file)
print(pfgd_test)
newfile = open('data/pfgd_test.txt', 'w') #created a new blank file
newfile.write(str(pfgd_test)) #placed data into the file
newfile.close() #closed the file