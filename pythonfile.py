#!/usr/bin.env python

#1. load a dataset from a file
#2. "organize" that file, so we can access colums *or* rows of it easily
#3. compute some "summary statistics" about the dataset
#4. print those sumary statistics


#1. load a dataset
#1a. accept arbitrary filename as argument
#1b. load the file

from argparse import ArgumentParser
 
parser = ArgumentParser(description='A CSV reader + stats maker')
parser.add_argument ('csvfile', help='Path to the input csvfile')

parsed_args = parser.parse_args()
print(parsed_args)
print(parsed_args.csvfile)


my_csv_file = parsed_args.csvfile

import os

#if os.path.isfile(my_csv_file):
#  print ("yay, it's real!!!!")
#else:
# print ('oops, plz give real file')


#assert os.path.isfile(my_csv_file), "pls give a real file"

#if not os.path.isfile(my_csv_file):
#   raise ValueError("not a valid file")

assert os.path.isfile(my_csv_file), "please give us a real file, k thx"
#print('hello')

#1b. load the file

import pandas as pd

data = pd.read_csv(my_csv_file, sep='\s+|,', header=None)
print(data.head())

#for item in idr(data):
#   print(item)

print(data.shape)

# 2. "organize" that file, so we can access columns *or* rows of it easily
# 2a. access any row "pandas access data by column"
print(data.iloc[3:5,:])
# 2b. access any column "pandas access data by row"

print(data.iloc[:3, -2:])
#print(data.iloc[::-1:4])
# 2c. access any value "pandas access specific data by location"
print(data.iloc [3,4])
#3. compute some "summary statistic" about the dataset

import numpy as np

print(np.mean(data))
print(np.std(data))


