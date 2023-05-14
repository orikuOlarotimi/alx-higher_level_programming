#!/usr/bin/python3
def element_at(my_list, idx,  element):
    count = len(my_list) - 1
    if idx > count:
        return None
    elif idx < 0:
        return None
    else:
        my_list[idx] = element
        return my_list
