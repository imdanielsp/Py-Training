# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Author: Daniel Santos                                   #
#   Date: 10/05/2015                                        #
#   Program: Basic I/O 1                                    #
#   Porpuse:                                                #    
#   Here we will be looking at print(), again, and input(), #
#   but this time in a source code. We will learn how to    #
#   compile Python code using the terminal.                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# <-- This is a comment in Python. 
# In C, or Java we use // and /**/, but in python is only the
# '#' (hastag).

# Here we are printing out the string "Hello World" 
print("Hello World")

# In Python we don't defined data types when we declare a
# variable. But after you initialize the variable, the data
# type will be equal to the type at initialization.
# For our advantage, we can change the data type later on, but 
# that is not recommended it.

# Name is an empty string
name = ""

# Here input() is a function that return whatever the user
# inputs. We need to be careful because input return a string
# type. You will see casting later on.
name = input("Enter your name: ")

# Print the inputted name to the screen.
print(name)