def greet(name="hello",age=18):
    print(f'my name is {name} and iam {age} years old')
greet("hello",19)
greet(18,"hello")


c=lambda a=20,b=30:a+b
print(c)

x=100
def display():
    x=10
    print("the value for inside",x)
display()
print("the value for outside:",x)



y=20
def change():
    y=65
    print(y)
change()
print(y)


def add(a,b):
    return a+b
x=int(input("enter x value"))
y=int(input("enter y value"))
result=add(x,y)
print(result)


def sum_natural(n):
    return n * (n + 1) // 2

print(sum_natural(10))

number=-12345
digit_count=len(str(abs(number)))
print(f"the number {number} has digits {digit_count}")

