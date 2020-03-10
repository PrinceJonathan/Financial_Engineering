# 財務工程 108-2 作業 
# 經濟四 李承翰
from prettytable import PrettyTable
p = int(input()) * 10000  #本金
n_y = int(input())  #期數(年)
i = int(input()) / 100  #年利率

n_m = n_y * 12  #期數(月)
p_m = p / n_m  #償還本金(月還
p_i = 0  #本利累計
table = PrettyTable(["期數(月)", "本金(元)", "利息(元)", "本利累計(元)"]) #prettytable現身
for k in range(n_m):
    i_m = p * (i / 12)  #利息(月)
    p -= p_m
    p_i_m = p_m + i_m  #本利累計(月)
    p_i += p_i_m
    table.add_row(["第" + str(k + 1) + "期", int(p_m), int(i_m), int(p_i)]) #add進table
    
print(table) #印出結果