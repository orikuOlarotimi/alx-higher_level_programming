#!/usr/bin/python3
for i in range(0, 10):
    for q in range(i + 1, 10):
        if i == 8 and q == 9:
            print("{}{}".format(i, q))
        else:
            print("{}{}".format(i, q), end=", ")
