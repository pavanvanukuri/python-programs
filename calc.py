def add(a,b):
    return a+b
def multiply(a,b):
    return a*b


def display():
    a=10
    print("inside value is :",a)
display()
print(a)


x=10
def display():
    print("inside fun:",x)
display()
print("outside fun:",x)


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(factorial(n))


