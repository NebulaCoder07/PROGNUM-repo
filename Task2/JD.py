days = [31,28,31,30,31,30,31,31,30,31,30,31]

def check_type(string, goal):
    """tries integer conversion for the input and returns the corresponding boolean"""
    if goal == 'int':
        try:
            int(string)
            return True
        except ValueError:
            return False
        
    elif goal == 'float':
        try:
            float(string)
            return True
        except ValueError:
            return False


#------------Inputs---------------
Y1 = input("Enter the year:") #gets the year from user
while not(check_type(Y1, 'int')):
    Y1 = input("The given year is not an integer; please enter a valid year: ")
Y1 = int(Y1)

#--------------       
M1 = input("Enter the month(1-12):") #gets the month from user
while not(check_type(M1, 'int')) or int(M1) > 12:
    M1 = input("The given month is not an integer or is out of range; please enter a valid month: ")
M1 = int(M1)

#--------------        
D1 = input("Enter the day of the month (can be decimal too, must be bigger than 0): ") #gets the day from user
while not(check_type(D1, 'float')) or float(D1)<0 or float(D1)>days[M1-1]:
    D1 = input("The given day is either out of range for that month, or negative, or not a number at all; please enter a valid day: ")
D1 = float(D1)

#------------Calculation---------------
JD1 = 367*Y1 -7*(Y1+(M1+9)//12)//4 - 3*((Y1+(M1-9)//7)//100 + 1)//4 + (275*M1)//9 + D1 + 1721029-0.5


print(f'The given date in Julian Date is {JD1}')
