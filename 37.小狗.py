lenth=int(input("輸入:"))
wow=[]
for i in range(0,lenth):
    where=input("輸入")
    wow.append(where)
for z in wow:
    if int(z)%9==0 or int(z)%11==0:
        print("第",wow.index(z)+1,"點",z)
    


