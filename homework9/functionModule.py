# File: functionModule.py

import matplotlib.pyplot as plt
import numpy as np 

def horizontalSubModules():
    """
    When called, it displays two graphs, a sine and a cosine graph.
    The graphs will be horizontal with the sine graph on the left and the cosine graph on the right.
    The range is from 0 to 2pi.
    Returns graph.
    """
    x = np.linspace(0, np.pi*2, 100)
    sin = np.sin(x)
    cos = np.cos(x)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.subplots_adjust(wspace = 0.5)
    ax1.plot(x, sin)
    ax2.plot(x, cos)
    ax1.set_xlabel('X Axis')
    ax2.set_xlabel('X Axis')
    ax1.set_ylabel('Y Axis')
    ax2.set_ylabel('Y Axis')
    ax1.set_title('Sine Horizontal')
    ax2.set_title('Cosine Horizontal')
    return plt.show()
    
def verticalSubModules():
    """
    When called, it displays two graphs, a sine and a cosine graph.
    The graphs will be vertical with the sine graph on the top and the cosine graph on the bottom.
    The range is from 0 to 2pi.
    Returns graph. 
    """
    x = np.linspace(0, np.pi*2, 100)
    sin = np.sin(x)
    cos = np.cos(x)
    fig, ax = plt.subplots(2)
    fig.subplots_adjust(hspace = 0.5)
    ax[0].plot(x, sin)
    ax[1].plot(x, cos)
    ax[0].set_xlabel('X Axis')
    ax[1].set_xlabel('X Axis')
    ax[0].set_ylabel('Y Axis')
    ax[1].set_ylabel('Y Axis')
    ax[0].set_title('Sine Horizontal')
    ax[1].set_title('Cosine Horizontal')
    return plt.show()