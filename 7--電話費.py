renttime=input("輸入月租型式及通話時間:").split(",")
##==的時候記得型態
##round(數字,取到幾位)，不打的話全部捨去
##print(round(123.45))==123
##print(round(123.45,0))==123.0
##print(round(123.45,-1))==120.0
if renttime[0]=="186" and int(renttime[1])*0.09<=372:
    print("通話費為",round((int(renttime[1])*0.09*0.9)))
elif renttime[0]=="186" and int(renttime[1])*0.09>372:
    print("通話費為",round((int(renttime[1])*0.09*0.8)))
elif renttime[0]=="386" and int(renttime[1])*0.08<=772:
    print("通話費為",round((int(renttime[1])*0.08*0.8)))
elif renttime[0]=="386" and int(renttime[1])*0.08>772:
    print("通話費為",round((int(renttime[1])*0.08*0.7)))
elif renttime[0]=="586" and int(renttime[1])*0.07<=1172:
    print("通話費為",round((int(renttime[1])*0.07*0.7)))
elif renttime[0]=="586" and int(renttime[1])*0.07>1172:
    print("通話費為",round((int(renttime[1])*0.07*0.6)))
elif renttime[0]=="986" and int(renttime[1])*0.06<=1972:
    print("通話費為",round((int(renttime[1])*0.06*0.6)))
elif renttime[0]=="986" and int(renttime[1])*0.06>1972:
    print("通話費為",round((int(renttime[1])*0.06*0.6)))

