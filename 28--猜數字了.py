a=input("")
t="1234"
y=0
z=0
aa=list(a)
tt=list(t)
w=0
for i in range(0,4):
    if aa[i] == tt[i]:
        y=y+1
    for j in range(0,4):
        if aa[i] == tt[j]:
            z=z+1
print(str(y)+"A"+str(z-y)+"B")