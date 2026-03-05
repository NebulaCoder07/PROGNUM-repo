import numpy as np
game_on = True
def game():
    """One round of rock-paper-scissors"""
    
    signs = ['R','P','S']
    sign = input('Type R for rock, P for paper or S for scissors:').upper()   # gets the sign and converts it to a capital letter (if someone hits lowercase)
    if not(sign in signs):                                                    # checks if the given sign is valid : quits if not
        return "Error"
    
    generated = signs[np.random.randint(0,2)]                                 # if the user input is valid, the code continues to run : generating the machine's sign
    print(f"Machine says: {generated}")
    if sign == 'S' and generated == 'R':                                      # machine's rock beats user's scissors
        return "Machine"
    elif signs.index(sign) == signs.index(generated)-1:                       # R loses to P, P loses to S : Machine wins 
        return "Machine"
    elif signs.index(sign) == signs.index(generated)+1:                       # P wins to R, S wins to P : User wins
        return "User"
    elif signs.index(sign) == signs.index(generated):                         # if the two signs are equal : draw
        return "Draw"

while game_on:
    print(game(),"won this round.")                                           # result of a round
    next_ = input("Do you want to continue? [y/n]").upper()                   # asks for next round
    if next_ == 'N':
        game_on = False                                                       # stops loop upon request
    elif next_ == 'Y':
        pass
    else:
        while next_ != 'Y' and next_ != 'N':
            next_ = input("Input cannot be comprehended, please type 'y' or 'n'!").upper()
print("Thank you for playing!")