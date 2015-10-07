# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Author: Daniel Santos                                   #
#   Date: 10/06/2015                                        #
#   Program: Removing from Lists                            #
#   Porpuse:                                                #    
#   Here we will see how to manipulate lists in Python.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# In this link you can see all the method of lists. We won't
# covert them all because it will make this tutorial very large.
# https://docs.python.org/2/tutorial/datastructures.html
#
# Here we will remove from list, again a very easy task with
# Python

my_list = ['a', 'b', 'c', 'd', 'e', '...']

# In this case I won't explain how .pop() works.
# We will look for it in the documentation.
poped = my_list.pop(2)

print(poped)

my_list.remove('...')

print(my_list)