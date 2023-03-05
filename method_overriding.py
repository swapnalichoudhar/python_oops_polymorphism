class A:
    def show(self):
        print("swapnali")
        
class B(A):
    def disp(self):
     super().show()     #super is the keyword that access the properties of parent class too..
     print("swap")
        
obj=B()

obj.disp()
