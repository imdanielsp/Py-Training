# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Author: Daniel Santos                                   #
#   Date: 10/06/2015                                        #
#   Program: Dictionaries 2                                 #
#   Porpuse:                                                #    
#   Here we will see what is a dictionary in Python.        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Another way to construct dictionaries in Python is like:

my_dict = {
    'first_name': "Daniel",
    'last_name': "Santos",
    'age': 21,
    'status': "single",
}

# Here we print our entire dictionary.
print(my_dict)

# We can then go back and change any of the value in a specific
# key. For example:

my_dict['first_name'] = "John"
my_dict['last_name'] = "Smith"

print(my_dict)
