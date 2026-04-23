def main():
    l,b=getvalues()
    area=caluclatearea(l,b)
    display(area)
def getvalues():
    return 5,3
def caluclatearea(x,y):
     return x*y
def display(area):
    print("area is:",area)
main()


def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

nums=[1,2,3,4,5,6]
print(list(map(lambda x:x*2,nums)))

nums=[1,2,3,4,5,6]
print(list(filter(lambda x:x%2!=0,nums)))
print(sum(nums))

from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda x,y:x+y,l))

nums=[1,2,3,4,5]
for i in range(1,6):
    print(i)


