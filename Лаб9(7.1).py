q=("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K" ,"1", "M", "N", "0", "P", "Q", "R", "S", "T", "U", "V", " W", "X", "Y", "Z") 
a=int(input("Кількість вершин: ")) 
b=(input("Перший символ: "))
s=[]
for e in q:
    if e==b:
        r=q.index (e)
        break
for i in range (a):
    s.append(q[r]) 
    r=r+1
    if r==len(q):
        r=0
        for j in range(a-len(s)):
            s.append(q[r])
            r=r+1
            break
print(s) 
d=""
for i in range(0, len(s)): 
    d=d+s[i]
print(d)