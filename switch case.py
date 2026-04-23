day=int (input("enter day number:"))
match day:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("wednesday")
    case 4:
        print("tuesday")
    case 5:
        print("thursday")
    case  6:
        print("friday")
    case 7:
        print("saturday")
    case _:
        print("invalid day")



day=int(input("enter day number: "))
switch = {
    1:"sunday",
    2:"monday",
    3:"tueday",
    4:"wedday",
    5:"thursday",
    6:"friday",
    7:"saturday"
    }

print(switch.get(day,"invalid day"))  
    
    
