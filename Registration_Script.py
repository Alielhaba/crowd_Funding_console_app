
import re
import json
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
dictionary = {}
#---------------------------------------------------------------------------------------
#Functions
#---------------------------------------------------------------------------------------

def check_user_choise(OPer):
   
    if OPer == "1" :
        import Login_Script
    elif OPer == "2":
        quit()
    else:
        print(f"{Fore.LIGHTRED_EX}Invalid Option Try Again\n{Style.RESET_ALL}")
        inp=input(">> ")
        check_user_choise(inp)
#-----------------------------------Check Name----------------------------------------
def chech_Name(Name):

    Na=Name
    while True:
        if Na.isalpha():
            return Na
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid Value Try Again\n{Style.RESET_ALL}")
            Na = input(">> ")

#----------------------------------Check Email-----------------------------------------------
def chec_Email(email):
    EM=email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        if re.fullmatch( pattern , EM ):
            return EM
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid Value Try Again\n{Style.RESET_ALL}")
            EM = input(">> ")

#---------------------------------check Password----------------------------------------------

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
        
#---------------------------------Registration function------------------------------------------- 
def Registration_Func (l):
   
    try:
        f1 = open ("Registration_file.txt" , "a")
    except Exception as e:
        print ("Exception Error : " , e)
    else:
        for item in l:
            index = l.index(item)
            if index == 4:
                f1.write(item+"\n")
                break
            
            f1.write(item+":")
                
    print(f"{Fore.LIGHTGREEN_EX}Success Registration\n{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}* * * * * * * * * * * * * * * *{Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}      Choose Option       {Fore.LIGHTBLACK_EX}    *\n                              *{Style.RESET_ALL}")
    print(f"1- Login {Fore.LIGHTBLACK_EX}                   *{Style.RESET_ALL}")
    print(f"2- Exit             {Fore.LIGHTBLACK_EX}          *{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}* * * * * * * * * * * * * * * *{Style.RESET_ALL}")
    OP=input(">> ")
    check_user_choise(OP)
    f1.close()
        
        
#--------------------------------- Get User Info ------------------------------------------- 
print(f"{Fore.LIGHTBLACK_EX}\n\n************************************************************************{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}**************************** Registration *****************************{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
print(f"{Fore.LIGHTGREEN_EX}Hint : You Should fill all data.{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")


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
list_values =[ First_Name , Last_Name , email, Password,  Mobile_Phone ]

for i in range(5):
    dictionary[list_variables[i]] = list_values[i]
    
    
Registration_Func(list_values)
  
  
  
  
"""
try:
f1 = open ("Registration_file.txt" , "a")
except Exception as e:
print ("Exception Error : " , e)
else:
for item in l:
    index = l.index(item)
    if index == 4:
        f1.write(item+"\n")
        break
    
    f1.write(item+":")
    
print('Success Registration')    
f1.close()
"""