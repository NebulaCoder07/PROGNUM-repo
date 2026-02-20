import math
def type_check(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
a = input('Enter the coefficient of the quadratic term: ')
while not(type_check(a)):
    a = input('Please enter a number: ')
a = float(a)

b = input('Enter the coefficient of the linear term: ')
while not(type_check(b)):
    b = input('Please enter a number: ')
b = float(b)

c = input('Enter the constant term: ')
while not(type_check(c)):
    c = input('Please enter a number: ')
c = float(c)

D = b**2-4*a*c

if D>0:
    print(f"The two solutions for the quadratic equation ({a})*x^2+({b})*x+({c})=0 are {(-b+math.sqrt(D))/(2*a)} and {(-b-math.sqrt(D))/(2*a)}.")
elif D == 0:
    print(f"The quadratic equation ({a})*x^2+({b})*x+({c})=0 are has one solution, which is {-b/(2*a)}.")
else:
    print(f"The quadratic equation ({a})*x^2+({b})*x+({c})=0 are has no solutions.")
