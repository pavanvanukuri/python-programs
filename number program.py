class ValueTooSmallError(Exception):
    """raised when the input is too small"""
    pass
class ValueTooLargeError(Exception):
    """raised when the input is too large"""
    pass
number=10

while True:
    try:
        i_num=int(input("enter a number:"))
        if i_num<number:
            raise ValueTooSmallError
        elif i_num>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("this value is too small,try again!")
        print()
    except ValueTooLargeError:
        print("this value is too large")
        print()
print("congarrtulations you gueessed it correctly ")
