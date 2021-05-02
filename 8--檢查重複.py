lenth=int(input("輸入第一行正整數為:"))
number=input("輸入第二行正整數為:").split(" ")
c=0
wow=[]
check=0
for i in number:
    c=0
    for j in  range(0,len(number)):
        if i==number[j]:
            c=c+1
    wow.append(c)
big=wow.index(max(wow))

for i in (wow):
    check=check+(i)
print(check)
if check==lenth:
    print("每一個數字剛好出現一次")
else:
    print("最大出現次數的數字",number[big])
    print("出現次數為",max(wow))