# Prolog
# Author:  YOUR NAME
# Email:  YOUR EMAIL @student.gsu.edu
# Section: YOUR SECTION(036/066)
'''
  Purpose:

  1. familiar with the functions

  2.
    calculate the Caffeine levels

  Pre-conditions (input):
       (Enter the begining caffeine level)
  Post-conditions (output):
      get the cafferine level after 6, 12,and 24 hours

'''

# familiar with "function "
"""
We need totally 3 function in our lab today

1. named PrintHello()   
2. named PrintGoodbye()
3. CaffeineLevels()

"""


# fuction 1
def PrintHello():
    print("Hello!")


def CaffeineLevels():
    caffeine_mg = float(input("what's the level of the caffeine now? \n"))

    print()

    print(f'Your coffeine leavel now is :{caffeine_mg:.2f} \n')

    print("Ok, here is your caffeine levels: \n")

    print(f'After 6 hours: {caffeine_mg / 2:.2f} mg\n')

    # miss After 12 hours  please do it by yourself

    print(f'After 24 hours: {caffeine_mg / 8:.2f} mg\n')

    # miss After 30 hours  please do it by yourself


CaffeineLevels()


def PrintGoodbye():  # fuction2

    print("Thanks, goodbye")




def main():
    PrintHello

    CaffeineLevels

    PrintGoodbye


main()