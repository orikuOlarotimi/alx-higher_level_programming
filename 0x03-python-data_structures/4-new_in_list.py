#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = len(my_list) - 1
    if idx > count:
        return my_list

    elif idx < 0:
        return my_list

    else:
        my_list[idx] = element
        return my_list
    copy = [x for x in my_list]
    copy[idx] = element
    return copy
