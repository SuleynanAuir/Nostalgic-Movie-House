from Data_Processing import train_data, type_list, year_list, data_rows
from Data_Cleaning_ import dataclean
from Resource import wordBox, img_seasons, question_Box,headImg,\
                     linesBox, chosenBoxs                     
from Resource import *
import pywebio
from pywebio import *
import datetime as t
import random as r
from pywebio.input import *
from pywebio.output import *
import time

import numpy as np


year_list = dataclean(year_list)

# Add an option for "all" type
type_list.insert(0, "All")

global now_time
global moment
global month
global day
# global wordBox

# record and get current time
now_time = t.datetime.now()

moment = now_time.hour
month = now_time.month
day = now_time.day
sec = now_time.second

# change time format into four seasons
if (3<=month<6):
        month='spring'
elif (6<=month<9):
        month='summer'
elif (9<=month<=12):
        month='autumn'
else :
        month="winter"
        
        
if (12<=moment<=18):
        moment='Afternoon'
elif (0<=moment<12):
        moment='Morning'
else:
        moment="Evening"


# Random Imgs for Specific seasons
ranIndex = r.randint(0,4)

ranNum = r.sample(range(0, 11), 3)
ranQes = r.sample(range(0, 7), 3)


global bg 

if (month=="spring"):
    bg=imgDates_spring[ranIndex]

if (month=='summer'):
    bg=imgDates_summer[ranIndex]
    
if (month=='autumn'):
    bg=imgDates_autumn[ranIndex]

if (month=='winter'):
    bg=imgDates_winter[ranIndex]


