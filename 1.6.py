distance=float(input("Distance in miles = "))
speed=float(input("Speed in km/h = "))
s=distance*1.6
t=(s/speed)*60

print("{:.2f}".format(t))
