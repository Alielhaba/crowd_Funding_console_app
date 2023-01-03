#--------------------------------- Import Part ------------------------------------------- 
import json
import Login_Script as login
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import Create_Pro_Script as create

#--------------------------------- Delete Project ------------------------------------------- 
def delete_pro():
    print(f"{Fore.LIGHTYELLOW_EX}Enter project Title Wich you want to Delete :\n{Style.RESET_ALL}")
    project= input(">>  ")

    file=open('Create.json', 'r+')
    file_data = json.load(file)
    size=len(file_data["Project_data"])
    list=create.list_variables

    for i in range(size):
        #check User's Project
        if file_data["Project_data"][i]["User_Email"] == login.log_success and file_data["Project_data"][i]["Project_Title"] == project:
            print("found")
            del file_data["Project_data"][i]
            with open('Create.json', 'w') as f:
                json.dump(file_data, f , indent=5)
            print(f"{Fore.LIGHTGREEN_EX}Deletion Done..{Style.RESET_ALL}")
            break
    else:
        print(f"{Fore.LIGHTYELLOW_EX}NO PROJECT WITH THIS NAME{Style.RESET_ALL}")
        import Pro_Menu


    file.close()




