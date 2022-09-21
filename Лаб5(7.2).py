import math
x1=float(input("Введіть число a: "))
x2=float(input("Введіть число b: "))
x3=float(input("Введіть число c: "))
Y=float(input("Введіть число Y: "))
if Y % x1 == 0 and Y % x2 == 0 and Y % x3 == 0:
   print("Y є спільним дільником")
else:
    print("Y не є спільним дільником")