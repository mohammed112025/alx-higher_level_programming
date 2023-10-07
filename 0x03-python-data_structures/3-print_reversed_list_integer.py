#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ''' prints all integers of a list, in reverse order

    Args:
        my_list (list): the list what you want to reverse it

    Returns: NULL
    '''
    if len(my_list) is None:
        print("", end="")
    else:
        for elem in my_list[::-1]:
            print("{:d}".format(elem))
