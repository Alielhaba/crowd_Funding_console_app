
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


log_success=""

def login ():
    print(f"{Fore.LIGHTBLACK_EX}\n\n************************************************************************{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}**************************** Login *************************************{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
    print(f"{Fore.LIGHTGREEN_EX}Hint : Login With Your ( Email And Password ).{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n{Style.RESET_ALL}")
    x=0
    Email = input("> Email : ")
    Pasword =input("> Password : ")

    try:
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
            
            
        Data_Login.close()
        
        

        


        
    
