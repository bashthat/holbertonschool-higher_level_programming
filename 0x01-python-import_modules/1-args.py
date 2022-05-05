#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import sys
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    else:
        if len(sys.argv) == 2:
            print("{:d} argument:".format(len(sys.argv) - 1))
        else:
            print("{:d} arguments:".format(len(sys.argv) - 1))
        for av in range(1, len(sys.argv)):
            print("{:d}: {}".format(av, (sys.argv[av])))
