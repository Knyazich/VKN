import sys
sideA=int(sys.argv[1])
sideB=int(sys.argv[2]) 
sideC=int(sys.argv[3])
areaA= sideA * sideB / 2;
print("S=(a*b)/2:", areaA);
areaB= areaA * sideC;
print("V=S*h", areaB)