#!/usr/bin/python3
def element_at(my_list, idx):
    count = len(my_list) - 1
    if idx > count:
        return None
    elif idx < 0:
        return None
    else:
        return my_list[idx]
