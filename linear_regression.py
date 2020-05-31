'''
This script demonstrates the use of linear regression on a random data sample
'''

import numpy as np
import matplotlib.pyplot as plt


def mean(values):
    return sum(values) / float(len(values))

# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

# Calculate the variance of a list of numbers
def variance(values, mean):
    return sum([(x-mean)**2 for x in values])

# Calculate coefficients
def coefficients(x,y):
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return [b0, b1]
    
x =  [1,2,3,4,5,6,7,8,9]
y =  [0.95,2.245,3.065,3.8456,5.453,6.774,7.2,7.95,9.3] 
linex = np.linspace(min(x),max(x))
b0,b1 = coefficients(x,y)
liney = b0 + b1 * linex    

plt.figure(1)
plt.plot(x,y, ".", label = " orig")
plt.plot(linex, liney, "--", label = " linear fit: y = "+str(round(b0,4))+"+"+str(round(b1,4))+"*x" )
plt.legend()
plt.show()