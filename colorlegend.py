import matplotlib.pyplot as plt
import matplotlib

def __color_legend_texts__(leg):
    """Color legend texts based on color of corresponding lines"""
    #function taken from http://stackoverflow.com/a/21161986
    for line, txt in zip(leg.get_lines(), leg.get_texts()):
        txt.set_color(line.get_color())

def color_legend(ax,handles=False,labels=False,loc=1):
    """make a color legend without any marker"""
    if((handles or labels) ==False):
        handles, labels = ax.get_legend_handles_labels()
    hcolors=[]
    for h in handles:
        firstobj=h
        if(type(h)==list):
            firstobj=h[0]
        color='k'

        if(type(firstobj)==matplotlib.collections.PathCollection):
            color=tuple(firstobj.get_facecolor()[0])
            
        else:
            color=firstobj.get_color()
        hcolors.append(plt.Line2D((0,0),(0,0), color=color))
    lg=ax.legend(hcolors,labels,loc=loc)
    lg.draw_frame(False)
    __color_legend_texts__(lg)
    for l in lg.legendHandles:
        l.set_linewidth(0)
    return lg


