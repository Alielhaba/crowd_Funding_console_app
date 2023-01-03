import Login_Script as login
import json
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import Create_Pro_Script as create


def check_user_choise(OPer):
    global Hint
    global project
    if OPer == "1" :
        project= input("Enter project  Start date : \n>>> ")
        print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
        Hint="Start_Date"
    elif OPer == "2":
        project=input("Enter project  End date : \n>>> ")
        print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
        Hint="End_Date"
    elif OPer == "3":
        quit()
    else:
        print(f"{Fore.LIGHTRED_EX}Invalid Option Try Again\n{Style.RESET_ALL}")
        
print(f"{Fore.LIGHTBLACK_EX}* * * * * * * * * * * * * * * *{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}      Choose Option       {Fore.LIGHTBLACK_EX}    *\n                              *{Style.RESET_ALL}")
print(f"1- Search BY Starting Date {Fore.LIGHTBLACK_EX}   *{Style.RESET_ALL}")
print(f"2- Search BY Ending Date {Fore.LIGHTBLACK_EX}     *{Style.RESET_ALL}")
print(f"3- Exit             {Fore.LIGHTBLACK_EX}          *{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}* * * * * * * * * * * * * * * *{Style.RESET_ALL}")
OP=input(">> ")
check_user_choise(OP)

#open json file
file=open('Create.json', 'r+')
file_data = json.load(file)
size=len(file_data["Project_data"])
list=create.list_variables

for i in range(size):
    #check User's Project
    if file_data["Project_data"][i]["User_Email"] == login.log_success and file_data["Project_data"][i][f"{Hint}"] == project:
        for j in list[1:]:
           print(""f"{j}","  ",file_data["Project_data"][i][j])
        print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
        break
else:
    print(f"{Fore.LIGHTYELLOW_EX}NO PROJECT WITH THIS NAME{Style.RESET_ALL}")

file.close()