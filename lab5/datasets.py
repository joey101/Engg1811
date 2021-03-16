#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811, Lab 05, Part B, Template 

"""
import math as m
# %% Experimental data
datasets = []
datasets.append([14.2, 32.5, 42.1, 74.5, 43.5])
datasets.append([25.7, 34.1, 48.7, 50.3])
datasets.append([11.2, 26.9, 95.1, 52.1, 23.5, 5.6, 45.7, 37.8])
datasets.append([54.7, 25.3])
# datasets.append([-24.7, -57.3, -145.5])
# datasets.append([-12.5, 14.5, -452, -734.4])

# The variable datasets contain 4 sets of experimental data
# E.g. The data set datasets[0] has 5 data points
# E.g. The data set datasets[1] has 4 data points

# %% 
# Your task is to create a list called summary_list with as many
# entries as the number of lists in the variable datasets
# 
# summary_list[0] = 
# minimum entry in datasets[0] / number of entries in datasets[0]
#
# This is then repeated for the other entries
#
# For checking, the expected answers are:
# [2.84, 6.425, 0.7, 12.65]
#-------------------------------------------------------------------------

# Finds the smallest number in a data set
def lowest(data_list):
    smallest = data_list[0]
    for num in data_list:
        if num < smallest:
            smallest = num
    return smallest
# Find the length of each array
def length(data_list):
    size = len(data_list)
    return size
#------------------------------------------------------------------------- 
summary_list = [] # Initiating empty list 
length_list = [] # initiating list length
ultimate_list = [] # combination of both lists
for num in datasets:
    summary_list.append(lowest(num))
for x in datasets:
    length_list.append(length(x))


print(summary_list)
print(length_list)