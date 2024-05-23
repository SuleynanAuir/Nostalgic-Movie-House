import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Cleaning_ import dataclean
import Create_folders as cf

# Load Dataset
train_data = cf.tpath
train_data = pd.read_csv(train_data, sep=':::', names=['Title', 'Type', 'Description'],engine='python')
train_data = pd.DataFrame(train_data , index=range(1,len(train_data)+1))

name_year = train_data["Title"]
year_container = list()

for i in range(1,len(train_data["Title"])):
    each = name_year[i].split()
    year_container.append((each[-1])[1:5])

year_container.sort()

year_container.sort()

year_container = dataclean(year_container)    
year_set = set(year_container) # every_single_list

year_list = []
count_list = []

for i1 in year_set:
    year_list.append(i1)
    count_list.append(year_container.count(int(i1)))


# Creat year-counttime Pair to make a dictionary
year_num_count = (dict(zip(year_list,count_list))) 

dict_ = dict()
dict_["Year"] = year_list
dict_["count"]=count_list

dict_DataFrame=pd.DataFrame(dict_)

dict_DataFrame.to_csv('Year_Count.csv', index=False)

sns.lineplot(x='Year', data=dict_DataFrame , y='count')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Yearly Count')
# plt.show()
plt.savefig('plot_3 (Distribution of Films_number in years).png')
# plt.show()

