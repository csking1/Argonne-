
##Simple program to generate X, Y numpy arrays and create/plot a regression line


from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

def best_fit_slope_intercept(xs, ys): 
    m = (mean(xs)*mean(ys) - mean(xs*ys)) / ((mean(xs)**2) - mean(xs**2))
    b = mean(ys) - m*(mean(xs))
    return m, b

def predict_values(m, b):
    x_hat = 7
    y_hat = (m*x_hat) + b
    return x_hat, y_hat

def graph(xs, ys, line, x_hat, y_hat):

    plt.scatter(xs, ys, color='#003F72', label='data')
    plt.scatter(x_hat, y_hat, color='green', label='predicted')
    plt.plot(xs, line, label='regression_line')
    plt.legend(loc=4)
    plt.savefig('best_fit.png')

def main():
    xs= [1, 2, 3, 4, 5]
    ys= [5, 4, 6, 5, 6]
    xs=np.array(xs)
    ys=np.array(ys)
    m, b = best_fit_slope_intercept(xs, ys)
    regression_line = [(m*x) + b for x in xs]
    x_hat, y_hat = predict_values(m, b)
    graph(xs, ys, regression_line, x_hat, y_hat)

main()
  