import os

from read_data import read_data

reviews_list = read_data()

print('len(reviews_list): ', len(reviews_list))

for r in reviews_list:
    print(r)
    print('.......................')