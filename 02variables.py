
from keyword import kwlist 

print(kwlist)

# A variable is a placeholder for storing data in the computer memory

name = "Godwin Kondo"
print(name)
first_school= "University of Ghana"
secondSchool= "KNUST"
ThirdSchool= "University of Cap Coast"

# VARIABLE NAMING RULES
# 1. Use descriptive names
# 2. Cannot use white spaces and hyphen in between names
# 3. Use underscore
# 4. Use camelCase notation
# 5. PascalCase notation 
# 6. snake_case notation
# 7. Cannot start with a number but can have a number in it
# 8. Cannot use reserved keywords
# 9. Python is case-sensitive

age= 20
Age= 20
print(type(age))

# *x for list variable that store more than one data  

a, *b= 20, 30, 40 
print(a, b, sep= "-")



# Multiple Assignment or Unpacking
x, y ,z= 10 ,20 , 30
# x= 10
# y= 20
# z= 30