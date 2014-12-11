import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import colorlegend
fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(1,2,1)
# example for the simplist case
# define label in plot functions and call color_legend directly
xs=np.linspace(0,10,100)
y1=np.sin(xs)
y2=np.sin(xs*2)
ax1.plot(xs,y1,label="y=sin(x)",color='b')
ax1.scatter(xs,y2,label="y=sin(2x)",color='g')
lg1=colorlegend.color_legend(ax1,loc=2)


ax2 = fig.add_subplot(1,2,2)
# call color_legend with custum handles and labels
# in this way you get more control
xs=np.linspace(0,10,100)
y1=np.sin(xs)
y2=np.sin(xs*2)
line1=ax2.plot(xs,y1,color='b')
# line2 will not appear in legend because we do not
# pass it to color_legend
line2=ax2.plot(xs,y2,color='r')
scat1=ax2.scatter(xs,y2,color='g')
handles=[line1,scat1]
labels=["y=sin(x)","y=sin(2x)"]
lg2=colorlegend.color_legend(ax2,handles=handles,labels=labels,loc=2)


plt.savefig("example.png")
