"""
Define a function commonsubstring that takes a list of DNA strings as an input.

-First the function should check if all strings in the list are valid DNA strands (use the function defined in the 1st part). If it's not, return "error".

-If all strings in the list are valid, the function then finds the longest nucleotide substring that is in all of the strings in the list and returns it as a list. If multiples such strings exist, the function should include them all in the returned list.

For example,
commonsubstring("ACGCT", "CGCCA", "ATTACGCT") should return ["CGC"]
"""
from Antcheck import isDNA

def commonsubstring(dnalist):
  s = ""
  sz = 1000000000
  for x in dnalist:
    if isDNA(x) == False: return "error"
    if len(x) <= sz:
      s = x
      sz = len(x)
  best = -1
  d = []
  l = sz
  for i in range(sz-1):
    cur = 0
    for j in range(sz-l+1):
      ch = s[cur:cur+l]
      pos = False
      for k in dnalist:
        good = False
        cur1 = 0
        it = len(k) - l + 1
        for m in range(it):
          if k[cur1:cur1+l] == ch:
            good = True
        if good == True: pos = True
        cur1 = cur1 + 1
      if pos == True: 
        if len(ch) >= best:
          best = len(ch)
          d.append(ch)
    cur = cur + 1
  return d


