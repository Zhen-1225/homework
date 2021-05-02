lenth=int(input("請輸入:"))
for i in range(0,lenth):
    blood=input("請輸入測試的資料").split(" ")    
    if blood[0]=="O" and blood[1]=="O" and blood[2]=="O":
        print("YES")
    elif blood[0]=="O" and blood[1]=="A" and (blood[2]=="O" or blood[2]=="A"):
        print("YES")
    elif blood[0]=="O" and blood[1]=="B" and (blood[2]=="B" or blood[2]=="O"):
        print("YES")
    elif blood[0]=="O" and blood[1]=="AB" and (blood[2]=="A" or blood[2]=="B"):
        print("YES")
    elif blood[0]=="A" and blood[1]=="A" and (blood[2]=="A" or blood[2]=="O"):
        print("YES")
    elif blood[0]=="A" and blood[1]=="B" and (blood[2]=="A" or blood[2]=="B" or blood[2]=="O" or blood[2]=="AB"):
        print("YES")
    elif blood[0]=="A" and blood[1]=="AB" and (blood[2]=="A" or blood[2]=="B" or blood[2]=="AB"):
        print("YES")
    elif blood[0]=="B" and blood[1]=="B" and (blood[2]=="B" or blood[2]=="O"):
        print("YES")
    elif blood[0]=="B" and blood[1]=="AB" and (blood[2]=="A" or blood[2]=="B" or blood[2]=="AB"):
        print("YES")
    elif  blood[0]=="AB" and blood[1]=="AB" and (blood[2]=="A" or blood[2]=="B" or blood[2]=="AB"):
        print("YES")
    else:
        print("IMPOSSIBLE")