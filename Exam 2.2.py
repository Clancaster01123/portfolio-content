# Christian Lancaster
# 10/17/17
# Exam 2.2

import numpy as np
import matplotlib.pyplot as py

tinitial = 0.0 # initial time
tfinal = 8.0 # final time
nts = 20 # number of timesteps
dt = (tfinal - tinitial)/nts
ts = np.linspace(tinitial,tfinal,num=nts+1)
Y = np.zeros(len(ts))
t = 0.5

def FINER(y):                       #define Euler derivative function
    a = 0.5
    eps = 0.01
    dif = 1
    while dif > eps:
        x = a + (a-np.sin(a)*dt-y)/(np.cos(a)*dt-1)
        a = x
        dif = abs(y - a + np.sin(a)*dt)
    return x
    
Y[0] = 0.001
for j in range(1,nts+1):
    Y[j] = FINER(Y[j-1])
py.plot(ts,Y,'r.')
py.plot(ts,Y,'r',label='Y[0]=0.001')
py.title('NEW EULER')


Y[0] = 0.1
for j in range(1,nts+1):
    Y[j] = FINER(Y[j-1])
py.plot(ts,Y,'g.')
py.plot(ts,Y,'g',label='Y[0]=0.1')


Y[0] = 0.2
for j in range(1,nts+1):
    Y[j] = FINER(Y[j-1])
py.plot(ts,Y,'b.')
py.plot(ts,Y,'b',label='Y[0]=0.2')


Y[0] = 0.5
for j in range(1,nts+1):
    Y[j] = FINER(Y[j-1])
py.plot(ts,Y,'y.')
py.plot(ts,Y,'y',label='Y[0]=0.5')


Y[0] = 1.
for j in range(1,nts+1):
    Y[j] = FINER(Y[j-1])
py.plot(ts,Y,'.')
py.plot(ts,Y,'',label='Y[0]=1.')
py.legend(loc='lower right')
py.show()
