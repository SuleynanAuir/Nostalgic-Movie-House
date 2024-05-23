# Python Project ——Group 5

 **Shell Frame**
 1. BackGround
	###### 1.1 Injection
	###### 1.2 Purpose

 2. **Coding Part**
	### 2.1 *Package*
	### 2.2 *Input Dataset*
	### 2.3 *Data Preview*
	### 2.4 *Data Processing*
	###### -- DataCleaning
	###### -- Visualization
	###### -- CheckingPart
	###### -- SearchingPart
	###### -- Recommendation

  3. **User Interface**
	###### -- Preliminary Processing by GUI
	###### -- Advanced Processing by Pywebio
 
  4. **Distribution**

---
##  1. Part One : BackGround
### 1.1 Genre Classification Dataset
   ##### 1.11> Injection:  **IMBD** is  an online database of information related to films containing cast, production crew and personal biographies, plot summaries, trivia, ratings, and fan and critical reviews. 

 ##### 1.12> Purpose: Built up **Searching** System to screen out the Target Movie for specific **Type**,  **Year**,  **KeyWords**, also having function to **Recommendation_Rank**

## 2. Part Two : CodePart

### 2.1 Package
```python
# This Python 3.11 environment 
# Defined by https://www.kaggle.com/datasets/hijest/genre-classification-dataset-imdb
import numpy as pd
import pandas as pd
import os
import Create_folders as cf
import sys
import random as r
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
import Data_Year_Count_
import Data_Processing
from tkinter import ttk
from tkinter import font as tkfont
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkinter import font as tkfont
from PIL import Image, ImageTk
```
### 2.2 Input Dataset
```python
# Creat Folder
folders1 = "train path"
folders2 = "image path"
os.makedirs(folders1,exist_ok=True)
os.makedirs(folders2,exist_ok=True)

#Get Path
def getpath(folderpath):
	file_paths=[]
	for root, dirs, files in os.walk(folderpath):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths
```
```python
trainpath = getpath(folders1)
imagepath = getpath(folders2)
tpath = trainpath[0]
ipath = imagepath[0]
```
```python
train_path = cf.tpath
# Seprate data by Specific symbols
# Reset Index, Rename Columns
train_data = pd.read_csv(train_path, sep=':::', names=['Title', 'Type', 'Description'], engine='python')
train_data = pd.DataFrame(train_data , index=range(1,len(train_data)+1))
```
### 2.3 Data Preview
```python
# train_data
print(train_data.head())
```
|Index|Title|Type|Description|
|--|--|--|--|
|1|  Oscar et la dame rose (2009)|drama|Listening in to a conversation between his do..|
|2  | Cupid (1997) |thriller | A brother and sister with a past incestuous ...
|3|Young, Wild and Wonderful (1980)|adult|As the bus empties the students for their...
| 4 | The Secret Sin (1915) |drama|To help their unemployed father make ends...
|  5| The Unrecovered (2007) |drama|The film's title refers not only to...

[54214 rows , 3 columns ]
```python.3.11
train_data.info()
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 54214 entries, 1 to 54214
Data columns (total 3 columns):
 #####   Column       Non-Null Count  Dtype 
 0   Title        54214 non-null  object
 1   Type         54214 non-null  object
 2   Description  54214 non-null  object
dtypes: object(3)
memory usage: 1.2+ MB

----
```python
train_data.shape 
```
(54214, 4)

----
```python
train_data.columns
```
Index(['Title', 'Type', 'Description'], dtype='object')

---

```python
train_data.isnull().sum()
```
Title          0
Type           0
Description    0
Year           0
dtype: int64

---
### 2.4 Data Processing
#### 2.41 *DataCleaning*
```python
# DataClening for Visualization
# filte out error value
def dataclean(input_list):
	clean_data = []
	for i in input_list:
		try:
			m = int(i)
		except ValueError:											   										
			continue
		clean_data.append(m)
	clean_data.sort()
	
	return clean_data
```
```python
# Using dataclean to Filter Wrong Values
set(dataclean(train_data["Year"]))
```
{1890, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022}

---
#### 2.42 *DataProcessing*
```python
# Separate Title, Year
name_year = train_data["Title"]
year_container = list()

