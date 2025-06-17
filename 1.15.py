from math import *
nx=float(input())
ny=float(input())
r1=float(input())
mx=float(input())
my=float(input())
r2=float(input())

distance=sqrt((nx-mx)**2+(ny-my)**2)-r1-r2
print("{:.2f}".format(distance))