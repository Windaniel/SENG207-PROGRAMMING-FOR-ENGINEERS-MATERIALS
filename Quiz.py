# defined a class 
# class Person:
#     pass 

# use the constructor method to define attribute for the person class
class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age 
        self.email= f'{firstName[0]}.{lastName}.st.ug.edu.gh'.lower()
       
        # writing a full_name method
    def full_name(self):
        return f"my name is {self.firstName} {self.lastName}, and I'm {self.age} years old"
    # nethod for initial Name 
    def Initial (self):
        return f'{self.firstName[0]}, {self.lastName[0]}'
    

person = Person('Daniel', 'Kondo', 20)
print(person.full_name())
print(person.Initial())
print(person.email,'\n')

# class student(Person): #Inheriting from the Person class
#     def myfunction(self):
#         return 'student method \n'

# student1= student('yaa','Kofi',12)
# print(student1.myfunction())
# print(student1.email)

class Student(Person):
    def __init__(self, firstName, lastName, age, hall, courses= None):
        super().__init__(firstName, lastName, age)
        self.hall = hall
        if courses is None:
            self.courses = []
        else:
            self.courses= courses 
    def add_courses(self, courses_title):
        if courses_title not in self.courses:
            self.courses.append(courses_title)

    def drop_course(self, course_title):
        if course_title in self.courses:
            self.courses.remove(course_title)
    def print_all_courses(self):
        print(f{self.fullName()})
        for course in self.courses:
            print(course)

student1 = Student('jeanne', 'ofore', 12,'Elisabeth Sey')
student1.add_courses('SENG203')
student1.add_courses('SENG203')
student1.add_courses('SENG204')
student1.add_courses('SENG204')
student1.add_courses('SENG204')
student1.add_courses('SENG201')
student1.add_courses('SENG207')
student1.add_courses('SENG209')
student1.drop_course('SENG203')
# print(student1.courses)
print(student1.print_all_courses())

