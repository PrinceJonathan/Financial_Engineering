import math
import scipy.stats as st

S = int(input("請輸入股票現值："))
σ = float(input("請輸入股票波動率："))
Dn = int(input("請輸入發放股息次數："))
Dd = int(input("請輸入股息："))
Dtime = []
for i in range(Dn):
    Dtime += input("請輸入第" + i + "個發放月數：")
r = float(input("請輸入無風險利率："))
X = int(input("請輸入履約價："))
t = int(input("請輸入期數(月)："))/12

D = 0
for i in range(Dn):
    D += Dd * math.exp(-r * (int(Dtime[i])/12)) 
        
Shat = S - D

d1 = (math.log(Shat/X) + (r + (1/2)*(σ**2)) * t) / (σ * math.sqrt(t))
# d1 = (math.log(73.02/65) + (0.06 + (1/2)*(0.35**2)) * (6/12)) / (0.35 * math.sqrt(6/12))
d2 = d1 - σ * math.sqrt(t)

p = X * math.exp(-r * t) * st.norm.cdf(-d2) - Shat * st.norm.cdf(-d1)
c = Shat * st.norm.cdf(d1) - X * math.exp(-r * t) * st.norm.cdf(d2) 
print("put price:", p)
print("call price:", c)
