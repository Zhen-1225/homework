number=int(input("請輸入一個正整數:"))
c=0
if number<=10:
    for i in range(1,number+1):
        c=0
        for x in range(0,i):
            c=c+i
            print(c,end=" ")
        print("")       