x=open('D:\sentences.txt', "r")
slova=0
krapka=0
okluk=0
putannya=0
for line in x:
    slova += len(line.split())
    s=list(line)
    for e in s:
        if e==".":
            krapka= krapka+1
        elif e=="!":
            okluk=okluk+1
        elif e=="?":
            putannya=putannya+1
print("Слів: ", slova)
print("Розповідних: ", krapka)
print("Окличних: ", okluk)
print("Питальних:", putannya)