elc=int(input("請輸入電費:"))
A=2.10
AA=2.10

B=3.02
BB=2.68

C=4.39
CC=3.61

D=4.97
DD=4.01

E=5.63
EE=4.50



if elc>=701:
    print("Summer months",(120*A)+(210*B)+(170*C)+(200*D)+((elc-700)*E))
    print("Non-Summer months",(120*AA)+(210*BB)+(170*CC)+(200*DD)+((elc-700)*EE))
elif elc>=501:
    print("Summer months",(120*A)+(210*B)+(170*C)+((elc-500)*D))
    print("Non-Summer months",(120*AA)+(210*BB)+(170*CC)+((elc-500)*DD))
elif elc>=331:
    print("Summer months",(120*A)+(210*B)+((elc-330)*C))
    print("Non-Summer months",(120*AA)+(210*BB)+((elc-330)*CC))
elif elc>=121:
    print("Summer months",(120*A)+((elc-120)*B))
    print("Non-Summer months",(120*AA)+((elc-120)*BB))
elif elc<=120:
    print("Summer months",(120*A))
    print("Non-Summer months",(120*AA))
