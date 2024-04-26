import json
import pandas as pd

json_fn = './ynat-v1.1_dev.json'
result_tsv_fn = 'dev.tsv'

with open(json_fn, mode='rt', encoding='utf-8-sig') as f:
    train_dataset = json.load(f)


train_dataset_list = [{'label':data['label'], 'text':data['title']} for data in train_dataset]
train_df = pd.DataFrame(train_dataset_list)
train_df.head()

train_df.to_csv(result_tsv_fn, sep="\t", index=False)