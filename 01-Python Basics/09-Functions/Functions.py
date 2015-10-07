# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Author: Daniel Santos                                   #
#   Date: 10/05/2015                                        #
#   Program: Functions!                                     #
#   Porpuse:                                                #    
#   Here we will see how to declare and define functions.   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# In Python we declare function as following
def my_function():
    # Do something!
    print("This is my function")
    
# Here we don't need to expecify what this function will return.
# This is sometimes good, and sometimes bad. You will have to make
# sure that this function return what you expect.
def my_return():
    # This function will return a number!
    return 9

def my_string():
    # This function will return a string, hold it!
    return "My good looking string!"

def greetings(name):
    print("Welcome to the training {}, we are please to have you here".format(name))
    return name

def something():
    print("We are doing something big!")
    i = 0 
    string = ""
    while i < 20:
        string = string + " p"
        i += 1
    return string


# Here is main :D, just the black

#Calling a function
my_function()

# Here we hold the number that my_number() returns
number = my_return()

# Here we format a string with the string that return the function
print("Hello {}, nice to meet you!".format(my_string()))

# Here we pass a string as an argument
greetings("Daniel")

# Here we just call it....
something()
