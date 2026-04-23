class person:
    def __init__(self,name):
       self.name=name
       print("constructer called",self.name)
    def __del__(self):
        print("destructer called",self.name)
p1=person("hello")
del p1


class A:
    def one(self):
        print("this is base class")
class B(A):
    def two(self):
        print("this is derived from class A")
class C(B):
    def Three(self):
        print("this is another class")
obj=C()
obj.one()
obj.two()
obj.Three()
