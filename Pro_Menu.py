#--------------------------------- Import Part ------------------------------------------- 

import Create_Pro_Script as create
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import Delete_Pro as delete
import Display_Pros as view
import Edit_project as edit
import Search_Pro as search
#--------------------------------- User Choise function ------------------------------------------- 

def check_user_choise(OPer):
    
    if OPer == "1" :
        create.get_user_data()
        create.Creat_Pro_Func(create.dictionary)
        Menu_func()
    elif OPer == "2":
       view.View_Pro()
       Menu_func()
    elif OPer == "3":
        edit.Edit()
        Menu_func()
    elif OPer == "4":
        delete.delete_pro()
        Menu_func()
    elif OPer == "5":
        search.search()
        Menu_func()
    elif OPer == "6":
        import Auth_Script
        Menu_func()
    elif OPer == "7":
        quit()
        import Auth_Script
    else:
        print(f"{Fore.LIGHTRED_EX}Invalid Option Try Again\n{Style.RESET_ALL}")
        inp=input(">> ")
        check_user_choise(inp)  
        
#--------------------------------- Menu function ------------------------------------------- 

def Menu_func():
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


          
          
    

    


