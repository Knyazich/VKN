import math
def func (x):
        y=(math.e**x**2/math.cos(x+x**4))-4*math.sqrt(x+x**3)
        return(y)
x1=float(input("Введіть x: "))
x=func(x1)
print(x)