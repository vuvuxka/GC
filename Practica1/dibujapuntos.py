import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
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
        self.clase_1 = []
        self.clase_2 = []

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

    def on_press(self, event):
#        if event.button == 3:
#            self.fig.canvas.mpl_disconnect(self.cidpress)
#            self.fig.canvas.mpl_disconnect(self.cidrelease)
#            self.fig.canvas.mpl_disconnect(self.cidmove)
#            points = [circle.center for circle in self.circle_list]
#            print("Pues tenías razon")
#            return points

        x0, y0 = event.xdata, event.ydata
        for circle in self.circle_list:
            contains, attr = circle.contains(event)
            if contains:
                self.press_event = event
                self.current_circle = circle
                self.x0, self.y0 = self.current_circle.center
                return
        p = np.array([x0,y0])
            
        if event.button == 3:
            c = Circle((x0, y0), 0.5, fc="r")
            self.circle_list.append(c)
            self.clase_1.append(np.array([[x0],[y0]]))
        else:
            c = Circle((x0, y0), 0.5, fc="b")
            self.circle_list.append(c)
            np.concatenate((p,p.T), axis=1 )
        self.ax.add_patch(c)
        self.current_circle = None
        self.fig.canvas.draw()

    def on_release(self, event):
        self.press_event = None
        self.current_circle = None
        t1 = len(self.clase_1)
        t2 = len(self.clase_2)
        t = np.array([np.concatenate(((np.ones(t1))[:], np.zeros(t2)), axis=0),
                      np.concatenate(((np.zeros(t1))[:], np.ones(t2)), axis=0)])
        #x = np.concatenate((self.circle_list_1[:], self.circle_list_2[:]), axis=0)
        print (t)
        print(self.clase_1)
       # lda()

    def on_move(self, event):
        if (self.press_event is None or
            event.inaxes != self.press_event.inaxes or
            self.current_circle == None):
            return
        
        dx = event.xdata - self.press_event.xdata
        dy = event.ydata - self.press_event.ydata
        self.current_circle.center = self.x0 + dx, self.y0 + dy
        self.fig.canvas.draw()
