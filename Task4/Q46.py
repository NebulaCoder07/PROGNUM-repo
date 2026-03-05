from numpy import *
fun = input("Input a function:")
xmin = float(input("Input the lower bound:"))
xmax = float(input("Input the upper bound:"))
n = 100000
x = random.uniform(xmin,xmax,n)
y = eval(fun)

integral = sum(y)*(xmax-xmin)/n
print(integral)