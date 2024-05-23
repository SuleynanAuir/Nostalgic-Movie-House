import time
import sys
import pandas as pd
import random as r
import Create_folders as cf
from Data_Processing import type_list, year_list, train_data
from Data_Cleaning_ import  dataclean


# Showint First Top-10 FilmNames
def TOP_WHOLE():
    print("")
    print("*"*23, flush=True) 
    time.sleep(0.3)
    print("*   THE TOP 10 RANK   *", flush=True) 
    time.sleep(0.3)
    print("*"*23, flush=True) 
    time.sleep(0.3)
    print("")
    for i in range(1,11):
        text="No.{} ---> {}".format(int(i), train_data["Title"][i])
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print("")
        
    return ""
        
        
# recommend any numbers of films
def Random_Rec(recmdNumber): 
    random_list = list()
    for i in range(recmdNumber):
        random_num = r.randint(1,54215)
        if (random_num not in random_list):
            random_list.append(int(random_num))
    
    print("*"*31)
    print("**   Random Recommendation   **")
    print("*"*31)
    print("")
    print("\n")
    words_list = "Guess U LIKE Maybe......"
    for char in words_list:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
    print("")
    print("\n")
    
    
    for index_, rank in zip(random_list, list(range(1,recmdNumber+1))):
        text="No.{}  Year:{}\n--->  Title: <{}> ({})\nIntroduce: {}".format(rank,
                                                                            train_data["Year"].loc[index_],
                                                                            train_data["Title"].loc[index_],
                                                                            train_data["Type"].loc[index_],
                                                                            str((train_data["Description"].loc[index_])[0:80])
                                                                            +"......"+"Waiting FOR U TO EXPLORE!!! ")
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.005) 
        print("")
        print("\n")
    return ""


# take out certain types
def Certain_Type():
    print("") 
    print("*"*19)
    print("**   Type_List   **")
    print("*"*19) ; print("")
    
    
    # Showint First Top-10 FilmNames According to the chosen types
    index_list = range(1,len(type_list)+1)
    
    for num, i in zip(index_list, type_list):
        text = ("{}.<{}>".format(num, i))
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01) 
        print("")
    
    print("")
    type_name = input("Input FileType (According the list above)    >>>")
    type_name = type_name.strip()
    container = train_data.loc[train_data["Type"]==type_name].index
    print("")
    print("*"*26)
    print("**   TOP 10 Films   ** (For:{})".format(type_name)) ; 
    print("*"*26)
    print("")
    

    # Print out First Top-10 FilmNames According to the chosen types
    for i, rank in zip(container, list(range(1,11))):
        text="No.{}  Year:{}\n--->  Title: <{}>".format(rank,
                                                        train_data.loc[i]["Year"],
                                                        train_data.loc[i]["Title"])
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01) 
        print("")
        print("\n")
        

# Randomly take out types in designed numbers
def Random_Type(start=0, end=27, count=6):
    numbers = r.sample(range(start, end+1), count)
    print([type_list[i] for i in numbers])
    # return numbers


# Using single year input or year range input
def Year_Search():
    print("")
    print("*"*57)
    mode = input("**    Choose Year Single Choice(1) /  Year Range(2)    **      ")
    print("*"*57)
    print("")
    
    try:
        mode = int(mode)
    
    except ValueError:
        print("Input forms with \"1\" or \"2\" ")
        print("")
        print("*"*37)
        print("**   Pay Attention to input_mode   **")
        print("*"*37)
        print("")
        
        print("*"*57)
        mode = input("**   ReChoose Year Single Choice(1) /  Year Range(2)   **      ")
        print("*"*57)
        print("")        
        
    # single year input
    if (mode==1):
        print("")
        print("*"*24)
        chosen_year = input("**   Input the Year   **      ")
        print("*"*24)
        print("")  
        print("*"*21)
        print("*                   *")
        print("**    YEAR:{}    **".format(chosen_year))
        print("*                   *")
        print("*"*21)
        
        for i1 in  list(range(1,data_rows)):
            if (train_data["Year"].loc[i1]==chosen_year):
                text="No.{}\n\tTitle:<{}>\n\tType: <{}>\n\tIntroduce: {}".format(i1,
                                                                                 train_data["Title"].loc[i1],
                                                                                 train_data["Type"].loc[i1],
                                                                                 (train_data["Description"].loc[i1])[0:80]
                                                                                 +"......Waiting U Explore")
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.005) 
                print("")   
                print("\t")
                
    # year range input            
    else:
        print("")
        print("*"*34)
        start_time = input("**   Input the Beginning_Time   **      ")
        print("*"*34)
        print("")
        print("*"*28)
        end_time = input("**   Input the End_Time   **      ")
        print("*"*28)
        print("")
        
        print("*"*25)
        print("*                       *")
        print("*     YEAR:{}->{}   *".format(start_time, end_time))
        print("*                       *")
        print("*"*25)
        
        for i1 in  list(range(1,54214)):
            if (start_time<=train_data["Year"].loc[i1]<=end_time):
                text="No.{}\n\tTitle:<{}>\n\tType: <{}>\n\tIntroduce: {}".format(i1,
                                                                                 train_data["Title"].loc[i1],
                                                                                 train_data["Type"].loc[i1],
                                                                                 (train_data["Description"].loc[i1])[0:80]
                                                                                 +"......Wanting U Explore")
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.005) 
                print("")   
                print("\t")
        

def show():
    # Overall Ranking List
    print("*"*29)
    print("**    TOP Recommendation   **")
    print("*"*29)
    TOP_WHOLE()        
    print("")
    print("\n")

    for i in range(3,-1,-1):
        print("{}s....".format(i))
        print("")
        time.sleep(1)

    # Certain Type Recommendation
    words_list="HERE WE COME TO THE TYPE CHOSEN LIST......"
    for char in words_list:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
    print("")
    print("\n")
    Certain_Type()
    print("")
    print("\n")

    # Random Recommendation
    print("*"*23)
    print("**   Guess U LIKES   **")
    print("*"*23)
    num = input("Input the number you want to recomend: ")
    Random_Rec(int(num))

    # Certain Year Search
    print("*"*21)
    print("**   Year Search   **")
    print("*"*21)
    Year_Search()


    print("*"*29)
    print("**   Guess U Likes......   **")
    print("*"*29)
    print("")
    print("\n")
    random_numbers = Random_Type(start=0, end=27, count=6)
    Random_Type()

show()