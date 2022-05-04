#!/usr/bin/python3
for n in range(0, 100):
    print("{:02d}".format(n), end="")
    print(("\n", ", ")[n != 99], end="")