for i in range(1,len(train_data["Title"])):
	each = name_year[i].split()
	year_container.append((each[-1])[1:5])

# Build a new column for "Year"
year_container.append(str(2006))
year_container.sort()

train_data["Year"] = year_container
year_container = dataclean(train_data["Year"])
year_set = set(year_container)
year_list = list(year_set)

change_Container_type = []

change_Container_title = []

# Reset format for Type, Title
for each_1 , each_2 in zip(train_data["Type"], train_data["Title"]):

	strip_each_type = each_1.strip()
	strip_each_title = each_2.strip()
	strip_each_title = strip_each_title[0:len(strip_each_title)-7]

	change_Container_type.append(strip_each_type)
	change_Container_title.append(strip_each_title)


# Reset Type and Title columns
train_data["Type"] = change_Container_type
train_data["Title"] = change_Container_title

type_list = []
for i in (train_data["Type"]):
	if (i not in type_list):
		type_list.append(i)

type_list.sort()

year_container = dataclean(year_container)
year_set = set(year_container) # every_single_list

year_list = []
count_list = []

for i1 in year_set:
	year_list.append(i1)
	count_list.append(year_container.count( int(i1) )
year_num_count = (dict(zip(year_list,count_list)))

dict_ = dict()
dict_["Year"] = year_list
dict_["count"]=count_list
dict_DataFrame=pd.DataFrame(dict_)
```
```python
# Check Year list and Type list
print(year_list) # Every Single Year
print(type_list) # Every Single Type
# year_list=[1890, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
# type_list=['action', 'adult', 'adventure', 'animation', 'biography', 'comedy', 'crime', 'documentary', 'drama', 'family', 'fantasy', 'game-show', 'history', 'horror', 'music', 'musical', 'mystery', 'news', 'reality-tv', 'romance', 'sci-fi', 'short', 'sport', 'talk-show', 'thriller', 'war', 'western']
```
#### 2.43 Visualization
##### a> Distribution of Types
```python
plt.figure(figsize=(14,6))
sns.countplot(data=train_data, y='Type', order=train_data['Type'].value_counts().index)

# Setting the value for the graph

plt.xlabel('Count', fontsize=12, fontweight=10)
plt.ylabel('Type', fontsize=12, fontweight=10)
plt.title("Distribution of Types(Transverse)" , fontsize=12 , fontweight=10)
plt.savefig('plot_1 (Distribution of Types(Transverse).png')
```
![Plot_1: Distribution of Types](/imgs/2023-12-20/VEkI2xdDWknfXETd.png)

```python
# Plot distribution of genres using bar plot
plt.figure(figsize=(14, 8))
counts = train_data['Type'].value_counts()
sns.barplot(x=counts.index, y=counts, palette='deep')
plt.xlabel('Genre', fontsize=12, fontweight=10)
plt.ylabel('Count', fontsize=12, fontweight=10)
plt.title('Distribution of Types(Vertical)', fontsize=12, fontweight=10)
plt.xticks(rotation=90, fontsize=14, fontweight=10)
plt.savefig('plot_2 (Distribution of Types(Vertical)).png')
```
![Plot_2: Distribution of Types](/imgs/2023-12-20/CtFW1m6TpC3d4Z52.png)

##### b> Distribution of Films_number in Years
```python
# Plot Distribution of Films_number in years
sns.lineplot(x='Year', data=dict_DataFrame , y='count')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Yearly Count')
plt.savefig('plot_3 (Distribution of Films_number in years).png')
plt.show()
```
![Distribution of Films_number in years](/imgs/2023-12-20/QGnwBiHFbKBTv01r.png)
#### 2.44 Checking
```python
print(train_data.head()) # Check the processed Data
print(train_data.info)
print(train_data.columns)
```
######    Check The Processed Data:
|Index|Title|Type|Description|Year|
|--|--|--|--|--|
|1|Oscar et la dame rose|drama|Listening in to a conversation between his do..|2009|
|2|Cupid|thriller|A brother and sister with a past incestuous ...|1997|
|3|Young, Wild and Wonderful|adult|As the bus empties the students for their...|1980|
|4|The Secret Sin|drama|To help their unemployed father make ends...|1915|
|5|The Unrecovered|drama|The film's title refers not only to...|2007|
[ 54214 rows, 4 columns ]

```python
train_data.info()
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 54214 entries, 1 to 54214
Data columns (total 4 columns):
 ######   Column       Non-Null Count  Dtype 

 0   Title        54214 non-null  object
 1   Type         54214 non-null  object
 2   Description  54214 non-null  object
 3   Year         54214 non-null  object
dtypes: object(4)
memory usage: 1.7+ MB
None

---
```python
train_data['Year'].value_counts() # Number of occurrences corresponding year
```
Year
2016    3275
2017    3223
2015    2910
2014    2450
        ... 
Girl       1
Powe       1
Rome       1
SRI)       1
Atro       1
Name: count, Length: 158, dtype: int64

