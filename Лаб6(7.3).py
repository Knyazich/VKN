import math 
a=float(input("Введіть значення a: ")) 
b=float(input("Введіть значення b: "))
h=float(input("Введіть крок h: "))
y=0.0
spisok=[]
while a<=b:
    y=math.log10(abs(a+math.sqrt(a)))
    spisok.append(y)
    print("Список: ",y)
    a=a+h
k=max(spisok)
print("Найбільше: ", k)
z=min(spisok)
print("Найменше: ", z)