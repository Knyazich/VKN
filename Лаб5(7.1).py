import math
x = float(input("Введіть значення аргументу функції x: "))
def f1(x1):
    rez=(-6*x1**2)+math.sin(x1)
    return(rez)
def f2(x2):
    rez=math.log1p(math.fabs(x2+math.sin(x2)))
    return(rez)
def f3(x3):
    rez=12+math.fabs(math.sin(2*x3))
    return(rez)
y=0.0
if x >= -0.7:
    y = f1(x)
elif -9.9 < x:
    y = f2(x) 
else :
    y = f3(x)
print(y)
