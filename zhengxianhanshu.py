import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi,0.01)
y=np.sin(x)

plt.plot(x,y)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('x(t)=Acos(ωt+φ)')
plt.xlabel('                                                                         t')
plt.ylabel('                                                        x(t)')
plt.show()