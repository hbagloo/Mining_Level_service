import pandas as pd 
import numpy as np 


data_all_df=pd.read_csv("1402-742.csv")

# print (data_all_df.describe())

data_df=data_all_df[['month', 'level', 'block', 'waste', 'sum' , 'ton']]
data=data_df.to_numpy()
operated_levels=data_df['level'].to_numpy()
data_month=data_df['month'].to_numpy()
block=data_df['block'].to_numpy()
waste=data_df['waste'].to_numpy()
tonnage=data_df['ton'].to_numpy()
total_load=data_df['sum'].to_numpy()  # sum of waste and ore


month_list=np.unique(data_df['month'].to_numpy())
level_list=[1095,1105,1120,1135,1150,1165,1180,1195,1210,1225,1240,1255,1270,1285,
1300,1315,1330,1345,1360,1375,1390,1405,1420,1435,1450,1465,1480,1495,1510,1525,
1540,1555,1570,1585,1600,1615,1630,1645,1660,1675]

# print (data_df)



'''
# -------------------- levels total services of the Year ---------------
year_result_list=[]
result_list=[]
print (len(operated_levels), len(waste), len (total_load))



for level in level_list:
    w=0
    t=0
    ore=0
    for i in range (0,len (operated_levels)):
        if (level == operated_levels[i]) and  (block[i] not in ['East-Dump', 'West-Dump'] ) :
            w+=waste [i]
            t+=total_load[i]
            ore +=(total_load[i] - waste [i])
    result_list.append([level,w, ore , t])   #  the order is as Level waste ore sum

print (result_list)
'''
# -------------- # levels total services of the month -----------------
level_mon_info=[]

for mon in month_list:
    for lev in level_list:
        w, t, ore , ton = 0,0,0,0
        for i in range (0, len (data_month)):
            if (mon == data_month[i]) and (lev == operated_levels [i]) and  (block[i] not in ['East-Dump', 'West-Dump']):
                w+=waste [i]
                t+=total_load[i]
                ton+=tonnage[i]
                ore +=(total_load[i] - waste [i])
        level_mon_info.append([mon, lev, ton, w, ore , t])  #  the order is as month Level ton waste ore total_weight


# print (level_mon_info)

# for item in level_mon_info:
#     print (item)

df = pd.DataFrame(level_mon_info)
df = df.rename(columns={0: 'month', 1: 'Level', 2:'tonnage', 3: 'waste', 4: 'ore', 5: 'total_weight'})
print (df)

df.to_excel("Result.xlsx")  