```python
train_data['Type'].value_counts() # Number of occurrences corresponding type
```
Type
drama          13613
documentary    13096
comedy          7447
short           5073
horror          2204
thriller        1591
action          1315
western         1032
reality-tv       884
family           784
adventure        775
music            731
romance          672
sci-fi           647
adult            590
crime            505
animation        498
sport            432
talk-show        391
fantasy          323
mystery          319
musical          277
biography        265
history          243
game-show        194
news             181
war              132

---
#### 2.45 SearchingPart
**This Part Showing in Terminal !!!**
```python
import pandas as pd
import time
import Create_folders as cf
from Data_Processing import type_list, year_list, train_data, data_rows
```
```python
def Seach():
	Name_Search() 		# Input FilmNames to Check
	Type_Search() 		# Input FilmTypes to Check
	KeyWords_Search()	# Input FilmWords to Check
	Year_Search()		# Input FilmYears to Check
```
```python
Search()
```
```python
# "TypeSearch"
# Choose the type you want: 
# >>> war
# Output would like be:
# <<<
'''
No.37638
Title:Hong se niang zi jun
Type:war
Description:
---> In 1930s, Wu Qionghua was a housemaid of Nan-ba-tian, a cruel warlord of a village in Hainan Island, China...

No.38113
Title:Dvazhdy rozhdyonnyy
Type:war
Description:
---> World War 2, White Sea. A Soviet transport ship carrying wounded from the front line is sunk by German planes...

............ More can be shown
'''
```
```python
# "KeyWords"
# Input any KeyWords (Input 0 TO SHUT DOWN):
# >>> love
# Output would like be:
# <<<   
'''
Title:Even Just 
Year:2019 
Description: Jerry J. Garanyan, an ambulance-chasing lawyer ...

Title:Bypass 
Year:2019 
Description: An American adventure seen through the eyes of a …

Title:Duped: The Jezebel Experience 
Year:2019 
Description: A successful man meets an attractive woman that b...

Title:Concrete Girl 
Year:2019 
Description: An amateur female fighter works multiple jobs to ….

Title:Before I lay me down to Sleep 
Year:2019 
Description: If you were given only six months to a year to'''
```
```python
# "YearSearch"
# Input Year Single Choice(1) / Year Range(num!=1)
# >>> 0
# Input the Beginning_Time:
# >>> 2017
# Input the End_Time:
# <<< 2019
"""
No.31
Title:<Love Bites>
Type: <horror>
Introduce:  Hollywood has long since been a haven for vampires and other underworld creatur......Wanting U Explore

No.43
Title:<Brad Cuts Loose>
Type: <short>
Introduce:  Brad, an uptight office drone, seemingly discovers the perfect vehicle for lett......Wanting U Explore

No.57
Title:<Race Across America: Push Beyond>
Type: <documentary>
Introduce:  Marshall Nord is a 49-year-old executive, Father, husband and amateur endurance......Wanting U Explore

More will be shown.......
"""
```
## 3. Part Three : User Interface

 - 3.0 **Frame**
```python
class Application(tk.Frame):
	def __init__(self, root):
		super().__init__(root)
		self.master = root
		self.pack()
		root.minsize(800, 500) # size
		root.title('HomePage') # name
		self.HomePage()
		self.search_var = tk.StringVar()
		image_path =cf.ipath # Replace with your image path
		original_image = Image.open(image_path)
		resized_image = original_image.resize((500, 300))
		self.bg_image = ImageTk.PhotoImage(resized_image)
		self.bg_label = tk.Label(root, image=self.bg_image)
		# Adjust the label to fill the available space
		self.bg_label.pack(fill="both", expand=False)
```

 - 3.1 **Login Interface**
