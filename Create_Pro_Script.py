#--------------------------------- Import part ------------------------------------------- 

import re
import datetime
import json
import Login_Script as login
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

#--------------------------------- Declare Variable------------------------------------------- 

dictionary={}
list_variables =[ "User_Email","Project_Title" , "Project_Details" , "Project_Target", "Start_Date",  "End_Date" ]

#----------------------------------- Check Title function ----------------------------------------

def chech_Title(Name):
    Na=Name
    while True:
        file=open('Create.json', 'r+')
        file_data = json.load(file)
        size=len(file_data["Project_data"])
        
        for i in range(size):
            #check User's Project
            if file_data["Project_data"][i]["User_Email"] == login.log_success and file_data["Project_data"][i]["Project_Title"] == Na:
                print(f"{Fore.RED}ERROR : This Project Is Exist .{Style.RESET_ALL}")
                print(f"{Fore.LIGHTGREEN_EX}Please Re-enter Project Title .{Style.RESET_ALL}")
                Na = input(">> ")
                break
        else:
            #------------------ check alpha ----------------------------
           while True:
            if Na.isalpha():
                return Na
            else:
                print(f"{Fore.RED}ERROR : Invalid Value Enter Title Again.{Style.RESET_ALL}")
                Na = input(">> ")
        
        file.close()
    
            
#-----------------------------------Check Target function ----------------------------------------
def chech_Target(Num):

    Na=Num
    while True:
        if Na.isnumeric():
            return Na
        else:
            print(f"{Fore.RED}ERROR : Invalid Value Enter Target Again.{Style.RESET_ALL}")
            Na = input(">> ")
         
#---------------------------------Rcheck Date function------------------------------------------- 

def check_date(date):
    D=date
    while True:
        try:
            dateObject = datetime.datetime.strptime(D,'%d-%m-%Y')
            return D
            break
        except ValueError:
            print(f"{Fore.RED}ERROR : Incorrect data format, should be YYYY-MM-DD.{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}Enter This Date Again{Style.RESET_ALL}")
            D=input(">> ")


#--------------------------------- check Password function ----------------------------------------------

def End_Start_Com(st , en):
    if  en < st :
        print(f"{Fore.RED}ERROR : End Date Should be after Start Date.{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}Enter End Date again.{Style.RESET_ALL}")
        co = input(">> ")
    
        
#--------------------------------- create Project function ------------------------------------------- 

def Creat_Pro_Func(new_data, filename='Create.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["Project_data"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 5)
        print(f"{Fore.LIGHTGREEN_EX}Creation Done..{Style.RESET_ALL}")

        
        
        
#--------------------------------- Get User Info ------------------------------------------- 
def get_user_data():
    print(f"{Fore.LIGHTBLACK_EX}\n\n************************************************************************{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}************************** {Fore.LIGHTYELLOW_EX}(Create Project ) {Fore.LIGHTBLACK_EX}***************************{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
    print(f"{Fore.LIGHTGREEN_EX}You Should fill all data\n{Style.RESET_ALL}")

    Pro_Title = input("> Project Title : ")
    Title=chech_Title(Pro_Title)
    Pro_Details = input("> project Details : ")
    Pro_Target = input("> Project Total Target : ")
    Target=chech_Target(Pro_Target)
    print("\n")
    Pro_Start = input("> Project Start Date : ")
    Start=check_date(Pro_Start)
    Pro_End = input("> Project End Date : ")
    End=check_date(Pro_End) 
    End_Start_Com(Pro_Start,Pro_End)
    print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
    global list_variables
    list_values =[ login.log_success ,Title , Pro_Details ,Target, Start , End]
    for i in range(6):
        dictionary[list_variables[i]]=list_values[i]
  
  
  
