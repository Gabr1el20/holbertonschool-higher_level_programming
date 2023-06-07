#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    "Prints x elements of a list"
    #First, try to print the members of my_list in the range of x
    try:
        for num in range(x):
            print("{}".format(my_list[num]), end="")
    #If an execption occurs, update the value of x to be equal to the lenght of my_list
    except Exception:
        x = len(my_list)
    #Finally, print a None (to handle the \n) and return x
    finally:
        print()
        return x