```python
# The login interface Code
```

 - 3.2 **HomePage**
```python
def HomePage(self):
	title_font = tkfont.Font(family='Helvetica', size=24, weight='bold')
	 # Title 
	tk.Label(self, text="Nostalgic Movies House", fg='#556B2F', font=title_font).grid(row=0, column=0) # title  
	subtitle_font = tkfont.Font(family='Helvetica', size=18, weight='bold')
	# Sub-Title
	tk.Label(self, text="Searching the movies you want", fg='#966F33', font=subtitle_font).grid(row=1, column=0) 
	frame = tk.Frame(self)
	frame.grid(row=3, column=0, columnspan=2, pady=0.2)
	
	# Random recommendation
	random_list = set()
	for i in range(5):
		random_num = r.randint(1, 54215)
		if random_num not in random_list:
			random_list.add(random_num)
			ran = [train_data["Title"].loc[i] for i in random_list]
	button = tk.Button(frame, text='Q',command=self.buttonActive)
	button.grid(row=1, column=0, columnspan=2)

	frame1 = tk.Frame(self)
	frame1.grid(pady=10)
	frame1.configure(height=500, width=200)
	tk.Label(frame1, text="Top Five Recommendation: "+''.join(ran)).grid(row=0, column=0)


def buttonActive(self): # button
	if not hasattr(self, "search_window"): # Check if the Searching window has been created already
		self.search_window = Searching()
		self.search_window.mainloop()
	else:
		self.search_window.destroy() # If the window is already created, close it before creating a new one
		self.search_window = Searching()
		self.search_window.mainloop()
```

**HomePage Show as fellow :** 
![HomePage](/imgs/2023-12-21/mLCKlyGTmnVrSl0v.png)
*Introduction:*
 - Middle Five Recommendation is **randomly generated**
 - Click The **"Search Button"** like a Magnifier in the middle
 ---> TO  **Jump to the Next Search Page** for More Detailed Search

---

 - 3.3 **Search Page**

```python
class Searching(tk.Frame):
	def __init__(self):
		super().__init__()
		self.master = root
		self.pack()
		root.minsize(520, 300)  # Size
		root.title('Searching') # Name
		self.intWind()

	def intWind(self):
		frame3 = tk.Frame(self) # Year
		tk.Label(frame3, text='Year').grid(row=0, column=0)
		year_container = list(year_set)
		self.year_var = tk.StringVar()
		ttk.Combobox(frame3, values=year_container, textvariable=self.year_var,width='15').grid(row=0, column=1)
		frame3.grid(pady=0.2)
		
		empty_frame = tk.Frame(self) #empty_frame:Type
		empty_frame.grid(pady=0.1)
		tk.Label(empty_frame, text="Type:").grid(row=0, column=0)
		frame4 = tk.Frame(self) #type
		type_list = type_container
		self.var_list = [tk.StringVar() for _ in type_list]
		
		# In Turn
		for index, var in enumerate(self.var_list): 
			checkbutton = tk.Checkbutton(frame4, text=type_list[index], font=("System", 15,'bold'),fg='#556B2F',variable=var)
			checkbutton.grid(row=index // 4, column=index % 4, sticky='w')
		frame4.grid(pady=6)
		
		frame5 = tk.Frame(self) #keywords
		tk.Label(frame5, text="Search:").grid(row=0, column=0)
		self.search_var = tk.StringVar()
		search_entry = tk.Entry(frame5, textvariable=self.search_var)
		search_entry.grid(row=0, column=1)
		frame5.grid(pady=6)
		
		tk.Button(self, text='Searching', width=10, command=self.buttonActive).grid(pady=6)

	def buttonActive(self): #button
		selected_year = self.year_var.get()
		selected_types = [var.get() for var in self.var_list if var.get()]
		selected_type_data = [type for type, var in zip(type_container, self.var_list) if var.get()]
		search_term = self.search_var.get().lower()
		print("Selected type data:", selected_type_data)
		print("Selected year:", selected_year)
		print("Search term:", search_term)

		# Contain the input Infomation
		container=[]
		for i1 in range(1,54214):
			if (train_data["Type"].loc[i1]in selected_type_data ) and (train_data["Year"].loc[i1]== selected_year) and (search_term in (train_data['Description'].loc[i1]).split()):
				container.append(i1)
				
		results = ["Title:"+train_data['Title'].loc[i1]+" Year:"+train_data['Year'].loc[i1]+" Description:"+train_data['Description'].loc[i1][:50]+"..." for i1 in container]
		result_window = tk.Toplevel(root)
		result_window.minsize(520, 300)
		result_window.title("Search Results")
		
		for result in results:
			label = tk.Label(result_window, text=result)
			label.pack()
```
```python
if __name__ == '__main__':
	root = tk.Tk()
	application = Application(root=root)
	application.mainloop()

root.mainloop()
```
**Page 1.**
![Search Page](/imgs/2023-12-21/xq0FyPKpJfgbDZEm.png)
**Page 2.**
![Type](/imgs/2023-12-21/eKIyCi3UeXQKBQqh.png)
**Page 3.**
![输入图片说明](/imgs/2023-12-21/vk4FS5k3zG97sJvP.png)

