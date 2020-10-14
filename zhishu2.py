import math 
import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.axisartist as axisartist 
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig=plt.figure(figsize=(6,4)) 
ax=axisartist.Subplot(fig,111) 
fig.add_axes(ax) 

def exponential_func(x, a=0.5): 
  y=math.pow(a, x)
  return y

X=np.linspace(-4, 4, 40) 
Y=[exponential_func(x) for x in X]
ax.plot(X, Y)
plt.show()

print(max(X), max(Y)) 
ax.axis[:].set_visible(False) 
ax.axis["x"]=ax.new_floating_axis(0, 0, axis_direction="bottom") 
ax.axis["y"]=ax.new_floating_axis(1, 0, axis_direction="bottom") 

ax.axis["x"].set_axisline_style("-|>", size=1.0) 
ax.axis["y"].set_axisline_style("-|>", size=1.0) 

ax.annotate(s='x', xy=(max(X), 0), xytext=(max(X)+0.5, 0.5)) 
ax.annotate(s='y', xy=(0, 1.0), xytext=(-0.5, max(Y)+0.5)) 

plt.xlim(-4, 5) 
plt.ylim(-1, 17) 
X_lim=np.arange(min(X), max(X)+1, 1)
ax.set_xticks(X_lim) 
Y_lim=np.arange(0, max(Y)+1, 1)
ax.set_yticks(Y_lim) 
ax.annotate(s=r'$y=a^x$',xy=(3, 10), xytext=(3, 10))