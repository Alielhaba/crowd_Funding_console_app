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
        pass
    elif OPer == "5":
        pass
    elif OPer == "6":
        quit()
    else:
        print("Enter Valid Nummber")
        

print(f"{Fore.LIGHTBLACK_EX}************************************************************************{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Choose Operation {Style.RESET_ALL}")
print("1- Create Project")
print("2- View All Project ")
print("3- Edit Project")
print("4- Delete Project")
print("5- Search For A project")
print("6- Exit")
print(f"{Fore.LIGHTBLACK_EX}************************************************************************{Style.RESET_ALL}")
OP=input(">>> ")
check_user_choise(OP)


          
          
    

    


