a=int(input())
b=int(input())
c=int(input())

unordered=[a,b,c]
sum=0
for i in range(3):
    sum+=unordered[i]

middle=sum-(min(unordered)+max(unordered))



print(min(unordered),middle,max(unordered))
