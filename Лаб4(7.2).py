import math
def func (x, y, a, t):
        z=2.33*3.14*(x*math.sin(y)+y*math.cos(a))+(math.e**(a*t))
        return(z)
x1=float(input("Введіть x: "))
y1=float(input("Введіть y: "))
a1=float(input("Введіть a: "))
t1=float(input("Введіть t: "))
f=func(x1, y1, a1, t1)
print(f)