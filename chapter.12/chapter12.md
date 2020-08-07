### Computational algorithms

* Terminate x efficiently

### What kinds of problem

* Additional applications examples\
  Airline facre construction and revenue optimisation

* Q1: Who else uses 
encryption algorithms?\
  Internet -- not just credit card 
  and personal info
  details, but almost everything nowadays\
  Some security systems encrypt passwords
  (eg password managers)\ 
  Instant messaging systems\
  Mobile phone transmission\
  Computer file systems / external storage

### A simple computational algorithm

* Efficiently. Hmmm....

* Q2: No, don't

* Q3: Failures:\
Doesn't allow for invalid inputs\
Doesn't always terminate 
(for invalid inputs)\
Not efficient\
Apart from that, fine

* Useful functional definition is
a prerequisite for a good algorithm, IMO.

### Divide and Conquer

* Are we going to program 
this right now?

* Q4: How many guesses?

### Trace table

* Q5: Is it a prime number 
(in a very very inefficient manner)?

### Exercises

* E.1 Football
```
    if TeamAGoals == TeamBGoals then 
      TeamAPoints = TeamAPoints + 1 
      TeamBPoints = TeamBPoints + 1 
    elif TeamAGoals > TeamBGoals then 
      TeamAPoints = TeamAPoints + 3 
    else
      TeamBPoints = TeamBPoints + 3 
    endif 
```
* E.2 Juggling
```
    a = input("Enter first number:")
    b = input("Enter second number:")
    c = input("Enter third number:")
    if    (a+b+c MOD 3 != 0)
      or  (abs(a-b) <= 1)
      or  (abs(b-c) <= 1)
      or  (abs(c-a) <= 1) 
    then
      print("Invalid pattern")
    else
      print("Pattern OK")
    endif
```

* E.3 Savings
```
  program savingsTable 
  CONST INTEREST RATE = 10 
  begin 
    amount = input("Enter yearly amount:")
    years = input("Enter number of years:")
    start = 0
    print("Year", "Start", "Paid In", "Interest", "Final")
    for year = 1 to years
      interest = (start + amount) * INTEREST RATE / 100
      final = start + amount + interest
      print(year, start, amount, interest, final)
      start = final
    next year
  end
```
