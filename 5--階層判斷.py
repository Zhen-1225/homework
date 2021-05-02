m=int(input("請輸入M值:"))
total=1
n=1
while total <m:
    total=total*n
    n=n+1
    
if total !=m:
    print("超過M的最小階乘值"+str(n-1))
    
elif total==m:
    print("超過M的最小階乘值"+str(n))
