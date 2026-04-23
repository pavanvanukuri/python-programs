class employee:
    def __init__(self,name):
        self.name=name
    def works(self):
        print("employee do the work")
class manager(employee):
    def work(self):
        print(self.name,"the manager manger manages the team")
class tester (employee):
    def work(self):
         print(self.name,"the tester tests the code")
def employedetails(emp):
     emp.work()
m=manager("girls")
t=tester("boys")
employedetails(m)
employedetails(t)
