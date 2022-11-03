# Prolog
# Author:  Toan Le
# Email:  tle153@student.gsu.edu
# Section: 036
import math
"""
    Purpose:

  1. familiar with the functions 

  2. calculate the Caffeine levels

  Pre-conditions (input): 
       (Enter the caffeine level now)
  Post-conditions (output): 
      get the cafferine level after 6, 12, 24,30 hours 

We need totally 3 function in our lab today

1. PrintHello()   
2. PrintGoodbye()
3. CaffeineLevels()

"""


# fuction 1

def PrintHello():
   print("Hello!")

# fuction 2

def CaffeineLevels():

    caffeine_mg = float(input("what's the level of the caffeine now? "))

    print(f'Your coffeine level is :{caffeine_mg:.2f} \n')

    print("Ok, here is your caffeine levels: \n")

    print(f'After 6 hours: {caffeine_mg/ 2:.2f} mg\n')

# missed “After 12 hours”   please do it by yourself
    print(f'After 12 hours: {caffeine_mg / 4:.2f} mg\n')

    print(f'After 24 hours: {caffeine_mg / 16:.2f} mg\n')
# missed “After 30 hours”   please do it by yourself
    print(f'After 30 hours: {caffeine_mg / 32:.2f} mg \n')


# function3
def PrintGoodbye():

        print("Thanks, goodbye")


def main():
    print(dir(math))
    '''
    PrintHello()

    CaffeineLevels()

    PrintGoodbye()

    print(dir(math))
    '''
main()
# line 29, missing colon after parentheses - added colon
# line 38, 'leavel' spelled wrong, corrected to level
# line 45, added code to print out for 12 hours
# line 47, fixed semantics error for mg caffeine after 24 hours --
#   half life every 6 hours, so it should be divided by 16, not 8
# line 49, added code to print out caffeine level after 30 hours
