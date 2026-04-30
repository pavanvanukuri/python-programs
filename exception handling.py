try:
   file = open("studentregistration.txt", "r")
except FileNotFoundError:
    print("Error: The file 'studentregistration.txt' does not exist.")
finally:
    print("succesfull")


try:
    print(5/0)
except ZeroDivisionError:
    print("errro:cant do")
finally:
    print("succesfull u did it yaarh!")

try:
    a=10
    print(A)
except NameError:
    print("it is a error")
finally:
    print("hahaa u did rah!")
try:
    def add(x=2,y=4):
        add()
        return x+y
    add()
except RecursionError:
    print("it is a error ra beta")
finally:
    print("hihi u did it")

try:
    x=10
    x.append(4)
except AttributeError:
    print("its  an error boy")
finally:
    print("its over my girl succesful")

try:
    a=int("pavan")
except ValueError:
    print("its an error called value")
finally:
    print("haha its success")

try:
    import bike.txt
except ModuleNotFoundError:
    print("its called error betee")
finally:
    print("module error successs")
    
try:
    a="pavan"
    b=2+a
except TypeError:
    print("its a type error")
finally:
    print("succes my dear")


def demo():
    try:
        return 10
    except:
        return 20
print(demo())


try:
    a=10
    if(a<0):
        print(a)
except AssertionError:
    print("its called error")
finally:
    print("succes ra pavan")
