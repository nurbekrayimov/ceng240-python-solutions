id1=int(input())
m1=float(input())
f1=float(input())
id2=int(input())
m2=float(input())
f2=float(input())
id3=int(input())
m3=float(input())
f3=float(input())
id=int(input())

database=dict({id1:(m1,f1),id2:(m2,f2),id3:(m3,f3)})

grade=(database[id][0]+database[id][1])/2
print(grade)

