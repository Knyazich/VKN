import math 
x=float(input("Перший діапозон a: "))
b=float(input("Дрегий діапозон b: "))
h=float(input("Крок h: "))
while x<=b: 
    y=float(math.log10(math.fabs(x+(math.sqrt(x)))))
    print("x=%.1f     y=%.3f"%(x,y))
    x=x+h