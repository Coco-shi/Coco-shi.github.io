import math 
import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.axisartist as axisartist 
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig=plt.figure(figsize=(6,4)) 
ax=axisartist.Subplot(fig,111) 
fig.add_axes(ax) 

def exponential_func(x1, a1=2):
  y=math.pow(a1, x1)
  return y1

X1=np.linspace(-4, 4, 40) 
Y1=[exponential_func(x1) for x1 in X1] 
ax.plot(X1, Y1，X2, Y2) 
plt.show()
print(max(X1), max(Y1)) 
ax.axis[:].set_visible(False) 
ax.axis["x1"]=ax.new_floating_axis(0, 0, axis_direction="bottom")
ax.axis["y1"]=ax.new_floating_axis(1, 0, axis_direction="bottom") 

ax.axis["x1"].set_axisline_style("-|>", size=1.0) 
ax.axis["y1"].set_axisline_style("-|>", size=1.0) 

ax.annotate(s='x1', x1y1=(max(X1), 0), x1y1text=(max(X1)+0.5, 0.5)) 
ax.annotate(s='y1', x1y1=(0, 1.0), x1y1text=(-0.5, max(Y1)+0.5)) 

plt.xlim(-4, 5)
plt.ylim(-1, 17)
X1_lim=np.arange(min(X1), max(X1)+1, 1)
ax.set_xticks(X1_lim)
Y1_lim=np.arange(0, max(Y1)+1, 1)
ax.set_yticks(Y1_lim)
ax.annotate(s=r'$y1=a^x$',x1y1=(3, 10), x1y1text=(3, 10))


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig=plt.figure(figsize=(6,4)) 
ax=axisartist.Subplot(fig,111) 
fig.add_axes(ax) 

def exponential_func(x2, a2=2):
  y2=math.pow(a2, x2)
  return y2

X2=np.linspace(-4, 4, 40) 
Y2=[exponential_func(x2) for x2 in X2] 
ax.plot(X1, Y1，X2, Y2) 
plt.show()
print(max(X2), max(Y2)) 
ax.axis[:].set_visible(False) 
ax.axis["x2"]=ax.new_floating_axis(0, 0, axis_direction="bottom")
ax.axis["y2"]=ax.new_floating_axis(1, 0, axis_direction="bottom") 

ax.axis["x2"].set_axisline_style("-|>", size=1.0) 
ax.axis["y2"].set_axisline_style("-|>", size=1.0) 

ax.annotate(s='x2', x2y2=(max(X), 0), x2y2text=(max(X2)+0.5, 0.5)) 
ax.annotate(s='y2', x2y2=(0, 1.0), x2y2text=(-0.5, max(Y2)+0.5)) 

plt.xlim(-4, 5)
plt.ylim(-1, 17)
X2_lim=np.arange(min(X2), max(X2)+1, 1)
ax.set_xticks(X2_lim)
Y2_lim=np.arange(0, max(Y2)+1, 1)
ax.set_yticks(Y2_lim)
ax.annotate(s=r'$y2=a^x$',x2y2=(3, 10), x2y2text=(3, 10))


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig=plt.figure(figsize=(6,4)) 
ax=axisartist.Subplot(fig,111) 
fig.add_axes(ax) 