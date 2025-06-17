x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x3=float(input())
y3=float(input())

v1=(x1,y1)
v2=(x2,y2)
v3=(x3,y3)
sum = []
for i in range(2) :
    s=v1[int(i)]+v2[int(i)]
    sum.append(s)

sumtup=(sum)
print(sumtup)
total=[]
for i in range(2) :
    t=sumtup[int(i)]-v3[int(i)]
    total.append(t)
totaltup=(total)
print(totaltup)

