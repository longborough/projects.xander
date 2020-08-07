#!python

# Block 1
number = 19321
low = 1
high = number
guess = (low+high) // 2
nsquared = guess**2
# Block 2
while nsquared != number:
  if nsquared > number:
    high = guess
  else:
    low = guess
  #-- endif
  guess = (low+high) // 2
  nsquared = guess**2
#-- endwhile
# Block 3
print(f"Square root is {guess}")
