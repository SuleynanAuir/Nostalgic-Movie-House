import pandas as pd
import time 
import Create_folders as cf
from Data_Processing import type_list, year_list, train_data, data_rows
import sys
import pandas as pd
import Create_folders as cf
from Data_Cleaning_ import dataclean



# Certain Name Search
def Name_Search(): # Not Done yet
    print("")
    print("*"*28)
    print("**   Input the FileName   **")
    print("*"*28)
    print("")
    print("*"*24)
    name_input = input("**   Input FilmName   **         ")
    print("*"*24)
    
    for i,each in zip(range(1,data_rows+1),train_data["Title"]):
        if (each==name_input):
            print("")
            print("No.{}".format(i))                             ; print("")
            print("Title:{}".format(train_data.loc[i]["Title"])) ; print("")        
            print("Type:{}".format(train_data.loc[i]["Type"]))   ; print("")
            print("Description:\n--->{}".format(train_data.loc[i]["Description"]), flush=True)
            print("")
            time.sleep(0.1)


# Certain Type Search
def Type_Search(): 
    # printFormat in terminal
    print("")
    print("*"*48) 
    print("**   just copy the type in the showing list   **")
    print("*"*48)
    print("")
    print("Type:")
    print(type_list)
    print("")
    print("*"*35)
    want_ele = input("**   Choose the type you want:   **      ")
    print("*"*35)   ; print("")

    # Filter out type-Search
    for i,each in zip(range(1,data_rows+1),train_data["Type"]):
        if (each==want_ele):
            print("")
            print("No.{}".format(i))                             ; print("")
            print("Title:{}".format(train_data.loc[i]["Title"])) ; print("")        
            print("Type:{}".format(train_data.loc[i]["Type"]))   ; print("")
            print("Description:\n--->{}".format(train_data.loc[i]["Description"]), flush=True)
            print("") ; print("_"*180) ; print("")            
            time.sleep(0.1)


# Certain Key Words Search
def KeyWords_Search ():
    # input 0 to quit the input window and store InputData into ListContainer
    while (1):
        print("Input any KeyWords (Input 0 TO SHUT DOWN)")
        print("")
        Keys_words_container=[]
        KeyWords = input("Input some KeysWord")
        KeyWords = KeyWords.strip()
        KeyWords = KeyWords.lower()
        print("")
        
        if (KeyWords != '0'):
            Keys_words_container.append(KeyWords)
        else:
            break
        
    # Lowercase Packaging For Words
    for i in list(range(1,data_rows+1)):
        each_list = [ x.lower() for x in (train_data["Description"].loc[i]).split()]
        for each in Keys_words_container[0]:
            if (each in each_list):
                Answer_container.append(i)
                continue
            else:
                break
        else:
            continue
    print("")
    print('Keyword_List=[{}]'.format([ x.upper() for x in Keys_words_container]))
    print("")
    
    # Print out object Films
    for i in Answer_container: 
        text="No.{}\n\tTitle:<{}>\n\tType: <{}>\n\tIntroduce: {}".format(i,
                                                                         train_data["Title"].loc[i],
                                                                         train_data["Type"].loc[i],
                                                                         (train_data["Description"].loc[i])[0:50]
                                                                         +"......Waiting U Explore")
        for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.005) 
        print("")   
        print("\t")
        

# Certain Year Search        
def Year_Search():
    print("")
    print("*"*62)
    mode = input("**    Choose Year Single Choice(1) /  Year Range(num!=1)    **      ")
    print("*"*62)
    print("")
    
    # Check Input Format
    try:
        mode=int(mode)
        
    except ValueError:
        print("Input forms with \"1\" or \"2\" ")
        print("")
        print("*"*37)
        print("**   Pay Attention to input_mode   **")
        print("*"*37)
        print("")
        print("*"*57)
        # Retry Input
        mode = input("**   ReChoose Year Single Choice(1) /  Year Range(2)   **      ")
        print("*"*57)
        print("")   

    # Single Year input    
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
        
        # Search certain Single Year
        for i1 in  list(range(1,54214)):
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
    # Year Range
    else:
        # printFormat in terminal
        print("")
        print("*"*34)
        start_time=input("**   Input the Beginning_Time   **      ")
        print("*"*34)
        print("")
        print("*"*28)
        end_time=input("**   Input the End_Time   **      ")
        print("*"*28)
        print("")
        print("*"*25)
        print("*                       *")
        print("*     YEAR:{}->{}   *".format(start_time, end_time))
        print("*                       *")
        print("*"*25)
        
        # Search certain Year Range
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
   
def Seach():
    # Name_Search()
    Type_Search()
    KeyWords_Search()
    Year_Search()
    
    
    
Seach()