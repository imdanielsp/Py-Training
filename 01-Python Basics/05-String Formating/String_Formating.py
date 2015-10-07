# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Author: Daniel Santos                                   #
#   Date: 10/05/2015                                        #
#   Program: String Formatting                              #
#   Porpuse:                                                #    
#   Here we will see string formating we the format method  #
#   of the String class in Python. If you don't now what    #
#   is a class or a method, not worries, we will see that   #
#   later.                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Before we continue, I just want you to have in mind that
# in Python, everything is an object. Later on, you will see
# what I am saying in action.

# Here we get all the input that we need
name = input("What is your name? ")
age = int(input("How old are you? "))
number = int(input("What is your favorite number? "))
lucky_number = age * number + 3

# Here we start using the format method. The '{}' is a "placeholder". 
# And the argmuent for the .format() have to be in order.
description = "His name is {}, and he/she is {} years old".format(name, age)
description = description + " his/her favorite number is {}, and his/her lucky number is {}.".format(number, lucky_number)  

# We print our formatted string.
print(description)