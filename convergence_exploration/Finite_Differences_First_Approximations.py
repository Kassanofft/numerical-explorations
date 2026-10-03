import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.symbols("x") #function input
h = sp.symbols("h") #step size

h_list = np.logspace(-1, -3, 1000) #log step values for log-residual plot
x_0 = 3 #point of interest

func = x**3
func_diff = sp.diff(func, x) #derivative of function

func_diff_right_approx = (func.subs(x, x+h) - func)/h #tangent line from point func(x) and func(x+h)
func_diff_left_approx = (func - func.subs(x, x-h))/h #tangent line from point func(x-h) to func(x)
func_avg_approx = (func_diff_right_approx + func_diff_left_approx)/2 #central approximation

taylor_approx_right = sp.series(func.subs(x, x+h), h, 0, 4).removeO() #computes the right taylor series up to order 4
taylor_approx_left = sp.series(func.subs(x, x-h), h, 0, 4).removeO() #computes the left taylor series
taylor_approx_right = (taylor_approx_right - func)/h
taylor_approx_left = (func - taylor_approx_left)/h
taylor_avg_approx = (taylor_approx_right + taylor_approx_left)/2 #central approximation of left and right approximations

#Abs is used to prevent negatives in the log residuals
right_approx_residual = sp.Abs(func_diff_right_approx - func_diff)
avg_approx_residual = sp.Abs(func_avg_approx - func_diff)
taylor_approx_residual = sp.Abs(taylor_avg_approx - func_diff)

#Creates an array full of residuals for each approximation (forward, central, and taylor)
right_res = np.array([float(right_approx_residual.subs({x: x_0, h: i})) for i in h_list])
avg_res   = np.array([float(avg_approx_residual.subs({x: x_0, h: i})) for i in h_list])
#taylor_res = np.array([float(taylor_approx_residual.subs({x: x_0, h: i})) for i in h_list]) #uncomment this lines to see the taylor approximation

#A log-residual plot (for exponential convergence log plots it linearly)
plt.loglog(h_list, right_res,  label="Forward Difference (O(h))")
plt.loglog(h_list, avg_res,    label="Central Difference (O(h²))")
plt.loglog(h_list, taylor_res, label="Taylor Average (O(h²))")

#Set up the plot
plt.xlabel("Step Size (h)")
plt.ylabel("Absolute Residual")
plt.title("Finite Difference Approximation Errors")
plt.legend()
plt.grid(True, which="both")
plt.show()


