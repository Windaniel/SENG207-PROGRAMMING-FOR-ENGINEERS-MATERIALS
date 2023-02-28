# defined a class 
# class Person:
#     pass 

# use the constructor method to define attribute for the person class
class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age 
        # writing a full_name method
    def full_name(self):
        return f"my name is {self.firstName} {self.lastName}, and I'm {self.age} years old"

person = Person('daniel', 'kondo', 20)
print(person.full_name())

