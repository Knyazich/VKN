import math
def ob(x,y):
    V=1/3*(math.pi*(x**2)*y)
    V=round(V,2)
    print("Об'єм ", V)
def pl(x,z):
    S=math.pi*x*z+math.pi*(x**2)
    S=round(S,2)
    print("Площа", S)