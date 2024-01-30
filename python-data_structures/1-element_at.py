#!/usr/bin/python3
def element_at(my_list, index):
    if index < 0 or index >= len(my_list):
        return None
    else:
        return my_list[index]
'''
my_list = [1, 2, 3, 4, 5]
index = 3
result = element_at(my_list, index)
print("Element at index {:d} is {}".format(index, result))
'''
