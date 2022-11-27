def byk():
    global line
    hol=0
    A=("a","o","e","i","u")
    line=line.lower()
    s=list(line)
    for i in s:
        if i in A:
            hol += 1
    return(hol)
f=open('sentences.txt',"r")
a=0
for line in f:
    a+=byk()
print("Всього голосних: ",a)