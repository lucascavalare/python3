#!/usr/bin/env python3

"""
   Sum integer numbers until 0 is typed. 
   When the program finds typed 0, then goes out showing the sum amount.
"""

sum = 0
while True:
    x = int(input("Type the number: (0 goes out): "))
    if x == 0:
        break
    sum = sum + x 
print ("Sum: %d" %sum)
