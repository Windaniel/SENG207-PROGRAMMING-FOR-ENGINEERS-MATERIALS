# A class is a blue-print for creating objects.
class BakinPang:  #creation of the class 
    pass 

Bread1= BakinPang()  #creation of the objet
print(Bread1)

#flour ,sugar, special_igrdient
Bread1.flour = 'soft' # define attribute 
Bread1.sugar = 20
Bread1.special_ingridient = 'wheat'

print(Bread1.flour)

Bread2= BakinPang()  #creation of the objet
Bread2.flour = 'Hard'
Bread2.sugar = 10
Bread2.special_ingridient = 'coconut'

#object an instance of a class 

number= int('1 2 3')
print(type(number))
