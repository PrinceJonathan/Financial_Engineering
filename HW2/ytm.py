PV = int(input("PV = "))  #Current Bond Price
F = int(input("F = "))  #Bond Par Value
c = int(input("c = ")) / 100  #Bond Coupon Rate(%p.a.)
n = int(input("n = "))  #Years to Maturity
print("Choose your payments plan: ")
print("(a) annually (b) semi-annually (c) quarterly")
m = input()  #輸入Payment方案
e = 1000000  #取小數點後4位數
if m == "a":
    m = 1
    n *= m
    C = F * c / m
    for i in range(1, e):
        r = i/e
        P = C * (1 - (1 + r/m)**(-n))/(r/m) + F/(1+r/m)**n
        if P < PV:
            r = 100*r/m
            print("%.4f" % r, end = "%")
            break
elif m == "b":
    m = 2
    n *= m
    C = F * c / m
    for i in range(1, e):
        r = i/e
        P = C * (1 - (1 + r/m)**(-n))/(r/m) + F/(1+r/m)**n
        if P < PV:
            r = 100*r/m
            print("%.4f" % r, end = "%")
            break
else:
    m = 4
    n *= m
    C = F * c / m
    for i in range(1, e):
        r = i/e
        P = C * (1 - (1 + r/m)**(-n))/(r/m) + F/(1+r/m)**n
        if P < PV:
            r = 100*r/m
            print("%.4f" % r, end = "%")
            break