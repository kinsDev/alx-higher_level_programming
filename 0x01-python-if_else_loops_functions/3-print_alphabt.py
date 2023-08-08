#!/usr/bin/python3
for i in range(97, 123):
    if character(i) == 'q' or character(i) == 'e':
        continue
    print(character(i).format(i), end='')
