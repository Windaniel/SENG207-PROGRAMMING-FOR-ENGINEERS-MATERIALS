# Python input function
# modules are files in the system that are hiding
from getpass import getpass
import maskpass #to mask the password 

# name= input("Enter your Name :")
# print("your name is :", name)
# password = input("enter your password")
# print("your pswd is: ", password)

#using the module getpass
# password = getpass("Enter your password")
# print("your password is: ", password)


pswd= maskpass.askpass("enter your password: ")
print(pswd)