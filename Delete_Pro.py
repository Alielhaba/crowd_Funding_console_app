import Login_Script as login
import json
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import Create_Pro_Script as create



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
        del file_data["Project_data"][i]
        with open('Create.json', 'w') as f:
            json.dump(file_data, f , indent=5)
        break
else:
    print(f"{Fore.LIGHTYELLOW_EX}NO PROJECT WITH THIS NAME{Style.RESET_ALL}")

file.close()




