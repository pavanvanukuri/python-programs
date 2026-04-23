first = 0
second = 1

a = int(input("Enter limit: "))

for i in range(a):
    print(first)
    next = first + second
    first = second
    second = next
