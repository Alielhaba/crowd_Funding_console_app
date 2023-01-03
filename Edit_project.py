import Create_Pro_Script as create
import Login_Script as login
import json
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
#--------------------------------- check Date function------------------------------------------- 
def End_Start_Com(st , en):
    sd=st
    ed=en
    while True:
        if  sd > ed :
            print(f"{Fore.LIGHTYELLOW_EX}End Date Should be after Start Date{Style.RESET_ALL}")
            sd = input(" Enter Start Date again : ")
            ed = input(" Enter End Date again : ")
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
        Title=create.chech_Str(T)
        file_data["Project_data"][i]["Project_Title"] = Title
        update_value()
    elif OPer == "2":
       D=input("Enter New Details : ")
       Details=create.chech_Str(D)
       file_data["Project_data"][i]["Project_Details"] = Details
       update_value()
    elif OPer == "3":
        Tr=input("Enter New Target : ")
        Target=create.chech_Target(Tr)
        file_data["Project_data"][i]["Project_Target"] = Target
        update_value()
    elif OPer == "4":
        print(f"{Fore.LIGHTGREEN_EX}Hint : End Date Should be after Start Date .{Style.RESET_ALL}")
        S_T = input("> Enter New Project Start Date : ")
        Start_pro=create.check_date(S_T)
        E_D = input("> Enter New Project Start Date : ")
        End_pro=create.check_date(E_D)
        End_Start_Com(S_T,E_D)
        file_data["Project_data"][i]["Project_Started_at"] = Start_pro
        file_data["Project_data"][i]["Project_Ended_at"] = End_pro
        update_value()
    elif OPer == "6":
        quit()
    else:
        print(f"{Fore.LIGHTYELLOW_EX}Invalid Choise{Style.RESET_ALL}")
        
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

project= input("Enter project Title Wich you want to Edit : ")
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


        
