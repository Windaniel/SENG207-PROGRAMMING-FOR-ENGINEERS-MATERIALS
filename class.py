class bakingPan:
    department= 'Materials Science and Engineering' #class variable
    unite_price= 6
    def __init__(self, flour, sugar, special_ingredian):
        self.flour= flour # instance.attribute
        self.sugar= sugar
        self.special_ingredient= special_ingredian

    def bread_name(self):
        return f'{self.special_ingredient} bread'
    
    def total_price(self,quantity):
        total = quantity * self.unite_price
        return f'the total price of {quantity} {self.bread_name()} = Ghc {total}'



bread1= bakingPan('soft',20,'wheat') # object = class(argument)
bread2= bakingPan('Hard',10,'coconut')


print(bread1.flour)
print(bread2.flour) 
print(bread2.department) #accessing through the object 
print(bakingPan.department) #accessing the class variable
print(bread1.bread_name()) #object.method 
print(bread2.bread_name()) #object.method 
print(bread1.total_price(10)) #object.method 
print(bread2.total_price(5)) #object.method 
 

 