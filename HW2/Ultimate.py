import pandas as pd

price_list = []
for i in range(6):
    p = int(input("Please type in the price of " + str(i) + " year bond: "))
    price_list.append(p/1000)

forward_list = []
for i in range(6):
    forward_list.append([])
    for j in range(6):
        forward_list[i].append(0)
        
for i in range(6):
    for j in range(i+1, 6):
        f = ((price_list[i])/(price_list[j]))**(1/(j-i)) - 1
        forward_list[i][j] = '%.4f' % f

for i in range(6):
    for j in range(6):
        if i == j:
            forward_list[i][j] = 0
        elif forward_list[i][j] == 0:
            forward_list[i][j] = "-"

forward_table = pd.DataFrame(forward_list)
print(forward_table)