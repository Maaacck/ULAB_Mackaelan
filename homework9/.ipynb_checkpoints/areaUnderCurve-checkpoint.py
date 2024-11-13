# File: areaUnderCurve.py 

import numpy as np
import matplotlib.pyplot as plt

def areaUnderCurve():
    """
    When called, it displays two different equations horizontally. 
    Range is (0, 5) and (0, 2pi).
    Equation 1 is|Sin(xx)/2(x^(x-pi/2)/pi| and equation 2 is cos(xsin(xtan(x))).
    Code plots the equations then shows the area under the curve for both. 
    Returns graph. 
    """
    pi = np.pi
    x = np.linspace(0, 5, 1000)
    x2 = np.linspace(0, pi*2, 1000)
    xPower = x**x
    numerator = np.sin(xPower)    
    denominatorPower = (xPower - pi / 2) / pi
    denominator = 2 ** denominatorPower
    fraction = numerator / denominator
    equation = np.abs(fraction)
    equation2 = np.cos(x*np.sin(x*np.tan(x)))
    section = np.linspace(0, 5, 1000)
    section2 = np.linspace(0, pi*2, 1000)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.subplots_adjust(wspace = 0.5)
    ax1.plot(x, equation, color='indigo', label='Equation')
    ax2.plot(x2, equation2, color='navy', label='Equation 2')
    ax1.fill_between(section, equation[:len(section)], color='thistle', alpha=0.5)
    ax2.fill_between(section2, equation2[:len(section2)], color='mediumslateblue', alpha=0.5)
    ax1.set_xlabel('X Axis')
    ax2.set_xlabel('X Axis')
    ax1.set_ylabel('Y Axis')    
    ax2.set_ylabel('Y Axis')
    ax1.set_title('Area Under Curve Equation 1')
    ax2.set_title('Area Under Curve Equation 2')
    ax1.grid()
    ax2.grid()
    ax1.legend()
    ax2.legend()
    return plt.show()