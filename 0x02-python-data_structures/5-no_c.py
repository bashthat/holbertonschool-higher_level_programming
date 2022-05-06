#!/usr/bin/python3
def no_c(my_string):
    string_xyz = ""
    for r in range(len(my_string)):
        if my_string[r] != "C" and my_string[r] != "c":
            string_xyz += my_string[r]
            return string_xyz
