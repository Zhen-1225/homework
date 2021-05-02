C=int(input("組數為:"))

for i in range(1,C+1):
    
    A,B=map(int,input("第"+str(i)+"組").split())
    W=250*A+175*B    
    print("第",i,"組應收費用",W)