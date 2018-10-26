alpha = 0
deltaH = () #Input delta H list
difficulty = 5949437371609.53 #Change D to the current value
Vc = 6000
Br = 12.5
Vd = 1
R = []# Replace with the value of Hash power of each segement
P =[]#Replace with the value of P,which is the power consumption of each segment
Tavg = 0 # Replace with average Transaction fee for the simulation.
#Calculating profitability threshold for each segment
#Geographic Distribution of bitcoin nodes
#North America = 23.73+3.67 = 27.4 (0.12 USD/Kwatt/H)
#EU = 18.70+6.73+4.75+3.16+2.77+8.44 = 44.55 (0.24 USD/Watt)
#Asia = 6.68+2.58 = 9.26 (0.08 USD/Watt)
#Others = 19.79 (0.11 USD/Watt)
#Weighted Average Electricity cost per watt in usd = (27.3×0.12+44.55×0.24+9.26×0.08+19.79×0.11) / (27.3+44.55+9.26+19.79) = 0.16735084 or 0.0000016 BTC

U = 0.000000000007222222

#Now we calculate the value of Efficiency for each segement
efficiency =[]
for i in range(len(deltaH)):
    efficiency.append((R[i]/1000000)/P[i])
print(len(deltaH))

#Cost of electricity

Ce = []

for i in range(len(deltaH)):
    Ce = (difficulty*(2**32)*P[i]*U)/(R[i])
    print(Ce)


#Next step is to calculate the value of Rev and P_t
rho = Br + Tavg
for i in range(len(deltaH)):
    Rev = rho - Ce
    print(Rev)

#For P_t we will replace the value of Ce wuthe the lowest U
P_t = []
for i in range(len(deltaH)):
    P_t = (difficulty * (2 ** 32) * P[i] * 0.000000000004222222) / (R[i])
    print(P_t)







