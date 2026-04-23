age=input("enter age")
if age.isdigit() :
      age= int(age)
      print("valid age")
      n=int(input("enter a number :"))
if 1<n<10:
          print("valid")
else:
    print("invalid")
p=input("enter password")
if len(p)>=6:
        print("strong")
else:
       print("weak")
k=input("enter gmail")
if '@' in k and '.com' in k:
    print ("valid email")
else :
    (invalid)




numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total = total + num
    print("Running Total:", total)
