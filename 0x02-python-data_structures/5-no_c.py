#!/usr/bin/python3
def no_c(my_string):
    string_xyz = ""
    for r in my_string:
        if r != "C" and r != "c":
            string_xyz += r
            return string_xyz
