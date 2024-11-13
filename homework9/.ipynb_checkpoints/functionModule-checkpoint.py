import matplotlib.pyplot as plt
import numpy as np 

sin = np.sin(x)
cos = np.cos(x)

def horizontalSubModules():
    x = np.linspace(0, np.pi*2, 100)
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
    x = np.linspace(0, np.pi*2, 100)
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