# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Author: Daniel Santos                                   #
#   Date: 10/06/2015                                        #
#   Program: Dictionaries                                   #
#   Porpuse:                                                #    
#   Here we will see what is a dictionary in Python.        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# The Python Documentation define Dictionaries as:
#
# Dictionaries are sometimes found in other languages as
# “associative memories” or “associative arrays”. 
# Unlike sequences, which are indexed by a range of numbers, 
# dictionaries are indexed by keys, which can be any immutable 
# type; strings and numbers can always be keys.

# Example of a dictionary

# We just created an empty dictionary
my_dict = {}

# Here we are creating keys and initializing them
# with a value. We will see how easy it is to access
# those values back again.
my_dict['name'] = "Daniel"
my_dict['last'] = "Santos"
my_dict['age'] = 21
my_dict['status'] = "single"

# Here we print our entire dictionary.
print(my_dict)

# We can print a specific element if know its key
print("He's name is " + my_dict['name'] + ".")

# This is very powerful. When I was learning them,
# I was kind of confused because I was very used to
# work with arrays. In the next section, you will see
# how to unpack dictionaries.