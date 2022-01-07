"""
Define a function commonsubstring that takes a list of DNA strings as an input.

-First the function should check if all strings in the list are valid DNA strands (use the function defined in the 1st part). If it's not, return "error".

-If all strings in the list are valid, the function then finds the longest nucleotide substring that is in all of the strings in the list and returns it as a list. If multiples such strings exist, the function should include them all in the returned list.

For example,
commonsubstring("ACGCT", "CGCCA", "ATTACGCT") should return ["CGC"]
"""
from Antcheck import isDNA

def issubstring(a, b): #is a a substring of b?
  la = len(a)
  lb = len(b)
  if la > lb: return "OOPS"
  else:
    ans = False
    cur = -1
    for i in range(lb - la + 1):
      cur += 1
      if b[cur:cur+la] == a: ans = True
    return ans

#time complexity is O(n^4), not sure if any faster solution exists
def commonsubstring(dnalist):
  s = "" #shortest dna string
  sz = 1000000000 #size of shortest dna
  for x in dnalist: 
    if isDNA(x) == False: 
      return "error" #check if DNA is valid
    if len(x) <= sz: #find shortest dna
      s = x
      sz = len(x)
  best = -1 #length of best common dna
  d = [] #list of answers with max length
  l = sz+1 #size of current string
  for i in range(sz):
    l -= 1 #increment length
    cur = -1#size of interval
    for j in range(sz-l+1):
      cur += 1#increment interval
      ch = s[cur:cur+l]
      flag = False
      for st in dnalist:
        if issubstring(ch, st) == False: 
          flag = True
      if flag == False: 
        d.append(ch)
        if best < len(ch):
          best = len(ch)
  lis = []
  for y in d:
    if len(y) == best:
      if y not in lis: lis.append(y)
  return lis


