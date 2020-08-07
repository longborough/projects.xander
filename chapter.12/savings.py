#!python
INTRATE = 10 
amount = 100
years = 5
start = 0
print("Year    Start    Paid In    Interest    Final")
for year in range(1,years+1):
  interest = (start + amount) * INTRATE / 100
  final = start + amount + interest
  print(year, start, amount, interest, final)
  start = final
