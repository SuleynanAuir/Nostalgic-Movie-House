import pandas as pd
import numpy as np
# from Data_Cleaning_ import dataclean
# import Year_Count_
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from tkinter.ttk import Combobox 
from PIL import Image, ImageTk  
import os
import random as r
import Create_folders as cf


def dataclean(list_):
    """ Using detaclean_function to delect the error data"""
    
    data_clean = []
    clean_data = []
    for i in list_:
        try:
            m = int(i)
        except ValueError:
            continue
        
        data_clean.append(m)
    
    data_clean.sort()
    return data_clean



train_path = cf.tpath 
train_data = pd.read_csv(train_path, sep=':::', names=['Title', 'Type', 'Description'], engine='python')
train_data = pd.DataFrame(train_data , index=range(1,len(train_data)+1))

name_year = train_data["Title"]
year_container = list()

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

year_container = dataclean(year_container)
# Collection of all existing years
year_set = set(year_container)                
type_container=[]
for i in (train_data["Type"]):
    if (i not in type_container):
        type_container.append(i)
type_container.sort()
year_container.sort()

class Application(tk.Frame):    
    def __init__(self, root):    
        super().__init__(root)    
        self.master = root    
        self.pack()    
        root.minsize(800, 500)  # size    
        root.title('HomePage')  # name    
        self.HomePage()    
        self.search_var = tk.StringVar()
        
        # Replace with your image path 
        image_path =cf.ipath 
        original_image = Image.open(image_path)  
        resized_image = original_image.resize((500, 300))  
        self.bg_image = ImageTk.PhotoImage(resized_image) 
    
        self.bg_label = tk.Label(root, image=self.bg_image)    
        self.bg_label.pack(fill="both", expand=False)  # Adjust the label to fill the available space
        
         
    def HomePage(self):    
        title_font = tkfont.Font(family='Helvetica', size=24, weight='bold')  
        tk.Label(self, text="Nostalgic Movies House", fg='#556B2F', font=title_font).grid(row=0, column=0)  # title  

        subtitle_font = tkfont.Font(family='Helvetica', size=18, weight='bold')  
        tk.Label(self, text="Searching the movies you want", fg='#966F33', font=subtitle_font).grid(row=1, column=0)  # sub-title   
        
        frame = tk.Frame(self)    
        frame.grid(row=3, column=0, columnspan=2, pady=0.2) 

        # Random recommend
        random_list = set()
        for i in range(5):  
            random_num = r.randint(1, 54215)  
            if random_num not in random_list:  
                random_list.add(random_num)  
                ran = [train_data["Title"].loc[i] for i in random_list]    
    
        button = tk.Button(frame, text='Q', command=self.buttonActive)    
        button.grid(row=1, column=0, columnspan=2)     
    
        frame1 = tk.Frame(self)  
        frame1.grid(pady=10)  
        frame1.configure(height=500, width=200) 
        tk.Label(frame1, text="Top Five Recommendation: "+''.join(ran)).grid(row=0, column=0)
        
    
    
    def buttonActive(self):  # button    
        # Check if the Searching window has been created already
        if not hasattr(self, "search_window"):      
            self.search_window = Searching()    
            self.search_window.mainloop()    
        else:    
            self.search_window.destroy()
            # If the window is already created, close it before creating a new one    
            self.search_window = Searching()    
            self.search_window.mainloop()

            
class Searching(tk.Frame):  
    def __init__(self):  
        super().__init__()  
        self.master = root  
        self.pack()  
        root.minsize(520, 300)    # size  
        root.title('Searching')   # name   
        self.intWind()  
        
        
    def intWind(self):  
        frame3 = tk.Frame(self)    # year  
        tk.Label(frame3, text='Year').grid(row=0, column=0)   
        year_container = list(year_set)    
        self.year_var = tk.StringVar()  
        ttk.Combobox(frame3, values=year_container, textvariable=self.year_var,width='15').grid(row=0, column=1)         
        frame3.grid(pady=0.2)

        empty_frame = tk.Frame(self)  # empty_frame:type
        empty_frame.grid(pady=0.1)   
        tk.Label(empty_frame, text="Type:").grid(row=0, column=0)
        
        frame4 = tk.Frame(self)    # type  
        type_list = type_container       
        self.var_list = [tk.StringVar() for _ in type_list]   
        for index, var in enumerate(self.var_list):  # In turn  
            checkbutton = tk.Checkbutton(frame4, text=type_list[index],  font=("System", 15,'bold'),fg='#556B2F',variable=var)     
            checkbutton.grid(row=index // 4, column=index % 4, sticky='w')     
        frame4.grid(pady=6)  

        frame5 = tk.Frame(self)   # keywords  
        tk.Label(frame5, text="Search:").grid(row=0, column=0)    
        self.search_var = tk.StringVar()   
        search_entry = tk.Entry(frame5, textvariable=self.search_var)    
        search_entry.grid(row=0, column=1)    
        frame5.grid(pady=6)    
        
        tk.Button(self, text='Searching', width=10, command=self.buttonActive).grid(pady=6)  
        
        
    def buttonActive(self):  # button   
        selected_year = self.year_var.get() 
        selected_types = [var.get() for var in self.var_list if var.get()]   
        selected_type_data = [type for type, var in zip(type_container, self.var_list) if var.get()]       
        search_term = self.search_var.get().lower()
        
        print("Selected type data:", selected_type_data)   
        print("Selected year:", selected_year)   
        print("Search term:", search_term)        
        
        container=[]
        # filter out Options meeting whole conditions
        for i1 in range(1,54214):
            if train_data["Type"].loc[i1]in selected_type_data and \
               train_data["Year"].loc[i1]== selected_year and \
               search_term in (train_data['Description'].loc[i1]).split():
                   
                container.append(i1)

        results = ["Title:"+train_data['Title'].loc[i1]+'\n'
                   +"Year:"+train_data['Year'].loc[i1]+"\n"
                   +"Description:"+train_data['Description'].loc[i1][:50]
                   +"..."+"\n" for i1 in container]
        
        # results = ["Title: {}\nYear: {}\nType: {}\nDescription: {}".format(train_data[""])]
        
        result_window = tk.Toplevel(root)
        result_window.minsize(520, 300)
        result_window.title("Search Results")
        
        for result in results:
            label = tk.Label(result_window, text=result)
            label.pack() 
            
            
if __name__ == '__main__':    
    root = tk.Tk()
        
    application = Application(root=root)    
    application.mainloop()

root.mainloop()