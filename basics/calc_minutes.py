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

