# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Author: Daniel Santos                                   #
#   Date: 10/05/2015                                        #
#   Program: Loops                                          #
#   Porpuse:                                                #    
#   Here we will see how For and While loops work in        #
#   Python.                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# If the switch is 1, the while loop will be activated, if 0
# the for loop will be activated.

SWITCH = 0 # This isn't a switch statement.

# While loops are constructed with block, as well as For loops.
if SWITCH is 1:
    i = 0
    print("WHILE LOOP:")
    while True:
        print("This will be print ten times!") # This will run inside of the while loop
        i += 1  # This will run inside of the while loop
        # Here a nested if statement inside of the while loop.
        if i == 10:
            break

    print("This will be printed only one!") # This is out of the while loop, inside of the if statement.
elif SWITCH is 0:
    # We will look at range() later on.
    print("FOR LOOP")
    for i in range(0,10):
        print("This will be print ten times!") # This will run inside of the while loop