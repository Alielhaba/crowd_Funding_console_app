#--------------------------------- Import Part ------------------------------------------- 
import re
import json
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import Login_Script as login
dictionary = {}
#--------------------------------- check user choise Function ------------------------------------------- 

def check_user_choise(OPer):
   
    if OPer == "1" :
        login.login()
    elif OPer == "2":
        quit()
    else:
        print(f"{Fore.LIGHTRED_EX}Invalid Option Try Again\n{Style.RESET_ALL}")
        inp=input(">> ")
        check_user_choise(inp)
        
#----------------------------------- Check Name Function ----------------------------------------

def chech_Name(Name):

    Na=Name
    while True:
        if Na.isalpha():
            return Na
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid Value Try Again\n{Style.RESET_ALL}")
            Na = input(">> ")

#---------------------------------- Check Email Function -----------------------------------------------

def chec_Email(email):
    EM=email
    #------------------ check Existance -------------------------
    while True:
        file=open('User_Data.json', 'r+')
        file_data = json.load(file)
        size=len(file_data["Users_Data"])
        
        for i in range(size):
            #check User's Project
            if file_data["Users_Data"][i]["email"] == EM:
                print(f"{Fore.RED}ERROR : This Email Is Exist .{Style.RESET_ALL}")
                print(f"{Fore.LIGHTGREEN_EX}Please Re-enter Email .{Style.RESET_ALL}")
                EM = input(">> ")
                break
        else:
            #------------------ check Pattern ----------------------------
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch( pattern , EM ):
                return EM
            else:
                print(f"{Fore.LIGHTRED_EX}Invalid Value Try Again\n{Style.RESET_ALL}")
                EM = input(">> ")
        
        file.close()
   
   

#--------------------------------- check Password Function ----------------------------------------------

def check_Pass(Pass , Conf_Pass):
    pa=Pass
    co=Conf_Pass
    if  Pass == "" :
        print(f"{Fore.LIGHTRED_EX}Password Not match\n{Style.RESET_ALL}")
        pa = input(" Enter Password Again : ")
        co = input(" Confirm Password : ")
    
    if  co == "" :
        print(f"{Fore.LIGHTRED_EX}Password Not match\n{Style.RESET_ALL}")
        pa = input(" Enter Password Again : ")
        co = input(" Confirm Password : ")

    while True:
            if co in pa : 
                return pa
            else:
                print(f"{Fore.LIGHTRED_EX}Password Not match\n{Style.RESET_ALL}")
                pa = input(" Enter Password Again : ")
                co = input(" Confirm Password : ")
        
#--------------------------------- Registration function ------------------------------------------- 
def Registration_Func (dic):
    with open('User_Data.json','r+') as f1:
        file_data = json.load(f1)
        file_data["Users_Data"].append(dic)
        f1.seek(0)
        json.dump(file_data, f1, indent = 6)
        f1.close()
    print(f"{Fore.LIGHTGREEN_EX}Success Registration\n{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}* * * * * * * * * * * * * * * *{Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}      Choose Option       {Fore.LIGHTBLACK_EX}    *\n                              *{Style.RESET_ALL}")
    print(f"1- Login {Fore.LIGHTBLACK_EX}                     *{Style.RESET_ALL}")
    print(f"2- Exit             {Fore.LIGHTBLACK_EX}          *{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}* * * * * * * * * * * * * * * *{Style.RESET_ALL}")
    OP=input(">> ")
    check_user_choise(OP)
   
        
        
#--------------------------------- Get User Info ------------------------------------------- 
print(f"{Fore.LIGHTBLACK_EX}\n\n************************************************************************{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}**************************** Registration *****************************{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
print(f"{Fore.LIGHTGREEN_EX}Hint : You Should fill all data.\n{Style.RESET_ALL}")


First_Name = input("> First Name : ")
F_Name= chech_Name(First_Name)

Last_Name = input("> Last Name : ")
L_Name=chech_Name(Last_Name)

email = input("> Email : ")
Email=chec_Email(email)

Mobile_Phone = input("> Mobile Phone : ")

    
Password = input("> Password : ")
Confirm_Pass = input("> Confirm Password : ")
Pass=check_Pass(Password,Confirm_Pass)

print("************************************************************************\n")
#-------------------------------- Storing Data ----------------------------------------
list_variables =[ "First_Name" , "Last_Name" , "email", "Password",  "Mobile_Phone" ]
list_values =[ First_Name , Last_Name , Email, Password,  Mobile_Phone ]

for i in range(5):
    dictionary[list_variables[i]] = list_values[i]
    
    
Registration_Func(dictionary)
  