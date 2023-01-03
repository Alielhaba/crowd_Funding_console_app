import json
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import Create_Pro_Script as create
import Login_Script as login

print(f"{Fore.LIGHTBLACK_EX}\n\n************************************************************************{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}**************************** {Fore.LIGHTYELLOW_EX}All Projects {Fore.LIGHTBLACK_EX}******************************{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
#open projects json_fil 
file=open('Create.json', 'r')
file_data = json.load(file)
size=len(file_data["Project_data"])
list=create.list_variables

for i in range(size):
    #check User's Project
    if file_data["Project_data"][i]["User_Email"] == login.log_success:
        for j in list[1:]:
           print(f"{j}",file_data["Project_data"][i][j])
        print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")

file.close()
    



        


