#--------------------------------- -- Import Part ------------------------------------------- 
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import Pro_Menu as Menu
import json
import maskpass
#--------------------------------- Declaring Variables -----------------------------------

log_success=""
list_variables =[ "First_Name" , "Last_Name" , "email", "Password",  "Mobile_Phone" ]

#----------------------------------- Login Function ------------------------------------------- 

def login ():
    print(f"{Fore.LIGHTBLACK_EX}\n\n************************************************************************{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}**************************** Login *************************************{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
    print(f"{Fore.LIGHTGREEN_EX}Hint : Login With Your ( Email And Password ).{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
    x=0
    Email = input("> Email : ")
    Password = maskpass.askpass(prompt="> Password ", mask="*")
    
    file=open('User_Data.json', 'r+')
    file_data = json.load(file)
    size=len(file_data["Users_Data"])
    
    for i in range(size):
        #check User's Project
        if file_data["Users_Data"][i]["email"] == Email and file_data["Users_Data"][i]["Password"] == Password:
            print("found")
            global log_success
            log_success = Email
            Menu.Menu_func()
            break
    else:
        print(f"{Fore.RED}ERROR : Email or Password is invalid.{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}Please Re-enter your email and password.{Style.RESET_ALL}")
        login()

    file.close()
    


    
    
    
    
    
    
    
    
    
    
"""try:
        Data_Login = open("Registration_file.txt")
        print(Data_Login)
    except Exception as e:
        print ("Exception Error : " , e)
    else:
        print(Data_Login)
        for i in Data_Login:
            Info = i.strip('\n')
            Info=Info.split(':')
            if Info[2] == Email and Info[3] == Pasword :
                print (" Successfully Loged in ")
                global log_success
                log_success = Email
                import Pro_Menu
                x=1
                break
            
        if x == 0:
            print(f"{Fore.RED}ERROR : Email or Password is invalid.{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}Please Re-enter your email and password.{Style.RESET_ALL}")
            login()
            
            
        Data_Login.close()"""
        
        

        


        
    
