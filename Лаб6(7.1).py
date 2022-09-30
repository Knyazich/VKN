import math
import numpy as np
a=float(input("Перший діапозон a: "))
b=float(input("Дрегий діапозон b: "))
h=float(input("Крок h: "))
for x in np.arange(a,b+h,h): 
  y=math.log10(math.fabs(x+(math.sqrt(x))))
  print("x=%.1f     y=%.3f"%(x,y))