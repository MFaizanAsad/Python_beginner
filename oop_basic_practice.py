# OOP
class Laptop:
    def __init__(self, brand, performance, popularity):
        self.brand = brand
        self.performance = performance
        self.popularity = popularity
    def __repr__(self):
        return f" the Laptop brand is {self.brand} . \n it has {self.performance} performce . \n it is {self.popularity}."
        #print f" the Laptop brand is {self.brand}., it has {self.performance} performce.it is {self.popularity}."
c1= Laptop("Lenovo", "good","popular")
c2= Laptop("Apple", "excellent", "very popular somesay overrated")
c1