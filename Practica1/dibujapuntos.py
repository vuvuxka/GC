import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from matplotlib.lines import Line2D
from parte3 import *


class CreatePoints(object):
    """Draw and drag points.

    Use left button to place points.
    Points are draggable. Use right button
    to disconnect and print and return
    the coordinates of the points.

    Args:
         fig: matplotlib figure
         ax: matplotlib axes
    """
    
    def __init__(self, fig, ax):
        self.circle_list = []

        self.x0 = None
        self.y0 = None

        self.fig = fig
        self.ax = ax
        
        self.cidpress = fig.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = fig.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmove = fig.canvas.mpl_connect(
            'motion_notify_event', self.on_move)

        self.press_event = None
        self.current_circle = None
        self.proyec = None
        self.separ = None
        self.X = np.zeros((0,2))
        self.t = np.zeros((2,0))

    def on_press(self, event):


        x0, y0 = event.xdata, event.ydata
        for circle in self.circle_list:
            contains, attr = circle.contains(event)
            if contains:
                self.press_event = event
                self.current_circle = circle
                self.x0, self.y0 = self.current_circle.center
                return
            
        if event.button == 3:
            c = Circle((x0, y0), 0.5, fc="r")
            self.circle_list.append(c)
            self.X = np.r_[self.X,np.array([[x0,y0]])]
            self.t = np.c_[self.t,np.array([0,1]).T]
        else:
            c = Circle((x0, y0), 0.5, fc="b")
            self.circle_list.append(c)
            self.X = np.r_[self.X,np.array([[x0,y0]])]
            self.t = np.c_[self.t,np.array([1,0])]
        self.ax.add_patch(c)
        self.current_circle = None
        self.fig.canvas.draw()

    def on_release(self, event):
        self.press_event = None
        self.current_circle = None
        self.actualizar()
        
        

    def on_move(self, event):
        if (self.press_event is None or
            event.inaxes != self.press_event.inaxes or
            self.current_circle == None):
            return
        
        dx = event.xdata - self.press_event.xdata
        dy = event.ydata - self.press_event.ydata
        self.current_circle.center = self.x0 + dx, self.y0 + dy
        self.fig.canvas.draw()
        self.actualizar()
    
    def actualizar(self):
        w,c = lda(self.X,self.t)
        if not isinstance(w,np.ndarray):
            return
        a = w[0]
        b = w[1]
        c1 = c[0]
        c2 = c[1]
        ## Plot functions and a point where they intersect
#        l1 =  Line2D((-20,20),((-20)*b/a,(20)*b/a))
#        if self.proyec == None:
#            self.proyec = l1
#            self.ax.add_line(self.proyec)
#        else: 
#            self.ax.get_lines()[0].set_data((-20,20),((-20)*b/a,(20)*b/a))
        
        k = a*c1 + b*c2
        l2 =  Line2D((-20,20),((k-a*(-20))/b,(k-a*(20))/b), c="g")
        
        if self.separ == None:
            self.separ = l2
            self.ax.add_line(self.separ)
        else: 
            self.ax.get_lines()[0].set_data((-20,20),((k-a*(-20))/b,(k-a*(20))/b))
        
        self.fig.canvas.draw()



