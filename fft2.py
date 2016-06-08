import numpy as np
from scipy.fftpack import fft
import sys , math, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../software/models/'))
import utilFunctions as UF

M= 501
hM1= int(math.floor((M+1)/2))
hM2= int(math.floor(M/2))

(fs,x)=UF.waveread('/home/ASP/sms.wav')
x1=x[5000:5000+M]*mp.hamming(M)



N=1024
fftbuffer=np.zeros(N)
fftbuffer[:hM1]=x[hM2:]
fftbuffer[N-hM2:]=x[:hM2]
X=fft(fftbuffer)
mX=abs(X)
pX=np.angle(X)
upX=np.unwrap(np.angle(X))
