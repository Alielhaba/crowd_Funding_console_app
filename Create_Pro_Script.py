
import re
import datetime
import json
import Login_Script as login

dictionary={}
list_variables =[ "User_Email","Project_Title" , "Project_Details" , "Project_Target", "Start_Date",  "End_Date" ]

#---------------------------------------------------------------------------------------
#Functions
#---------------------------------------------------------------------------------------

#-----------------------------------Check Str----------------------------------------
def chech_Str(Name):

    Na=Name
    while True:
        if Na.isalpha():
            return Na
        else:
            Na = input("Invalid Value Try Again : ")
            
#-----------------------------------Check Target----------------------------------------
def chech_Target(Num):

    Na=Num
    while True:
        if Na.isnumeric():
            return Na
        else:
            Na = input("Invalid Value Try Again : ")
         
            
def check_date(date):
    D=date
    while True:
        try:
            dateObject = datetime.datetime.strptime(D,'%d-%m-%Y')
            return D
            break
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            D=input("Enter This Date Again ")


#---------------------------------check Password----------------------------------------------

def End_Start_Com(st , en):
    if  en < st :
        print(" End Date Should be after Start Date  : ")
        co = input(" Enter T Date again : ")
    
        
#---------------------------------Registration function------------------------------------------- 
# def Creat_Pro_Func (l):
   
#     try:
#         projects = open("Create.json", "w" , encoding="utf-8")
#         x = json.dumps(l, indent=4)
#         projects.write(x + '\n')
#         projects.close()
#         print('Create Project Succefully') 
#     except Exception as e:
#         print ("Exception Error : " , e)
   
     

def Creat_Pro_Func(new_data, filename='Create.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["Project_data"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 5)
        
        
#--------------------------------- Get User Info ------------------------------------------- 
def get_user_data():
    print("\n***************************( Create Project )****************************")
    print("You Should fill all data. ")
    print("*************************************************************************\n")
    
    Pro_Title = input("> Enter The Project Title : ")
    Title=chech_Str(Pro_Title)
    Pro_Details = input("> Enter Details about project : ")
    Details=chech_Str(Pro_Title)
    Pro_Target = input("> Enter Project Total Target : ")
    Target=chech_Target(Pro_Target)
    print("\n")
    Pro_Start = input("> Enter Project Start Date : ")
    Start=check_date(Pro_Start)
    Pro_End = input("> Enter Project Start Date : ")
    End=check_date(Pro_End) 
    End_Start_Com(Pro_Start,Pro_End)
    print("************************************************************************\n")
    global list_variables
    list_values =[ login.log_success ,Title , Details ,Target, Start , End]
    for i in range(6):
        dictionary[list_variables[i]]=list_values[i]
    #-------------------------------- Storing Data ----------------------------------------
    


# Creat_Pro_Func(dictionary)
  
  
  
