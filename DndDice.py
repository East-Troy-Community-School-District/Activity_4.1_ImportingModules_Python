'''
DnD Dice
Pawelski
5/1/2023
Python II

Instructions:
In this example, we will see how changing the import statement
affects our code. First, modify the marked line so it looks like
this...

randint(1, sides)

The code will no longer work. Why? Change the code back to it's
original form. Let's modify the import statment so that it looks
like this...

import random as r

Try running the code. It no longer works! Why? When we use the as
keyword, we provide an alias for the module. What does this mean?
How should we change the marked line so that the code works? What
is the benefit of importing a module under an alias? Let's modify
the import again so that it looks like this...

from random import randint

Try running the code. It no longer works! By modifying the import
in this way, we have now import only the specific function randint().
This means that we no longer have to reference the module or it's
alias to call the randint() function. Modify the marked line so that
the code works again. What is the benefit of importing the function
in this way? Guess what, let's modify the import again...

from random import randint as r

Obviously, the code will no longer work. Modify the marked line so
that the code works again. What is the benefit of importing the
function under an alias? We have only one more import to look at

from random import *

In addition, we will have to revert the marked line back to this...

randint(1, sides)

What this import will do is import all the functions in the random
module without any alias. Why might we do this?
'''

from random import randint as r

def roll_dice(sides, times):
    '''
    Simulates a given number of rolls of a dice with a given number
    of sides.
    '''
    for i in range(0, times):
        roll = r(1, sides)		# modify this line!
        print(roll)

repeat = "y"
while repeat == "y":
    highest_value = int(input("What die do you need to roll? (4, 6, 8, 10, 12, 20, or 100) >> "))
    roll_amounts = int(input("How many times? >> "))
    roll_dice(highest_value, roll_amounts)
    repeat = input("Do you need to roll again? (y/n) >> ")
    print()