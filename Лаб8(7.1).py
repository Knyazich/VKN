import math
import numpy as np
x = input("Введіть числа через пробіл: ").split()
y = np.array(list(map(int, x)))
x=sum(y)/len(y)
print(x)