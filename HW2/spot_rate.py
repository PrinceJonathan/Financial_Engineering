import math
t = int(input("Duration of spot rate = "))
print("Price of", t, "year unit zero-coupon bond = ", end = "")
p = float(input())

y = p ** (-1/t) - 1
y *= 100

Y = (-1/t) * math.log(p)
Y *= 100
print(t, "year spot rate of interest:", "%.2f" % y, "%")
print(t, "year spot force of interest:", "%.2f" % Y, "%")
