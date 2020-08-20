#!python
import pprint
# A pretty-print function
pp = pprint.PrettyPrinter(indent=2,width=70).pprint

# -----------------------------------------------------------------
# A few helper functions to make py look a bit more like pseudocode
# -----------------------------------------------------------------
def empty(list):
  return list == []
def head(list):
  return list[0]
def tail(list):
  return list[1:]
# -----------------------------------------------------------------

def sumList(list):
  pp(("Start sumL", list))
  if empty(list):
    pp(("sumL: bingo!", list)) 
    total = 0
  else:
    first = head(list)
    rest = tail(list)
    pp(("sumL recurses with", rest))
    total = first + sumList(rest)
  pp(("sumL", list, "returns", total))
  return total

def main():
  numbers = [16, 2, 7, 5,]
  pp(("End result:",sumList(numbers)))

main()
