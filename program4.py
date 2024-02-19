# Class in Python

class Product():
    code:int
    name:str
    supplier:str
    price:int

    def info(self):
        print("Product Code ",self.code," Name ",self.name," Supplier ",self.supplier," Price ",self.price)

prod1 = Product()
prod1.code = 1
prod1.name = "Laptop"
prod1.supplier = "ASUS"
prod1.price = 60000
prod1.info()

# Class with Constructor

class Customer():
    # constructor
    def __init__(self,code,name,email,mobile):
        self.code = code
        self.name =  name
        self.email = email
        self.mobile = mobile

    def __str__(self):
        return f"Code :{self.code} Name :{self.name} Email :{self.email} Mobile :{self.mobile}"

cust1 = Customer(1,"Anish","anish@gamil.com",9903941812)
print(cust1)