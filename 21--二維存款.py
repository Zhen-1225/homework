N=int(input("輸入查詢組數:"))

Search=[["123","456","90000"],["456","789","5000"],["789","888","6000"],
["336","558","10000"],["775","666","12000"],["566","221","7000"]]

for i in range(N):
 
    
    M=(input("輸入帳號、密碼")).split() 
    if M[0]==Search[0][0] and M[1]==Search[0][1]:
        print(Search[0][2])
    elif M[0]==Search[1][0] and M[1]==Search[1][1]:
        print(Search[1][2])
    elif M[0]==Search[2][0] and M[1]==Search[2][1]:
        print(Search[2][2])
    elif M[0]==Search[3][0] and M[1]==Search[3][1]:
        print(Search[3][2])
    elif M[0]==Search[4][0] and M[1]==Search[4][1]:
        print(Search[4][2])
    elif M[0]==Search[5][0] and M[1]==Search[5][1]:
        print(Search[5][2])
    else:
        print("error")
        