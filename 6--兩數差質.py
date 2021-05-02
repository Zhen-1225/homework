number=input("輸入值為:").split(",")

cc=""
dd=""
ee=""
for x in number:
    cc=str(cc)+str(x)
y=sorted(cc)
yy=list(cc)
yy.sort()
yy.reverse()
for i in y:
    dd=str(dd)+i
for w in yy:
    ee=str(ee)+w    
print(int(ee)-int(dd))    
##sorted可以是str or list 
##list可以用.sort()






