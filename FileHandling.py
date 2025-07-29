# File Handling Project for CRUD-Operation


from pathlib import Path
import os


print("Welcome To File Handling Project")
print("Choose Your Option:")
print("Press - 1 : For Create File")
print("Press - 2 : For Read File")
print("Press - 3 : For Update File")
print("Press - 4 : For Delete File")
check = int(input("Enter Your Option : "))


# Show all exist file in current directory
def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

# Create File
def createfile():
    try:
        readfileandfolder()
        name = input("Enter File Name you want to create : ")
        p = Path(name)
        if not p.exists() and p.is_file:
            with open(p,"w") as fs:
                data=input("What do  you want to write :---")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY !!!")
        else:
            print("This file already Exist")
    
        
    except Exception as err:
        print(f"An error occured as {err}")
        

# Read File
def readfile():
    name= input("Which file you want to Read : ")
    p=Path(name)
    if p.exists() and p.is_file():
        with open(p,'r') as fs:
            data = fs.read()
            print(data)
        print("READED SUCCESSFULLY !!!")
    
    else :
        print("FILE DOES'NT EXIST")
        

# Update File
def updatefile():
    name=input("Enter Name of file you want to Update : ")
    p = Path(name)
    if p.exists() and p.is_file():
        print("Press 1: for Rename the File")
        print("Press 2: for OverWriting the File")
        print("Press 3: for Appending Content in the File")
        
        res = int(input("Enter Your choice : "))
        
        if res==1:
            name2=input("Tell Your New Name for File :--")
            p2 = Path(name2)
            p.rename(p2)
        
        if res==2:
            with open(p, 'w') as fs:
                data = input("Write what you want to write : ")
                fs.write(data)
        
        if res==3:
            with open(p, 'a') as fs:
                data = input("Write what you want to append : ")
                fs.write(" "+ data)
            



# Delete File
def deletefile():
    name = input("Which file you want to Delete : ")
    p=Path(name)
    
    if p.exists() and p.is_file():
        os.remove(name)
        print("FILE REMOVED SUCCESSFULLY !!!")






if check==1:
    createfile()

if check==2:
    readfile()
    
if check==3:
    updatefile()

if check==4:
    deletefile()