import math
x1=int(input("Введіть число a: "))
x2=int(input("Введіть число b: "))
x3=int(input("Введіть число c: "))
Y=int(input("Введіть число Y: "))
if x1 % Y == 0 and x2 % Y == 0 and x3 % Y == 0:
   print("Y є спільним дільником")
else:
    print("Y не є спільним дільником")