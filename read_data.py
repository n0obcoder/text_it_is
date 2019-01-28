'''
DATE 28th JAN 2019
THIS CODE READS THE CSV AND CREATES THE reviews_list WHICH CONTAINS ALL THE REVIEWS. THESE REVIEWS HAVE TO BE PREPROCESSED BEFORE THEY CAN BE USED FOR MAKING WORD EMBEDDINGS.
'''

import pandas as pd
import numpy as np
import os, pdb
from tqdm import tqdm

###pandas hacks
#print(data.head())
#print(data.columns.values) 
#print(data[0:2].['review'])
################

data_dir = 'data'
'''
for f in os.listdir(data_dir):
    print(f)
'''
imdb_reviews_path = 'data/imdb_master.csv'

from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv(imdb_reviews_path, index_col = 0)
data = data[:100][:]

def read_data():
    
    display_label_categories = False
    
    reviews_list = []
    for idx, row in tqdm(data.iterrows()):
        #print(row['review'], row['label'])
        #exit()
        #print(idx)
        reviews_list.append(row['review'])
    
    print('the column names are:')
    for col_names in data:
        print(col_names)
        
    #pdb.set_trace()

    train_data = data[data.type == 'train']
    test_data = data[data.type == 'test']

    #print(train_data.shape)
    #print(test_data.shape)
    #exit()
    X_train = train_data[['review']] #pd dataframe
    y_train = train_data['label'] #pd series


    X_test = test_data[['review']] #pd dataframe
    y_test = test_data['label'] #pd series

    #print(y_train.unique())
    
    if display_label_categories == True:
        y_train.value_counts().plot(kind="bar", rot=0, figsize=(13, 8))
        plt.ylabel("count", fontsize=13)
        plt.xlabel("label", fontsize=13)
        plt.show()
    
    return reviews_list






