# 5. Write a program that simulates the throw of a die I.e. a random number generator

# 6. Using the concept learned in 5 above, write a program that jumbles the word "PASSWORD". That is, your program should effectively scatter the letters of the word in a different manner every time the program is run

import random

def dice_roll():
    return random.randint(1, 6)

print(dice_roll())


def jumbler(word):
    x = [i for i in word]
    random.shuffle(x)
    return ''.join(x)

print(jumbler('PASSWORD'))
