#!/usr/bin/python3
for n in range(97, 123):
    if chr(n) is not 'q' and chr(n) is not 'e':
        print("{}".format(chr(n)), end="")
