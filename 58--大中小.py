put=[]
for i in range(1,11):
    number=int(input("請輸入第"+str(i)+"個數字"))
    put.append(number)
put.sort()
put.reverse()
small=sorted(put)
print("最大的三個數字",put[0],put[1],put[2])
print("最小的三個數字",small[0],small[1],small[2])