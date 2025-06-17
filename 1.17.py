
f1=float(input()) #f for filling & e for emptying
f2=float(input())
f3=float(input())
e1=float(input())
e2=float(input())
d1=float(input())
d2=float(input())
l=float(input())
w=float(input())
d=float(input())

A=l*w
v1=f1+f2+f3
v2=v1-e1
v3=v2-e2
t1=((d-d1)*A)/(v1)
t2=((d1-d2)*A/(v2))
t3=abs(((d2-d)*A/(v3)))
total=t1+t2+t3

print(total)