'''
DATE 28th JAN 2019
THIS CODE GETS THE reviews_list WHICH CONTAINS ALL THE REVIEWS FROM read_data.py. THESE REVIEWS HAVE TO BE PREPROCESSED BEFORE THEY CAN BE USED FOR MAKING WORD EMBEDDINGS.
'''

import os
from read_data import read_data

reviews_list = read_data()

print('len(reviews_list): ', len(reviews_list))

for r in reviews_list:
    print(r)
    print('.......................')
