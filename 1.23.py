a=input("Enter values separated by commas: ")
data=a[1:len(a)-1]
tuple_data = tuple(data.split(","))
b= input("Enter change values separated by commas: ")  #
change=b[1:len(b)-1]
change_data = tuple(change.split(","))

converted2 = tuple(map(int, change_data))


list=list(tuple_data)


list[converted2[0]]=str(converted2[1])
answer= tuple(map(int, list))



print(answer)
