x = int(input("Enter the capacity of the first jug (x) : "))
y = int(input("Enter the capacity of the second jug (y) : "))
z = int(input("Enter the capacity needed to be carried: "))

xn = 0
while z%y!=0:
    z-=x
    xn+=1
    if z<0:
        print("Impossible")
        break
print("jug x needs to filled",xn,"time(s) and jug y needs to be filled",z//y,"time(s)")