def Login():

    global bg
    # Cover Design by Rows
    put_row([
    put_image(open("IMG_2392.JPG", 'rb').read(), width='800px', height='400px'),
    put_image(open("Bat_bg.png", 'rb').read(), width='500px', height='400px')])

    inputs = input_group(
       "\tRegister Page",
       [
           input("Input Your Nickname\ne.g. Aiur", name="Nickname"),
           input("NOTICE:First one must be letter and length<=10 !!!\nInput username\n e.g. A113300", name="username"),
           input("Input Your Password", type=PASSWORD, name="password")
       ]
    )
        
    User_Library = []    
    
    if (inputs['username'][0].isalpha() and len(inputs['password'])<=10):
        User_Library.append((inputs['username'],inputs['password']))
    
    if (inputs['username'][0].isalpha()==False or len(inputs['password'])>10):
        inputs = input_group(
       "\tReser Page",
       [   
           input("Input Your username", name="username"),
           input("Input Your password", type=PASSWORD, name="password")
       ]
    )
    
    
    # Retry to Double Verification
    inputs_1 = input_group(
        ("Login Page - ({}) {}".format(moment,now_time)),
        [input("Input Your username", name="username"),
        input("Input Your password", type=PASSWORD,name="password")]
    )
    
    
    clear()

    options=list(range(1,10))

    # Choose Head Image for user
    put_row([
            put_image(open("WechatIMG68.jpg", 'rb').read(), width='100px', height='100px'),
            put_image(open("WechatIMG69.jpg", 'rb').read(), width='100px', height='100px'),
            put_image(open("WechatIMG70.jpg", 'rb').read(), width='100px', height='100px'),

    ])
    
    put_row([
            put_image(open("WechatIMG71.jpg", 'rb').read(), width='100px', height='100px'),
            put_image(open("WechatIMG72.jpg", 'rb').read(), width='100px', height='100px'),
            put_image(open("WechatIMG73.jpg", 'rb').read(), width='100px', height='100px'),

    ])
    
    put_row([
            put_image(open("WechatIMG74.jpg", 'rb').read(), width='100px', height='100px'),
            put_image(open("WechatIMG75.jpg", 'rb').read(), width='100px', height='100px'),
            put_image(open("WechatIMG76.jpg", 'rb').read(), width='100px', height='100px'),

    ])
        
    headImgChosen = radio("Choose Your HeadImage",options) 
    # outpunt an int number
    
    clear()
    
    
    Image_chosen = headImg[headImgChosen-1]
    # Security Question Page
    put_row([
            put_text("Welcome {}!!!\
                \nThis is YourFile\
                \nCome into the Security Question\
                \nRandomly Pick Three Questions:\n".format(inputs["Nickname"])),
            put_image(open(Image_chosen, 'rb').read(), width='100px', height='100px') 
            ])

    inputs_ = input_group("Secret Question",
        [
        input(question_Box[ranQes[0]],name="A1"), 
        input(question_Box[ranQes[1]],name="A2"),
        input(question_Box[ranQes[2]],name="A3")
        ]
    )

    time.sleep(1.5)
    clear()
    
    # Check Input user Name and Password
    for user, pwd in User_Library:
        if user == inputs_1['username'] and pwd == inputs_1["password"]:
            
            # Login Page
            put_row([
                        put_image(open("row0.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("row1.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("row2.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("row3.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("row4.png", 'rb').read(), width='200px', height='230px')])
            

            put_text ("                                                                                     **  Login Successfully  **                                                \nGood <{}> {}  !!! \t\t\t\t----> Lastly Login:{} ({})......\n".format(
                                                                        moment,
                                                                        inputs["Nickname"],
                                                                        now_time,month.upper()))

            # Login Page Design
            put_text(linesBox[0]) ;  time.sleep(3)
            put_text(linesBox[1]) ; time.sleep(1.5)
            put_text(linesBox[2]) ; time.sleep(1.5)
            
            put_text(linesBox[3]) ; time.sleep(1)
            # put_text("Today President Clinton voiced,\t今天克林顿总统表示") ; time.sleep(1)
            put_text(linesBox[4]) ; time.sleep(1)
            put_text(linesBox[5]) ; time.sleep(1)
            put_text(linesBox[6])
                        
            chose = select("Choose your favorite lines:",linesBox)

            # Time Count
            put_text("Exciting is about to be presented......")                      
            for i in range(3,0,-1):
                put_text("{}s...".format(i))
                time.sleep(1)            
            
            clear()
                                
            put_text("Daily recommendations:\n")
            put_text("No.1 {}".format(wordBox[ranNum[0]]))
            time.sleep(1.5)
            put_text("No.2 {}".format(wordBox[ranNum[1]]))
            time.sleep(1.5)
            put_text("No.3 {}".format(wordBox[ranNum[2]]))
            time.sleep(1.5)
            
            
            put_image(open(bg, 'rb').read(), width='1000px', height='300px')
           
            break
        
        while (user != inputs_1['username'] or pwd != inputs_1["password"]):
            
            time.sleep(0.5)
            put_row([
                        put_image(open("p1.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("p2.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("p3.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("p4.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("p5.png", 'rb').read(), width='200px', height='230px')])            
            
            time.sleep(1)
            inputs_1 = input_group (
            ("Login Page - {}".format(moment)),
            [input("Reput Your username !!!", name="username"),
            input("Reput Your password !!!",type=PASSWORD ,name="password")]
                                   )

            clear()
            
            if (user == inputs_1['username'] and pwd == inputs_1["password"]):
                put_text ("Login Successfully\nGood {}!!! {}".format(moment,inputs["Nickname"]))
                put_text (User_Library)
               # Passing the value into this Var
                break
        
    
        
        put_image(open(bg, 'rb').read(), width='1000px', height='300px')
        
        put_text ("Login Successfully\nGood {}!!! {}\n\n{}\n\n".format(moment,inputs["Nickname"],"Here We COME to Film World"))
          

        clear()
    
        put_row([
                        put_image(open("row0.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("row1.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("row2.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("row3.png", 'rb').read(), width='200px', height='230px'),
                        put_image(open("row4.png", 'rb').read(), width='200px', height='230px')])
            

        put_text ("                                                                                     **  Login Successfully  **                                                \nGood {} {} !!! \t\t\t\t------> Lastly Login:{} ({})......\n".format(
                                                                                moment,
                                                                                                                                                                                                                                inputs["Nickname"],
                                                                                                                                                                                                                                now_time,month.upper()))    
        
        put_text(linesBox[0]) ;  time.sleep(1.5)
        put_text(linesBox[1]) ; time.sleep(1.5)
        put_text(linesBox[2]) ; time.sleep(1.5)
            
        put_text(linesBox[3]) ; time.sleep(1)    
        put_text(linesBox[4]) ; time.sleep(1)
        put_text(linesBox[5]) ; time.sleep(1)
        put_text(linesBox[6])
            
                            
        chose = select("Choose your favorite lines:",chosenBoxs)


    boxele=["A",'B']
    chose = select("Choose Year SearchMode (A:Single Year / B:Year Range):",boxele)
   
    
    if (chose=="A"):
        chosenYear = select("Select a specific Year", year_list)
        
        clear()
        
        choses = checkbox("Choose The Type you want",type_list)
        
        if ("All" in choses):
            text=str()
            result=0
            rank=1
            
            for i in range(1,data_rows+1):
                if (train_data["Year"].loc[i]==str(chosenYear)):
                    result+=1
                    each=("No.{}\nTitle:{}({})\n\tType:{}\n\tDescription:{}\n".format(rank,
                        train_data["Title"].loc[i],
                        train_data["Year"].loc[i],
                        train_data["Type"].loc[i],
                        train_data["Description"].loc[i]
                    ))

            result_text=("\n                                                                                {} Results have been Found !!!                                                  \n\n".format(result))                        
            put_text(result_text)
            
            # put_text(text)
            for i in range(1,data_rows+1):
                if (train_data["Year"].loc[i]==str(chosenYear)):
                    result+=1
                    each=("No.{}\nTitle:{}({})\n\tType:{}\n\tDescription:{}\n".format(rank,
                        train_data["Title"].loc[i],
                        train_data["Year"].loc[i],
                        train_data["Type"].loc[i],
                        train_data["Description"].loc[i]
                    ))
                    rank+=1
                    # text+=each
                    each+="\n"
                    each+="\n"
                    put_text(each)
                    time.sleep(0.5)
            
        
        else: #else
            text=str()
            result=0
            rank=1
            
            for i in range(1,data_rows+1):
                if (train_data["Year"].loc[i]==str(chosenYear)) and (train_data["Type"].loc[i] in choses):
                    result+=1
                    each=("No.{}\nTitle:{}({})\n\tType:{}\n\tDescription:{}\n".format(rank,
                        train_data["Title"].loc[i],
                        train_data["Year"].loc[i],
                        train_data["Type"].loc[i],
                        train_data["Description"].loc[i]
                    ))

            result_text=("\n                                                                                {} Results have been Found !!!                                                  \n\n".format(result))            
            put_text(result_text)
            # put_text(text)        
            
            for i in range(1,data_rows+1):
                if (train_data["Year"].loc[i]==str(chosenYear)) and (train_data["Type"].loc[i] in choses):
                    result+=1
                    each=("No.{}\nTitle:{}({})\n\tType:{}\n\tDescription:{}\n".format(rank,
                        train_data["Title"].loc[i],
                        train_data["Year"].loc[i],
                        train_data["Type"].loc[i],
                        train_data["Description"].loc[i]
                    ))
                    rank+=1
                    text=each
                    text+="\n"
                    text+="\n"    
                    
                    put_text(text)
                    time.sleep(0.5)
            
        
    
    if (chose=="B"):
        start_time = select("Choosing Beginning Time:",year_list)
        end_time = select("Choosing Ending Time:",year_list[year_list.index(start_time):])

        clear()
        choses = checkbox("Choose The Type you want",type_list)
        
        if ("All" in choses):
            text=str()
            result=0
            rank=1
            
            for i in range(1,data_rows+1):
                if (str(start_time)<=train_data["Year"].loc[i]<=str(end_time)):
                    result+=1
                    each=("No.{}\nTitle:{}({})\n\tType:{}\n\tDescription:{}\n".format(rank,
                            train_data["Title"].loc[i],
                            train_data["Year"].loc[i],
                            train_data["Type"].loc[i],
                            train_data["Description"].loc[i]
                        ))                
            
            result_text=("\n                                                                                {} Results have been Found !!!                                                  \n\n".format(result))                    
            clear()
            
            put_text(result_text)       
            # put_text(text)
            
            for i in range(1,data_rows+1):
                if (str(start_time)<=train_data["Year"].loc[i]<=str(end_time)):
                    result+=1
                    each=("No.{}\nTitle:{}({})\n\tType:{}\n\tDescription:{}\n".format(rank,
                            train_data["Title"].loc[i],
                            train_data["Year"].loc[i],
                            train_data["Type"].loc[i],
                            train_data["Description"].loc[i]
                        ))
                    rank+=1
                    text=each
                    text+="\n"
                    text+="\n"
                    put_text(text)
                    time.sleep(0.5)
                          
                    
        else: # else
            text=str()
            result=0
            rank=1
            
            for i in range(1,data_rows+1):
                if (str(start_time)<=train_data["Year"].loc[i]<=str(end_time) and train_data["Type"].loc[i] in choses) :
                    result+=1
                    each=("No.{}\nTitle:{}({})\n\tType:{}\n\tDescription:{}\n".format(rank,
                            train_data["Title"].loc[i],
                            train_data["Year"].loc[i],
                            train_data["Type"].loc[i],
                            train_data["Description"].loc[i]
                        ))
                    rank+=1
                    text=each
                    text+=each
                    text+="\n"
                    text+="\n"
            
            result_text=("\n                                                                                {} Results have been Found !!!                                                  \n\n".format(result))                    
            clear()
            
            put_text(result_text)       
            for i in range(1,data_rows+1):
                if (str(start_time)<=train_data["Year"].loc[i]<=str(end_time) and train_data["Type"].loc[i] in choses) :
                    result+=1
                    each=("No.{}\nTitle:{}({})\n\tType:{}\n\tDescription:{}\n".format(rank,
                            train_data["Title"].loc[i],
                            train_data["Year"].loc[i],
                            train_data["Type"].loc[i],
                            train_data["Description"].loc[i]
                        ))
                    rank+=1
                    text=each
                    text+="\n"
                    text+="\n"
                    put_text(text)
                    time.sleep(0.5)

        
            
if __name__ == '__main__':
    Login()
    
    
        
        # 根据时间的变化调整背景的特点 => 