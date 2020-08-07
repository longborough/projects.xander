#!python

# Block 1
number = 19321              # Square root of this
low = 1                     # Starting lower limit
high = number               # Starting higher limit
guess = (low+high) // 2     # Initial guess -- halfway
nsquared = guess * guess    # Guess squared
# Block 2
count = 1                   # Initialise guess count
while nsquared != number:   # Looping until we find it (!)
  print(f"Guess = {guess}") # Print the guess, for the lulz.
  if nsquared > number:     # Where are we?
    high = guess            # Too high, guess is new upper limit
  else:
    low = guess             # Too low, guess is new lower limit
  #-- endif
  count += 1                # Add 1 to guess count
  guess = (low+high) // 2   # New guess is halfway
  nsquared = guess * guess  # Guess squared
#-- endwhile
# Block 3
print(f"Square root is {guess}")
print(f"In {count} guesses.")
