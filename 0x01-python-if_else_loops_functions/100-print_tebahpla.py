#!/usr/bin/python3
for i in range(90, 64, -1):
    char = chr(i) if i % 2 == 1 else chr(i + 32)
    print("{}".format(char), end="")