**Introduction**
 - Step 1: **Select** appropriate Year from **Dropdown box** and **Click**
 - Step 2:**Select** appropriate Type from **Checkbox** and **Click**
 - Step 3:**Input** any numbers of **KeyWords**  (Any Input Format OK)
 - Step 4:**Click** the **Searching Button** TO get results

---
## 4. Part Four : Work Contribution
**Thanks for every members in Gruop No.5**
Each member carefully and responsibly completed their tasks.
```python
labels = ['Huang Siqi', 'Chen Zhuoxuan', 'Liang Yirui', 'Tu Yixin','Chen Qianqi','Li Minghao']
each = 100/6
sizes = [each, each, each, each,each,each]
colors = ['burlywood', 'khaki', 'salmon', 'orchid','pink','dodgerblue']
# Plot Work Contribution PieChart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
text_content="""
1>Import Path and Dataset:\n--Huang Siqi\n
2>Data Preview and Visualization:\n--Tu Yixin\n--Li Minghao\n--Huang Siqi\n
3>User Interface (GUI):\n--Liang Yirui\n--Chen Qianqi\n--Chen Zhuoxuan\n
4>PPT:\n--Tu Yixin
"""
plt.text(1.5,0.4,text_content,fontsize=10,fontstyle='italic',fontweight=15)
plt.title('Work contribution')
plt.show()
```
![输入图片说明](/imgs/2023-12-21/BQQH5w7NUXONB7NY.png)
---
## Detailed Information for Work Contribution
 - [1] **Code**: All
#### a> Path + DataImport:  Inport Dataset and Change Format
*Huang Siqi* (t330034020)
--
#### b> DataProcessing:  Datacleaning, Classification, Resetting
*Li Minghao* (t330034027)
*Huang Siqi* (t330034020)
--
#### c> Visualization: Plot Three Graphs
*Li Minghao*(t330034027)
--

#### d> SearchingPart:  
*Tu Yixin*		(t330034048)
*Li Minghao* (t330034027)
--
#### e> Usage Interface: LoginPage, HomePage, SearchPage
*Chen Qianqi* (t330034001)
*Liang Yirui*  (t330034030)
*Chen Zhuoxuan* (t330034003)
--
#### f> Improvement: Improve Code and Add Remarks
*Liang Yirui*  (t330034030)
*Chen Qianqi* (t330034001
*Chen Zhuoxuan* (t330034003)
*Huang Siqi* (t330034020)
*Tu Yixin*		(t330034048)
*Li Minghao* (t330034027)
--

 - [2]  PPT: All
 #### Designed: 
 *Tu Yixin*		(t330034048)
 ---
 #### Improved:
 *Other*
--
 - [3] Pre: All
 ---


# Thanks For Your Reading !!!
![输入图片说明](/imgs/2023-12-21/lK9BoDDdYKfSA5VD.png)
