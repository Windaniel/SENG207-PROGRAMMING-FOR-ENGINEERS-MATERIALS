# Python string and methods

# When to use single or double quotation marks
print("Ghana's premiers University")
print('He is a "Good" student')

# Indexing: Python indexing starts from 0
 # slising
school= 'university of Ghana'
print(school[:])
print(school[0:]) 
print(school[0]) 
print(school[0:10]) #print out only university or
print(school[0:-9]) 

# len function return the number of characters or element of a variable.
lenght =len(school) #with len function
print(lenght)

# STRING METHODS
# methods & function are the same but depend on the context that each is found 


# Capitalize -- Converts the first character to uppercase
print(school.capitalize())
# Count -- Returns the number of times a specified character occurs in a string
print(school.count('i'))
# Find -- Searches the string for a specified value and returns the position (index) of where it was found
print(school.find('u'))
# Replace -- Replaces a specified value with another
print(school.replace('Ghana','Cape Coast').upper())
# Index -- Searches the string for a specified value and returns the position of where it was found
print(school.index('i'))
# Lower -- Converts a string into lower case
print(school.lower())
# Upper -- Converts a string into upper case
print(school.upper())
# Isalnum -- Returns True if all characters in the string are alphanumeric
print(school.isalnum())
# Isdigit -- Returns True if all characters in the string are digits
print(school.isdigit())
# Isspace -- Returns True if all characters in the string are whitespaces
print(school.isspace())
# Slipt -- Splits the string at the specified separator, and returns a list
print(school.split(' '))
# Startwith -- Returns true if the string starts with the specified value
print(school.startswith('n'))
# Endwith -- Returns true if the string ends with the specified value
code = 'python.py'
print(code.endswith('.py'))

