weight = 41.5
premium = 125
cost = 1.5

#Ground Shipping
if weight <= 2:
  print(weight * 1.5 + 20)
elif weight <= 6:
  print(weight * 3 + 20)
elif weight <= 10:
  print(weight * 4 + 20)
else:
  print(weight * 4.75 + 20)

print('Premium shipping is ' + str(premium) + '.')

if weight <= 2:
  cost = 4.50
  print(weight * cost)
elif weight <= 6:
  cost = 9
  print(weight * cost)
elif weight <= 10:
  cost = 12
  print(weight * cost)
else:
  cost = 14.25
  print(weight * cost)
