X=int(input("請輸入XX值:"))
Y=int(input("請輸入YY值:"))
Z=((0-X)**2+(0-Y)**2)
if (X>0 and Y>0):
    print("該點位於第一象限","離圓點距離為根號",Z)
elif(X<0 and Y<0):
    print("該點位於第三象限","離圓點距離為根號",Z)
elif(X<0 and Y<0):
    print("該點位於第三象限","離圓點距離為根號",Z)
elif(X>0 and Y<0):
    print("該點位於第四象限","離圓點距離為根號",Z)
elif(X==0 and Y==0):
    print("該點該點位於原點")
elif(X==0 and Y>0):
    print("該點位於上半平面Y軸上","離圓點距離為根號",Z)
elif(X==0 and Y<0):
    print("該點位下半平面Y軸上","離圓點距離為根號",Z)
elif(X>0 and Y==0):
    print("該點位於右半平面X軸上","離圓點距離為根號",Z)
elif(X<0 and Y==0):
    print("該點位於左半平面X軸上","離圓點距離為根號",Z)
    
    