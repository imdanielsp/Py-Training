# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Author: Daniel Santos                                   #
#   Date: 10/05/2015                                        #
#   Program: If-Else                                        #
#   Porpuse:                                                #    
#   Here we will see if-else statement in Python.           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Here we will see why blocks in Python are really important.


age = int(input("Enter your age: "))

# Here we see if and else statement and blocks.
# Here is the main block
if age > 0 and age < 21:
    # This print statement is indented, so it's inside of the this block.
    print("Sorry you can't buy alcohol yet. You still need to wait {} year(s)".format(21-age))
elif age > 0 and age >= 21:
    # We are inside of the else-if block.
    print("You can definitely buy alcohol, but don't drink a lot. It's bad for you.")
else:
    # Inside of the else block.
    print("Something went wrong....")