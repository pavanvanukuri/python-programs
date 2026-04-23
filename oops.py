class dog:
    attr1="puppy"
    attr2="snoopy"
    def display(self):
        print("this is",self.attr1)
        print("this is",self.attr2)
tommy=dog()
print(tommy.attr1)
tommy.display()

class prabhas:
    attr1="handsome"
    attr2="taller"
    def display(yogi):
        print("prabhas is ",yogi.attr1)
        print("prabhas is",yogi.attr2)
bahubali=prabhas()
print(bahubali.attr1)
bahubali.display()

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("my name is:",self.name)
        print("age is:",self.age)
s1=student("hello",15)
s1.display()


class car:
    def __init__(self,name,model,cost,colour):
        self.name=name
        self.model=model
        self.cost=cost
        self.colour=colour
    def display(self):
      print("my car is :",self.name)
      print("my car model is:",self.model)
      print("my car cost:",self.cost)
      print("my car colour:",self.colour)
s1=car("audi",2026,50000,"blue")
s1.display()


class display:
        def__init__(self,name)
            self.name=name
d1=display("hi")
print(d1)
