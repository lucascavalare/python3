#/usr/bin/env python3

""" Basic example about calculating a bill of minutes spent by the customer in a month. 
    The customer inputs the amount of the desired minutes and the output is the amount of
    the price. Based on the quantity of minutes, the bill is calculated.
"""

minutes = int(input("Utilized minutes: "))
if minutes < 200:
   price = 0.20
elif minutes <= 400:
   price = 0.18
elif minutes <= 800:
   price = 0.15
else:
   price = 0.08

print("Billing: $%6.2f" % (minutes * price))

