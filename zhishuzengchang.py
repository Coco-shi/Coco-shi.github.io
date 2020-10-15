import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-3.0,3.0,1000)
plt.ylim(0,4)
f=2*np.exp((complex(-0.5,8))*t)
plt.subplot(221)
plt.plot(t,np.real(f))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('x(t)=(Ce^σt)*cos(ωt+φ),σ>0')
plt.xlabel('                                   t')
plt.ylabel('                           x(t)')
plt.show()
