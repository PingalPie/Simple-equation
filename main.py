'''
This reminder is for drinking water
==================================================
In this program we are using numpy module for Square one
So, make sure you have installed numpy module
--------------------------------------------------
For Windows process to install plyer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Step 1 -> Open command prompt
Step 2 -> Type pip install numpy
Done!
==================================================
For Mac/Unix process to install plyer
Step 1 -> Open terminal
Step 2 -> type pip install numpy
Done!
'''
import numpy

opt = str(input("""Option a -> x + <|number-which-you-choose|> = <|number-which-you-choose|>
Option b -> x - <|number-which-you-choose|> = <|number-which-you-choose|>
Option c -> x * <|number-which-you-choose|> = <|number-which-you-choose|>
Option d -> x / <|number-which-you-choose|> = <|number-which-you-choose|>
Option e -> x ^ 2 = <|number-which-you-choose|>


--> """))
# Asking user what he/she want to do

if  opt == 'a':
    num1 = float(input('''
    Enter the number which you want to add - '''))
    num2 = float(input('Enter the number which is on Right hand side - '))
    res = num2-num1
    print('Value of x is', res)
# If user asked for option a means for add

elif  opt == 'b':
    num1 = float(input('''
    Enter the number which you want to subtract - '''))
    num2 = float(input('Enter the number which is on Right hand side - '))
    res = num2+num1
    print('Value of x is', res)
# If user asked for option b means for subtract
    
elif  opt == 'c':
    num1 = float(input('''
    Enter the number which you want to multiply - '''))
    num2 = float(input('Enter the number which is on Right hand side - '))
    res = num2/num1
    print('Value of x is', res)
# If user asked for option c means for multiply
    
elif  opt == 'd':
    num1 = float(input('''
    Enter the number which you want to divide - '''))
    num2 = float(input('Enter the number which is on Right hand side - '))
    res = num2*num1
    print('Value of x is', res)
# If user asked for option d means for divide
    
elif  opt == 'e':
    num1 = float(input('''
    Enter the number which you want to add in right hand side - '''))
    eres = numpy.sqrt(float(num1))
    print('Value of x is', res)
# If user asked for option e means for square
    
