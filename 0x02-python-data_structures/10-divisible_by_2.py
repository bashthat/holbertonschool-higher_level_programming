#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    theList = []
    if my_list:
        '''loop'''
        for xyz in my_list:
            if xyz % 2 == 0:
                theList.append(True)
            else:
                theList.append(False)
        return (theList)
