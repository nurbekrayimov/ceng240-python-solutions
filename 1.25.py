list=eval(input())

n=(int(input()))
m=(int(input()))



for i in range(len(list)):
    if i>=(n-1) and i<m :
        list[i]=0


print(list)
