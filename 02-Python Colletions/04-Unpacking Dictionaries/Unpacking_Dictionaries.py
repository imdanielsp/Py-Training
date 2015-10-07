# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Author: Daniel Santos                                   #
#   Date: 10/06/2015                                        #
#   Program: Unpacking Dictionaries                         #
#   Porpuse:                                                #    
#   Here we will see what is a dictionary in Python.        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# With the dictionary from last section, 02-03-02-Dictionaries.py
# we are going to unpack it.
my_dict = {
    'first_name': "Daniel",
    'last_name': "Santos",
    'age': 21,
    'status': "single",
}

# If we want to go trough all the elements in a dictionary, we can
# just do

print(my_dict['first_name'])
print(my_dict['last_name'])
print(my_dict['age'])
print(my_dict['status'])

# In this case, it is easy to do because we only have four keys.
# But what about if we have 3,000 keys?
# Well we use a loops to access to the keys for us.
for key in my_dict:
    print(my_dict[key])
