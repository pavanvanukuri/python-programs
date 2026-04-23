n = int(input("Enter a number: "))
temp = n
sum_digits = 0
product_digits = 1

while temp > 0:
    digit = temp % 10
    sum_digits = sum_digits + digit
    product_digits = product_digits * digit
    temp = temp // 10

if sum_digits == product_digits:
    print("Spy number")
else:
    print("Not a Spy number")
