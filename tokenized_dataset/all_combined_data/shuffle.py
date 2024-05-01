import random 
 
# Open the file in read mode and read all the lines into a list 
with open('all_combined_tokenized_240430.txt', 'r') as f: 
    lines = f.readlines() 
 
# Shuffle the list of lines randomly 
random.shuffle(lines) 
 
# Open the same file in write mode and write the shuffled lines back to the file 
with open('all_combined_tokenized_shuffled_240430', 'w') as f: 
    f.writelines(lines) 