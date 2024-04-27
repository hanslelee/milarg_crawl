import random 
 
# Open the file in read mode and read all the lines into a list 
with open('mil_data_combined_duplicates_removed_shuf.tsv', 'r') as f: 
    lines = f.readlines() 
 
# Shuffle the list of lines randomly 
random.shuffle(lines) 
 
# Open the same file in write mode and write the shuffled lines back to the file 
with open('mil_data_combined_duplicates_removed_shuffled.tsv', 'w') as f: 
    f.writelines(lines) 