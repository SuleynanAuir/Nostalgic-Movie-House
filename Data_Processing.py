import pandas as pd
import Create_folders as cf
from Data_Cleaning_ import dataclean

train_path = cf.tpath
train_data = pd.read_csv(train_path, sep=':::', names=['Title', 'Type', 'Description'], engine='python')
train_data = pd.DataFrame(train_data , index=range(1,len(train_data)+1))

name_year = train_data["Title"]
year_container = list()

# Pick out Year and Creat new column for Year
for i in range(1,len(train_data["Title"])): 
    each = name_year[i].split()             
    # append signle year into container
    year_container.append((each[-1])[1:5])
    
year_container.append(str(2006))
# Build a new column for "Year"
train_data["Year"] = year_container 


year_container.sort()
year_container = dataclean(train_data["Year"])
year_set = set(year_container)                 
year_list = list(year_set)


# Change format for "Type" and "Title"
change_Container_type = []
change_Container_title = []

for each_1 , each_2 in zip(train_data["Type"], train_data["Title"]):
        strip_each_type = each_1.strip() 
        strip_each_title = each_2.strip()
        strip_each_title = strip_each_title[0:len(strip_each_title)-7]
        
        change_Container_type.append(strip_each_type)
        change_Container_title.append(strip_each_title)

# Reset Type and Title columns
train_data["Type"] = change_Container_type 
train_data["Title"] = change_Container_title 

# Creat list containing all types
type_list = []
for i in (train_data["Type"]):
    if (i not in type_list):
        type_list.append(i)
type_list.sort()
data_rows = len(train_data)

# view train_data
# print(train_data.info()) ;  print("")
# print(year_list)  ;  print("")
# print(type_list)  ;  print("")
