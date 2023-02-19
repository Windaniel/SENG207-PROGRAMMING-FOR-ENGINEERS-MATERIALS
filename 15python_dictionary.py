# Python dictionary is a collection of key value pair of data.
# It is ordered and mutable.
# It allows duplicate members

student_info = {
    'name': 'Godwin',# key 'name' : value of the key 
    'age' : 19,
    'email':'danielkofi@gmail.com',
    'ID': '10950054',
} 
student_info['name'] = 'Daniel'
print(student_info['name']) # print(Dictionary_Name['keyName'])
print(type(student_info))

fruit = ['mango', 'apple', 'orange']

fruit[1] = 'pineaple'
print(fruit)
# python dictionary are ordered by the keys

# Dictionary Methods

# Copy -- Returns a copy of the dictionary

# Clear -- Removes all the elements from the dictionary

# Pop -- Removes the element with the specified key

# Keys -- Returns a list containing the dictionary's keys

# Values -- Returns a list containing the dictionary's values
