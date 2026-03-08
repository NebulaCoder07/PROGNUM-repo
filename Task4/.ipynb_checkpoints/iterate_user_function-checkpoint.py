from numpy import sin, cos, exp, pi
from scipy.integrate import quad

def type_check(string):
    """Ensures that the user entered a number or pi"""
    try:
        return eval(string)
    except SyntaxError or ValueError:
        return "None"        # None means, that the user has to input a new value


def f(x,func):
    """ tries to evaluate the function """
    try:
        eval(func)
        return eval(func)
    except:
        return "None"              # None means, that the user has to input a new function

print('IMPORTANT: use python syntax!')

a = input("Enter the lower bound for the integration (possible constants: pi): ")
while (type(type_check(a)) == "None"):
   a = input('Please enter a number: ')
a = type_check(a)

b = input("Enter the upper bound for the integration (possible constants: pi): ")
while (type(type_check(b)) == "None"):
   b = input('Please enter a number: ')
b = type_check(b)

fun = input("Enter a function (possible functions: sin,cos,exp or polinomials): ")
while f(a,fun) == "None":
    print(f'The entered function \'{fun}\' contains elements, that cannot be recognised by the program.')
    fun = input("Enter another function (possible functions: sin,cos,exp or polinomials): ")

n = 100000
domain = np.linspace(a,b,n)

if ('x' in fun) and ("None" in f(domain,fun)):                               # sees if integration is possible on the domain
    if input('The function has a non-iterable part on the domain. Do you want to proceed anyways? (y/n)') == 'y':
        domain = domain[f(domain,fun) != "None"]
    else:
        fun = input("Enter another function (possible functions: sin,cos,exp or polinomials): ")


if not('x' in fun):                     # constant functions cannot be summed
    integral = f(domain,fun)*(b-a)
else:
    integral = sum(f(domain,fun))*(b-a)/n
    
print(f'The integral of the function {fun} on the given domain [{a},{b}] is {integral:.4f}')

func1 = 'x**4+exp(sin(x)+cos(x))'                      # The function provided in the description

d = np.linspace(0,pi,n)
integral = quad(f,0,pi, args = (func1,))
integral2 = sum(f(d,func1))*(pi-0)/n                        # Applies Monte-Carlo to the function

print(f'The integral of the function \'{func1}\' on the given domain [{0},pi] is {integral[0]:.4f} using scipy\'s quad() function.')
print(f'The integral of the function \'{func1}\' on the given domain [{0},pi] is {integral2:.4f} using Monte-Carlo integration.')