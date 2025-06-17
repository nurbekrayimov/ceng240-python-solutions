from math import *

capacity=float(input())
per100=float(input())
distance=float(input())

totalfuel=(distance/100)*per100
n=(ceil(totalfuel/capacity)-1)
m=ceil(totalfuel/capacity)
leftfuel=(capacity*m)-totalfuel

print(n)
print("{:.2f}".format(leftfuel))
