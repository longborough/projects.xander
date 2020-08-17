#!python

# -----

def calcFactorial(n):
  print("Start CalcF: ", n)
  if n==0:
    print("calcF(0): bingo!") 
    factorial = 1
  else:
    print("calcF", n, "calls calcF", n-1)
    next = calcFactorial(n-1)
    factorial = n * next
    print("calcF", n, "returns", factorial)
  return factorial

def main():
  print("End result:",calcFactorial(5))

main()
