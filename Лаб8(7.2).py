import numpy as np
import random
M = int(input("Введіть M: "))
N = int(input("Введіть N: "))
masiv1=np.zeros((M,N),dtype=np.int)
for i in range(M):
    for j in range (N):
        masiv1[i][j]=random.randint(1,20)
print(masiv1)
        
print('input\n',masiv1)
b = np.sum
print('sum\n',b)

def maximumSum(masiv1):
    maxi = 0
    for x in masiv1:
        sum = 0
        for y in x:
            sum+= y     
        maxi = max(sum, maxi)       
    return maxi

R = maximumSum(masiv1)
for i in range(M):
    s=sum(masiv1[i])
    if s == R:
        print (masiv1[i])