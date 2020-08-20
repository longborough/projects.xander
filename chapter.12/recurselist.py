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

def sumList(list,totalSoFar):
  pp(("Start sumL", list, totalSoFar))
  if empty(list):
    pp(("sumL: bingo!", list, totalSoFar)) 
    total = totalSoFar
  else:
    first = head(list)
    rest = tail(list)
    pp(("sumL recurses with", rest, totalSoFar + first))
    total = sumList(rest, totalSoFar + first)
    pp(("sumL", list, totalSoFar, "returns", total))
  return total

def main():
  numbers = [16, 2, 7, 5,]
  pp(("End result:",sumList(numbers,0)))

main()
