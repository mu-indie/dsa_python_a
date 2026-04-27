#class Product:
 #   def __init__(self, product_name, product_price, product_desc):
  #      self.product_name= product_name
   #     self.product_price = product_price
    ##
    #def get_name(self):
     #   return self.product_name
    
   # def set_name(self, name):
   #     self.product_name = name
#p1 = Product("Tablet", 1423, "qwerty")
#print(p1.get_name())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = self.validate_age(age)
    
    def validate_age (self, age):
        if age > 0 and age < 110:
            return age
        else:
            return 0
        return self.age

    def get_age(self):
        return self.age 

p2 = Person("Jason", 20)
print(p2.get_age())