#!python

def generate(num1):
  print(f" 4: Called with {num1}")
  if num1 > 10:
    print(f" 6: Bingo! {num1} > 10")
    return 10
  else:
    print(f" 9: Calculating: {num1} + (generate({num1} + 1) DIV 2)")
    print(f"10: Recursing with {num1 + 1}")
    unwind = generate(num1 + 1)
    print(f"12: Got back: {unwind}")
    print(f"13: Returning: {num1} + {(unwind // 2)}")
    return num1 + (unwind // 2)

def main():
  print(f"17: End result: {generate(7)}")

main()
