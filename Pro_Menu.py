import Create_Pro_Script as create

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
#--------------------------------- User Choise function------------------------------------------- 

def check_user_choise(OPer):
    
    if OPer == "1" :
        create.get_user_data()
        create.Creat_Pro_Func(create.dictionary)
    elif OPer == "2":
       import Display_Pros 
    elif OPer == "3":
        import Edit_project
    elif OPer == "4":
        import Delete_Pro
    elif OPer == "5":
        import Search_Pro
    elif OPer == "6":
        import Auth_Script
    elif OPer == "6":
        quit()
    else:
        print(f"{Fore.LIGHTRED_EX}Invalid Option Try Again\n{Style.RESET_ALL}")
        inp=input(">> ")
        check_user_choise(inp)        

print(f"{Fore.LIGHTBLACK_EX}************************************************************************{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Choose Operation {Style.RESET_ALL}")
print("1- Create Project")
print("2- View All Project ")
print("3- Edit Project")
print("4- Delete Project")
print("5- Search For A project")
print("6- Back")
print("7- Exit")
print(f"{Fore.LIGHTBLACK_EX}************************************************************************{Style.RESET_ALL}")
OP=input(">>> ")
check_user_choise(OP)


          
          
    

    


