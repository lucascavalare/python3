#!/usr/bin/env python3                                                                                                                                                              

""" 
    Example of getting tables of 1 to 10. 
"""

table = 1
while table <= 10:
    n = 1
    print ("Table %d" %table)
    while n <= 10:
        print ("%d x %d = %d"
               %(table, n, table * n))
        n = n + 1
    table = table + 1
