number=(input("請輸入正整數:")).split()
wow=[]
end=[]
s=""
k=0
for x in range(len(number)):
    s=""
    for i in range(x,len(number)):
        s=s+number[i]
        wow.append(s)

for c in range(len(wow)):
    a=int(wow[c])
    k=0
    for y in range(1,a+1):
        if a%y==0:
            k=k+1            
    if k==2:
        end.append(int(a))
if end==[]:
    print("No prime found")
else:
    print("子字串中最大的質數",max(end))



   