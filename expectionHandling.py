------------------------------------------->Execption handling<------------------------------------------------------------------------------------------

#Handling a Specific Exception

try:
    num=int(input("Enter a Number: "))
    result=10/num
    print('Result',result)
except ZeroDivisionError:
    print("Error: Cannot diviede by Zero")
except ValueError:
    print("Error:Please enter a Valid Number")
    
    
 

#Handling  Multiple Exceptions

try:
    file_name=input('Enter the name of the file')
    #Open and read the content of the file
    with open(file_name,'r') as file:
        content=file.read()
        print("File Contents",content)
except FileNotFoundError:
    print("Error:File not found:")
except PermissionError:
    print("File doesn't have permission for this file")
except Exception as e:
    print(f"An unexpected error occured:{e}")
    
    
    
try:
    number=int(input(("Enter a Numner")))
    for i in number:
        print(i)
except ValueError:
    print("Not enter  number")