class animal:
    def sound(self):
        print("animals make sound")
class mammal(animal):
    def makesound(self):
        print("mammals make sound")
class bird(animal):
    def makessound(self):
     print(" bird make sound eww")
class bat(mammal,bird):
    pass
obj=bat()
obj.makesound()
obj.makessound()
obj.sound()
class methodoverloading:
   def add(self,datatype,*args):
      if(datatype=='int'):
        answer=0
      if(datatype=='str'):
       answer=' '
      for x in args:
         answer=answer+x
      print(answer)
a=methodoverloading()
a.add('int',5,15)
a.add('str','computer','science')

class mother:
    def parent(self):
        print("this is base class")
class child(mother):
    def parent(self):
        super().parent()
        print("this is child class")
ch=child()
ch.parent()



class bankaccount:
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
    def deposit(self,amount):
        self.amount=self.amount+amount
    def withdraw(self,amount):
        self.amount=self.amount-amount
    def display(self):
        print(self.name,"balance is:",self.amount)
ba=bankaccount("cse",10000)
ba=deposit(1000)
ba.withdraw(500)
ba.display()
