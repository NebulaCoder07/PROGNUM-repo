import numpy as np
import matplotlib.pyplot as plt

def type_check(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def inputs(name):
    var = input(f"Enter the value for {name}: ")
    while not(type_check(var)):
        var = input('Please enter a number: ')
    return float(var)

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

print("The gaussian distribution function has a form of  𝑓(𝑥) = 𝐴 * exp[−(𝑥−𝑥0)^2/(2𝜎^2)+𝑧0]")

A = inputs("A")
x0 = inputs("x0")

sig = inputs("𝜎")
while sig == 0.0:
    print("The standard deviation must not be 0")
    sig = inputs("𝜎")
    
z0 = inputs("z0")
a = inputs("the lower bound of the function")
b = inputs("the upper bound of the function")

if b < a:
    a,b = b,a # the AREA is always positive

bound = [-4*sig if a > -4*sig else a ,4*sig if b < 4*sig else b]            # the 4sigma bound ensures that the whole peak is shown
x1 = np.linspace(bound[0],bound[1],10000)
y1 = gauss(x1, A, x0, sig, z0)

x2 = np.linspace(a,b,10000)
y2 = gauss(x2, A, x0, sig, z0)

plt.rc("text",usetex = True)
plt.title("Gaussian function values")
plt.ylabel("$A e^{-(x-x0)^2/(2 \sigma^2)}+z_0$")
plt.plot(x1,y1, color = 'black', label = f"$A={A}$ \n$x_0={x0}$ \n$z_0={z0}$\n$\sigma={sig}$")
plt.fill_between(x2,gauss(x2, A, x0, sig, z0),color = 'red', label = f'Area between x = [{a},{b}] \nthe area is {scipy.integrate.quad(gauss,a,b, args=(A,x0,sig,z0,))[0]:.3e}')
plt.legend(loc='upper right' if x0 < sum(bound)/2 else 'upper left')

plt.show()

print(f'The area below the curve on the relevant domain is {scipy.integrate.quad(gauss,a,b, args=(A,x0,sig,z0,))[0]}')