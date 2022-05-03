#!/bin/python3
import random
number = random.randint(-20, 20)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
elif number < 0:
    print("{} is negative".format(number))
