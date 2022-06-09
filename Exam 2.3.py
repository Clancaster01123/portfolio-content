# Christian Lancaster
# 10/17/17
# Exam 2.3

import numpy as np
import matplotlib.pyplot as py

k = 1
m = 2
l = 3
A=np.matrix([[2*k,-k,0,0,0],[-k,2*k,-k,0,0],[0,-k,2*k,-k,0],[0,0,-k,2*k,-k],
[0,0,0,-k,2*k]])
eval,evec = np.linalg.eig(A)
print(eval)
print(evec)
w_1=np.sqrt(eval[0]/m)
w_2=np.sqrt(eval[1]/m)
w_3=np.sqrt(eval[2]/m)
w_4=np.sqrt(eval[3]/m)
w_5=np.sqrt(eval[4]/m)

print(w_1,w_2,w_3,w_4,w_5)

t=np.linspace(0,8*np.pi,200)
mode1 = evec[0,0]*np.cos(w_1*t)+l
mode2 = evec[1,0]*np.cos(w_1*t)+2*l
mode3 = evec[2,0]*np.cos(w_1*t)+3*l
mode4 = evec[3,0]*np.cos(w_1*t)+4*l
mode5 = evec[4,0]*np.cos(w_1*t)+5*l
py.figure(1)
py.title('Omega 1')
py.plot(t,mode1,'r',label='mode 1')
py.plot(t,mode2,'b',label='mode 2')
py.plot(t,mode3,'purple',label='mode 3')
py.plot(t,mode4,'black',label='mode 4')
py.plot(t,mode5,'green',label='mode 5')
py.legend(loc='upper right')
py.show()


mode1 = evec[0,1]*np.cos(w_2*t)+l
mode2 = evec[1,1]*np.cos(w_2*t)+2*l
mode3 = evec[2,1]*np.cos(w_2*t)+3*l
mode4 = evec[3,1]*np.cos(w_2*t)+4*l
mode5 = evec[4,1]*np.cos(w_2*t)+5*l
py.figure(2)
py.title('Omega 2')
py.plot(t,mode1,'r',label='mode 1')
py.plot(t,mode2,'b',label='mode 2')
py.plot(t,mode3,'purple',label='mode 3')
py.plot(t,mode4,'black',label='mode 4')
py.plot(t,mode5,'green',label='mode 5')
py.legend(loc='upper right')
py.show()


mode1 = evec[0,2]*np.cos(w_3*t)+l
mode2 = evec[1,2]*np.cos(w_3*t)+2*l
mode3 = evec[2,2]*np.cos(w_3*t)+3*l
mode4 = evec[3,2]*np.cos(w_3*t)+4*l
mode5 = evec[4,2]*np.cos(w_3*t)+5*l
py.figure(3)
py.title('Omega 3')
py.plot(t,mode1,'r',label='mode 1')
py.plot(t,mode2,'b',label='mode 2')
py.plot(t,mode3,'purple',label='mode 3')
py.plot(t,mode4,'black',label='mode 4')
py.plot(t,mode5,'green',label='mode 5')
py.legend(loc='upper right')
py.show()

mode1 = evec[0,3]*np.cos(w_4*t)+l
mode2 = evec[1,3]*np.cos(w_4*t)+2*l
mode3 = evec[2,3]*np.cos(w_4*t)+3*l
mode4 = evec[3,3]*np.cos(w_4*t)+4*l
mode5 = evec[4,3]*np.cos(w_4*t)+5*l
py.figure(4)
py.title('Omega 4')
py.plot(t,mode1,'r',label='mode 1')
py.plot(t,mode2,'b',label='mode 2')
py.plot(t,mode3,'purple',label='mode 3')
py.plot(t,mode4,'black',label='mode 4')
py.plot(t,mode5,'green',label='mode 5')
py.legend(loc='upper right')
py.show()


mode1 = evec[0,4]*np.cos(w_5*t)+l
mode2 = evec[1,4]*np.cos(w_5*t)+2*l
mode3 = evec[2,4]*np.cos(w_5*t)+3*l
mode4 = evec[3,4]*np.cos(w_5*t)+4*l
mode5 = evec[4,4]*np.cos(w_5*t)+5*l
py.figure(5)
py.title('Omega 5')
py.plot(t,mode1,'r',label='mode 1')
py.plot(t,mode2,'b',label='mode 2')
py.plot(t,mode3,'purple',label='mode 3')
py.plot(t,mode4,'black',label='mode 4')
py.plot(t,mode5,'green',label='mode 5')
py.legend(loc='upper right')
py.show()

