import math

S = int(input("輸入一檔無配發股息的股票價格 S："))
u = float(input("輸入上升比例 u："))
d = float(input("輸入下降比例 d："))
r = float(input("輸入無風險利率 r："))
X = int(input("輸入履約價格 X："))
n = int(input("輸入期數 n："))
# S = 160
# u = 1.5
# d = 0.5
# r = 0.18232
# X = 150
# n = 3

R = math.exp(r) 
p = (R - d)/(u - d)

Cn_list = []  #在第n期的call value陣列
for i in range(n+1):
    Cn = S * pow(u, (n-i)) * pow(d, i)
    if Cn - X > 0:
        Cn_list.append(Cn - X)
    else:
        Cn_list.append(0)

print("C[" + str(n) + "]:", Cn_list)

def Cfunc(x):  #降階倒推call value
    for i in range(n-1, -1, -1):
        a_list = []
        for j in range(len(x)-1):
            c = (p * x[j] + (1-p) * x[j+1])/R
            a_list.append(c)
        x = a_list
        print("C[" + str(i) + "]:", x)
    return x

print("call alue 約等於", "%.3f" %  Cfunc(Cn_list)[0])



        
    
