class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is:",self.name)
        print("age is:",self.age)
p1=person("madhu",24)
p1.display()


class numdisplay:
    def __init__(self):
        self.x=100
    def display(self):
        y=30
        print("instance variable is",self.x)
        print("normal varibale is",y)
n1=numdisplay()
n1.display()
print("outside instance variable is:",n1.x)


class college:
    collegename="aditya"
    def display(self):
      print("college name is:",self.collegename)
c=college()
c.display()
