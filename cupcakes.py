class Cupcake:
        size = "regular"
    
    def __init__(self,size,name,price,flavor,frosting,sprinkles,filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = sprinkles
        self.filling = filling
    def add_sprinkles(self,*args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
        
            
    

my_cupcake = Cupcake("large","red velvet",4.99,"red velvet","cream cheese",[],True)      

my_cupcake.frosting = "chocolate"
my_cupcake.filling = "chocolate"
my_cupcake.name = "double chocolate red velvet"
my_cupcake.is_miniature = False

my_cupcake.add_sprinkles("chocolate","rainbow")
print(my_cupcake.sprinkles)
