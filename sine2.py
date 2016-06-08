import matplotlib.pyplot as plt
import numpy as np

N=500
k=5
n=np.arange(-N/2,N/2)
s=np.exp(1j *2 *np.pi* k* n/N)
plt.plot(n, np.imag(s)) #imag(s) for sine part and real(s) for cosine part

plt.axis([-N/2, N/2, -1, 1])
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.show()
