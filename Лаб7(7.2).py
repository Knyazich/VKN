a=str
s=[]
while not a=="end":
    a=str(input("Введіть слова: "))
    s.append(a)
    if a=="end":
        s.pop()
n=0
q=0
e=("")
r=(",")
while n<len(s):
    s2=(s[n])
    for q in range(100):
        w=(s2[q])
        e=e+w+r
        if q==len(s2)-1:
            e=e+r
            break
    n=n+1
print(e)