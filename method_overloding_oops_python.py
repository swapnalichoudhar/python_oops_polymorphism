class A:
    def show(self):
        print("welcome")
        
    def show(self,firstname=" "):
        print("welcome",firstname)
        
    def show(self,firstname=" ",lastname=" "):
        print("welcome",firstname,lastname)
        
        
obj=A()
obj.show()
obj.show("swapnali")
obj.show("swapnali","choudhar")


# polymorphism is have multiple form . ther is two types of the polymorphism is 1.compile time 2. Runtime 
# a compile time polymorphism is implemented in compile time. the example of compile time polymorphism is method overloading. the method overloading is the technique
# which allow us to have more than one function but with different dunctionality.. 
