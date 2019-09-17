#!/usr/bin/env python3

#import nester_function
import sys

"""This is the nester_function.py module and it provides one function called print_lol()
   which prints lists that may or may not include nested lists."""

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

def print_lol(the_list, indent=False, level=0, out=sys.stdout):
    """ Prints a list of (possibly) nested lists.

        This function takes one positional argument called "the_list", which 
        is any Python list (of - possibly - nested lists). Each data item in the 
        provided list is (recursively) printed to the screen on it's own line.
        The second argument called "ident" controls whether or not indentation 
        is show on the display. This defaults to False: set it to True to switch on.
        The third argument called "level" (which defaults to 0) is used to insert
        tab-stops when a nested list is encountered."""
    
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, out)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=out)
            print(each_item, file=out)

#print_lol(movies, out=man_file)
