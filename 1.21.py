g1=float(input())
g2=float(input())
g3=float(input())
g4=float(input())
g5=float(input())

list=[g1,g2,g3,g4,g5]
min=min(list)
sum=0
for i in range(len(list)):
    sum+=list[i]

grade=((sum-min)/40)*5
print(grade)