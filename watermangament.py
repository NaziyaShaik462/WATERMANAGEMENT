def Total_water_bill(flat_mem,monthly_water,no_of_guest1,no_of_guest2,ratio_sum):
    total_mem=flat_mem+no_of_guest1+no_of_guest2
    total_liters=total_mem*10*30
    print(total_liters,end=" ")
    per_ratio=int(monthly_water/ratio_sum)
    corp_water_liters=ratio_list[0]*per_ratio
    corp_water_amnt=corp_water_liters*1
    bor_water_liters=int(ratio_list[1]*per_ratio)
    bor_water_amnt=int(bor_water_liters*1.5)
    corp_bor_amnt=(bor_water_amnt+corp_water_amnt)
    tank_water=total_liters-monthly_water
    amnt_tank_water=0
    if tank_water==0 or tank_water<=500:
        amnt_tank_water=tank_water*2
    elif tank_water==501 or tank_water<=1500:
        amnt_tank_water=(500*2)+(tank_water-500)*3
    elif tank_water==1501 or tank_water<=3000:
        amnt_tank_water=(500*2)+(1000*3)+(tank_water-1500)*5
    elif tank_water>=3001:
        amnt_tank_water=(500*2)+(1000*3)+(1500*5)+(tank_water-3000)*8
    total_amnt=amnt_tank_water+corp_bor_amnt
    print(total_amnt,end=" ")
"""
Inputs take as 
    2 3:7
    4
    1
"""
#ALLOT_WATER 3 2:1 taken as 2 3:7
n=(input().split())
if int(n[0])==2:
    flat_mem=3
    monthly_water=900
elif int(n[0])==3:
    flat_mem=5
    monthly_water=1500
ratio=n[1]
#ADD_GUESTS if guests are there then we will take the no_of guests else we have to take "0"
no_of_guest1=int(input())#ADD_GUESTS 4
no_of_guest2=int(input())#ADD_GUESTS 1
ratio_list=[]
ratio_sum=0
for i in ratio:
    if i ==":":
        pass
    else:
        ratio_list.append(int(i))
for i in ratio_list:
    ratio_sum=ratio_sum+i
Total_water_bill(flat_mem,monthly_water,no_of_guest1,no_of_guest2,ratio_sum)