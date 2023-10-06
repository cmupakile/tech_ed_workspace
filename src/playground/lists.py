# example python lists
# python can handle multiple data types in a list. But that invites confusion in code

# lists are reference based

#                   0          1      2        3
shopping_list = ["bananas", "eggs", "milk", "bread", "cabbages"]
#                             -3     -2      -1
# print(shopping_list[-2])
#
# Methods

shopping_list.append("cabbages")

# using set removes the duplicates you may see when ingesting data
print(set(shopping_list))