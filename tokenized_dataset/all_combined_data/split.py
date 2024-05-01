import random

# 데이터 파일 경로
file_path = './all_combined_tokenized_shuffled_240430.txt'

# 각 데이터 파일로 분할할 비율
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# 데이터를 읽어들임
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 데이터를 무작위로 섞음
random.shuffle(lines)

# 분할 지점 계산
num_lines = len(lines)
train_split = int(train_ratio * num_lines)
val_split = train_split + int(val_ratio * num_lines)

# 분할
train_data = lines[:train_split]
val_data = lines[train_split:val_split]
test_data = lines[val_split:]

# 파일로 쓰기
def write_data(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(data)

write_data('./240501/train.txt', train_data)
write_data('./240501/val.txt', val_data)
write_data('./240501/test.txt', test_data)
