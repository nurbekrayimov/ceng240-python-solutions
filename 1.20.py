s=input()

for i in range(len(s)) :
    if s[i]=="a" and s[i-1]=="h" and s[i+1]=="n" :
        new=s[:i]+"e"+s[i+1:len(s)]

print(new)
