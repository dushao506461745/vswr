import numpy as np
import math
import matplotlib.pyplot as plt

T=0.01
Uavs = 10
Zin = 0
Zout = 50
gama = (Zin-Zout)/(Zin+Zout)
Ur = Uavs*gama
print(Ur)
print(Ur.imag)
Ur_am = (Ur.real**2+Ur.imag**2)**0.5
print(Ur_am)
Ur_rad = math.acos(Ur_am/Ur.real)

print(Ur_am)
print(Ur_rad)
Z0=10
IL=0
W=1
Q1=0
Q2=Ur_rad
t=np.arange(0,4*np.pi,0.1*np.pi)

tn=0
while(tn!=100):
    print(tn)
    U1=(Uavs)*np.cos(W*t+Q1)
    U2=(Ur_am)*np.cos(W*t+Q2)
    U=U1+U2
    delyQ = 0.02*np.pi
    Q1=Q1+delyQ
