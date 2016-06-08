import matplotlib.pyplot as plt
import numpy as np

A=.8
fs=44100
f0=1000
phi=np.pi/2
t=np.arange(-0.002,.002,1.0/fs)
x=A*np.cos(2*np.pi *f0 * t  + phi)


plt.plot(t,x)
plt.axis([-.002,.002,-0.8,0.8])
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()
