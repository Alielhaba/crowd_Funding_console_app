#--------------------------------- Import Part ------------------------------------------- 

import json
import Create_Pro_Script as create
import Login_Script as login
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

#--------------------------------- check Date function-------------------------------------
 
def End_Start_Com(st , en):
    sd=st
    ed=en
    list=[]
    while True:
        if  sd > ed :
            print(f"{Fore.LIGHTRED_EX}End Date Should be after Start Date{Style.RESET_ALL}")
            print(f"{Fore.LIGHTRED_EX}Enter Again : {Style.RESET_ALL}")
            sd = input("> Start Date ")
            ed = input("> End Date ")
            list.append(sd)
            list.append(ed)
            return list
        else:
            break
        
#--------------------------------- Update Values function------------------------------------------- 

def update_value():
    with open('Create.json', 'w') as f:
        json.dump(file_data, f , indent=5)

#--------------------------------- check DUser Choise function------------------------------------------- 

def check_user_choise(OPer):
    
    if OPer == "1" :
        T=input("Enter New Title : ")
        Title=create.chech_Title(T)
        file_data["Project_data"][i]["Project_Title"] = Title
        update_value()
        print(f"{Fore.LIGHTGREEN_EX}Edit Done..{Style.RESET_ALL}")
    elif OPer == "2":
       Details=input("Enter New Details : ")
       file_data["Project_data"][i]["Project_Details"] = Details
       update_value()
       print(f"{Fore.LIGHTGREEN_EX}Edit Done..{Style.RESET_ALL}")
    elif OPer == "3":
        Tr=input("Enter New Target : ")
        Target=create.chech_Target(Tr)
        file_data["Project_data"][i]["Project_Target"] = Target
        update_value()
        print(f"{Fore.LIGHTGREEN_EX}Edit Done..{Style.RESET_ALL}")
    elif OPer == "4":
        print(f"{Fore.LIGHTGREEN_EX}Hint : End Date Should be after Start Date .{Style.RESET_ALL}")
        S_T = input("> Enter New Project Start Date : ")
        Start_pro=create.check_date(S_T)
        E_D = input("> Enter New Project Start Date : ")
        End_pro=create.check_date(E_D)
        list =End_Start_Com(S_T,E_D)
        file_data["Project_data"][i]["Start_Date"] = list[0]
        file_data["Project_data"][i]["End_Date"] = list[1]
        update_value()
        print(f"{Fore.LIGHTGREEN_EX}Edit Done..{Style.RESET_ALL}")
    elif OPer == "6":
        quit()
    else:
        print(f"{Fore.LIGHTRED_EX}Invalid Option Try Again\n{Style.RESET_ALL}")
        inp=input(">> ")
        check_user_choise(inp)        
        
#--------------------------------- Type of Edit function------------------------------------------- 

def type_of_edit():
    print(f"{Fore.LIGHTBLACK_EX}************************************************************************{Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}Choose Operation {Style.RESET_ALL}")
    print("1- Edit Pro_Title")
    print("2- Edit Pro_Details ")
    print("3- Edit Pro_Target")
    print("4- Edit Pro_Date")
    print("6- Exit")
    print(f"{Fore.LIGHTBLACK_EX}************************************************************************{Style.RESET_ALL}")
    OP=input(">>> ")
    check_user_choise(OP)
    
#--------------------------------- Get data from json file ------------------------------------------- 
def Edit():
    global file_data
    global i
    print(f"{Fore.LIGHTYELLOW_EX}Enter project Title Wich you want to Edit :\n{Style.RESET_ALL}")
    project= input(">>  ")
    #open json file
    file=open('Create.json', 'r+')
    file_data = json.load(file)
    size=len(file_data["Project_data"])
    list=create.list_variables

    for i in range(size):
        #check User's Project
        if file_data["Project_data"][i]["User_Email"] == login.log_success and file_data["Project_data"][i]["Project_Title"] == project:
            print("found")
            type_of_edit()
            break
    else:
        print(f"{Fore.LIGHTYELLOW_EX}NO PROJECT WITH THIS NAME{Style.RESET_ALL}")

    file.close()


        
