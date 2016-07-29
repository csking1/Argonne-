

import random 
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

def create_N_dataset(N, variance, step=2, correlation=False):

    val = 1
    ys = []
    for i in range(N):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step

    xs = [i for i in range(len(ys))]
    return np.array(xs), np.array(ys)

def best_fit_slope_intercept(xs, ys): 
    m = (mean(xs)*mean(ys) - mean(xs*ys)) / ((mean(xs)**2) - mean(xs**2))
    b = mean(ys) - m*(mean(xs))
    return m, b

def coefficient_of_determination(ys_origin, ys_line):
    y_mean_line = [mean(ys_origin) for y in ys_origin]
    squared_error_reg = sum((ys_line - ys_origin) * (y_mean_line - ys_origin))
    squared_error_ymean = sum((y_mean_line - ys_origin) * (y_mean_line - ys_origin))
    # print ("Squared error regression is {}".format(squared_error_reg))
    # print ("Squared error ymean is {}".format(squared_error_ymean))
    return 1 - (squared_error_reg/squared_error_ymean)
def graph(xs, ys, regression_line, variance):

    plt.scatter(xs, ys, color='#003F72', label='data')
    plt.plot(xs, regression_line, label='regression_line')
    plt.legend(loc=4)
    plt.savefig('regression variance {}.png'.format(variance))


variance = 10
xs, ys = create_N_dataset(40, variance, 2, 'pos')
m, b = best_fit_slope_intercept(xs, ys)
regression_line = [(m*x) + b for x in xs]
r_squared = coefficient_of_determination(ys, regression_line)
print ("R squared for variance {} is {}". format(variance, r_squared))
graph(xs, ys, regression_line, variance)
