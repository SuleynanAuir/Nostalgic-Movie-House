import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Cleaning_ import dataclean
import tkinter as tk
import time as t
import Data_Year_Count_
import Create_folders as cf
from Data_Processing import type_list, year_list, train_data

# Load the training data
train_path = cf.tpath
train_data = pd.read_csv(train_path, sep=':::', names=['Title', 'Type', 'Description'], engine='python')
train_data = pd.DataFrame(train_data , index=range(1,len(train_data)+1))
train_data.head()

name_year = train_data["Title"]
year_container = list()

# Run through the data and take its year out in the following rows 
for i in range(1,len(train_data["Title"])): # using reset index
    each = name_year[i].split()             # split title_year pair into sigle one
    year_container.append((each[-1])[1:5])

year_container.append(str(2006))
train_data["Year"] = year_container

change_container_type=[]
change_container_title=[]

for each_1 , each_2 in zip(train_data["Type"], train_data["Title"]):
        strip_each_type=each_1.strip() # change successfully
        strip_each_title=each_2.strip()
        strip_each_title=strip_each_title[0:len(strip_each_title)-1-6]
        
        change_container_type.append(strip_each_type)
        change_container_title.append(strip_each_title)


train_data["Type"]=change_container_type
train_data["Title"]=change_container_title


year_container.sort()

# using the self-defined function named"dataclean" to clean the data
year_container = dataclean(year_container)    # the whole data after Cleaning
year_set = set(year_container)                # Collection of all existing years 
# year_container.sort()


# Using to contain the element , prepare to make dict
year_list  = []    # dict_keys
count_list = []    # dict_values


# Fill dict_keys and dict_values list with the data one by one
for i1 in year_set:
    year_list.append(i1)                                # fill the dict_keys with the year
    count_list.append(year_container.count(int(i1)))    # count the number of occurrences of a year


# Making the dict corresponding to the year and count_times
year_num_count = ((dict(zip(year_list,count_list)))) 


# Assign values to the dictionary with year corresponding to the times it has occurred
dict_ = dict()
dict_["Year"]  = year_list  
dict_["count"] = count_list


# Changing the dictionary into pandas.DataFrame form
dict_DataFrame = pd.DataFrame(dict_)

plt.figure(figsize=(14,6))
sns.countplot(data=train_data, y='Type', order=train_data['Type'].value_counts().index) 


# Setting the value for the graph
plt.xlabel('Count', fontsize=12, fontweight=10)
plt.ylabel('Type', fontsize=12, fontweight=10)
plt.title("Distribution of Types(Transverse)" , fontsize=12 , fontweight=10)
plt.savefig('plot_1 (Distribution of Types(Transverse).png')


# Plot the distribution of genres using a bar plot
plt.figure(figsize=(14, 8))
counts = train_data['Type'].value_counts()
sns.barplot(x=counts.index, y=counts, palette='deep')
plt.xlabel('Genre', fontsize=12, fontweight=10)
plt.ylabel('Count', fontsize=12, fontweight=10)
plt.title('Distribution of Types(Vertical)', fontsize=12, fontweight=10)
plt.xticks(rotation=90, fontsize=14, fontweight=10)
plt.savefig('plot_2 (Distribution of Types(Vertical)).png')
plt.show()

# print(train_data['Year'].value_counts())
# print(set(dataclean(train_data["Year"])))