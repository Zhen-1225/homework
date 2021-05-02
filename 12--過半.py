number=input("輸入").split()
ok=len(number)/2
point=[]
a=0

for i in range(0,len(number)):
    a=0
    for x in number:
        if int(number[i])==int(x):
            a=a+1
    point.append(a)
search=point.index(max(point))
if a>ok:
    print(number[search])
else:
    print("沒有過半")
    