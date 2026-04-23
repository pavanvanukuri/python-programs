import math
n=int(input ("enter a number:"))
root = math.isqrt(n)
if root*root==n:
     print("perfect number")
else:
     print("not a perfect square")
