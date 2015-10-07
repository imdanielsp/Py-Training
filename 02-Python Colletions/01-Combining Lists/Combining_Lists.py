# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Author: Daniel Santos                                   #
#   Date: 10/06/2015                                        #
#   Program: Combining Lists                                #
#   Porpuse:                                                #    
#   Here we will see how to manipulate lists in Python.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Python make this ridiculously easy...
list_one = [0, 1, 2, 3, 4, 5]

list_two = [6, 7, 8, 9, 10]

# This is one way to combine two lists together
my_list = list_one + list_two

print("Printing list combined")
print(my_list)

# There are a lot of way to do this.
# Here is one a little bit more complicated
list_three = [0, 9, 2, 5]
list_four = [5, 13, 77]

# Here we introduced a for-each type loop
# that iterate trough each of the elements 
# of the lists.
for item in list_four:
    list_three.append(item)

print("Printing third list")
print(list_three)