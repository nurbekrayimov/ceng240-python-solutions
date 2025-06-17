amount=float(input("Money amount ? // "))
interest=float(input("İnterest rate ? (in percents) // "))
duration=int(input("When will you return (After x months) ? // "))
n=duration
i=interest/100
totalpm=(3000*(1+i)**n)/n

print("{:.2f}".format(totalpm))