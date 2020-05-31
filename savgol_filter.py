'''
This simple example demonstrates the usage of the savgol filter
in reducing the noise of signals. Such application is commonly used 
when comparing signals from different sources; such as comparing
a signal from a virtual sensor to that from a physical sensor.
signals from physical sensors tend to have a lot of noise
'''

import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

x = np.linspace(0,2*np.pi,100)
y = np.sin(x) + np.random.random(100) * 0.2
yhat = scipy.signal.savgol_filter(y, 51, 3) # window size 51, polynomial order 3

plt.plot(x,y)
plt.plot(x,yhat, color='red')
plt.show()