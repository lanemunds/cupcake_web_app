from abc import ABC,abstractmethod
import csv
from pprint import pprint

class Cupcake(ABC):
    size = "regular"
    
    def __init__(self,name,price,flavor,frosting,sprinkles,filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = sprinkles
        self.filling = filling
    def add_sprinkles(self,*args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
    @abstractmethod        
    def calculate_price(self,quantity):
        return quantity * self.price
        

class Mini(Cupcake):
    size = "mini" 
    def __init__(self,name,price,flavor,frosting,sprinkles):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = sprinkles
    
    def calculate_price(self,quantity):
        return quantity * self.price    
     
     
    
class large(Cupcake):
    size = "large" 
    def __init__(self,name,price,flavor,frosting,sprinkles):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = sprinkles
    
    def calculate_price(self,quantity):
        return quantity * self.price    
     
class regular(Cupcake):
    size = "regular" 
    def __init__(self,name,price,flavor,frosting,sprinkles):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = sprinkles
    
    def calculate_price(self,quantity):
        return quantity * self.price    
    
def read_csv(file)   
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile) 
        for row in reader:
            pprint(row)

read_csv("starter/sample.csv")

my_cupcake_mini = Mini("white",2.99,"white","raspberry",["white chocolate"])          
    

# my_cupcake = Cupcake("red velvet",4.99,"red velvet","cream cheese",[],True)      

# my_cupcake.frosting = "chocolate"
# my_cupcake.filling = "chocolate"
# my_cupcake.name = "double chocolate red velvet"
# my_cupcake.is_miniature = False

# my_cupcake.add_sprinkles("chocolate","rainbow")


