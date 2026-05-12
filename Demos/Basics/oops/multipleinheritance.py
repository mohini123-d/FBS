class A:

    def show(self):
        print("This IS A Class")

    def display(self):
        print("This is A display class method")

class B:
    def get(self):
        print("This is get method of class B")
    def display(self):
        print("This is B class display method")

class  C(A,B):
    def present(self):
        print("hhhh")


c1 = C()
c1.display()