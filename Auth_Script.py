#--------------------------------- Import Part ------------------------------------------- 
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import Login_Script as login
colorama_init()
#--------------------------------- Import Part ------------------------------------------- 
print(f"{Fore.LIGHTBLACK_EX}\n\n************************************************************************{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}**************************** {Fore.LIGHTYELLOW_EX}Crowd-Funding{Fore.LIGHTBLACK_EX} *****************************{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")

#--------------------------------- Check User Choise Function ------------------------------------------- 
def check_user_choise(OPer):
    
    if OPer == "1" :
      import Registration_Script
    elif OPer == "2":
        login.login()
    elif OPer == "3":
        quit()
    else:
        print(f"{Fore.LIGHTRED_EX}Invalid Option Try Again\n{Style.RESET_ALL}")
        inp=input(">> ")
        check_user_choise(inp)
        

print(f"{Fore.LIGHTBLACK_EX}* * * * * * * * * * * **{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Choose Operation    {Fore.LIGHTBLACK_EX}   *{Style.RESET_ALL}")
print(f"1- Registration     {Fore.LIGHTBLACK_EX}   *{Style.RESET_ALL}")
print(f"2- Login            {Fore.LIGHTBLACK_EX}   *{Style.RESET_ALL}")
print(f"3- Exit             {Fore.LIGHTBLACK_EX}   *{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}* * * * * * * * * * * **{Style.RESET_ALL}")
OP=input(">> ")
check_user_choise(OP)


          
          
    

    


