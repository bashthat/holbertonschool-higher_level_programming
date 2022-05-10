#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        xyz = max(a_dictionary, key = a_dictionary.get)
    return (xyz)
