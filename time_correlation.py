import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

x = np.linspace(0,100,10001) # (start, finish, how many points)
B  = 20

ys = []
for i in range(0,50): # number of runs 
    y = [1]
    for i in range(1,len(x)):
        y.append(y[-1] + B*np.random.normal(0,B))
    ys.append(y)

C = []
for j in range(0,5000): # max tau
    C_j = []
    for n in range(0,len(ys)):
        A_j_n = []
        A_j_n_0 = []
        for i in range(0,len(ys[n])-j):
            A_j_n.append(ys[n][i]*ys[n][i+j])
            A_j_n_0.append(ys[n][i]*ys[n][i])

    for n in range(0,len(ys)):
        A_j_n_avg = sum(A_j_n)/len(A_j_n)
        A_j_n_0_avg = sum(A_j_n_0)/len(A_j_n_0)
    C_j = np.abs(A_j_n_avg - A_j_n_0_avg)/(np.abs(A_j_n_0_avg)+np.abs(A_j_n_avg))
    C.append(1 - C_j)

# y = [2]
# for i in range(1,len(x)):
#     y.append(y[-1] + B*random.uniform(-1,1))

           
# C = []
# for j in range(0,1000):
#     A_j = []
#     for i in range(0,len(y)-j):
#         A_j.append(y[i]*y[i+j])
#     C.append(sum(A_j)/len(A_j))    

# Aavg = []
# for i in range(0,len(ys[n])):
#     Aavg_i = []
#     for n in range(0,len(ys)):
#         Aavg_i.append(ys[n][i])
#     Aavg.append
# Aavg_squared = (sum(Aavg_n)/len(Aavg_n))*(sum(Aavg_n)/len(Aavg_n))

# C = [ele/max(C) for ele in C]        
# C = [1 - ele for ele in C]
    
# J = fft(C)
# xj = fftfreq(100, 0.1)
# plt.xlim(0,max(xj))
plt.ylim(-0.1,1.1)
plt.plot(x[0:5000],C)
# plt.plot(x[0:500],[Aavg_squared for ele in x[0:500]])
plt.show()
