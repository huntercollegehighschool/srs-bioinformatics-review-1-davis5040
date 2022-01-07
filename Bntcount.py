"""
Define a function ntcount that takes a string representing a DNA string. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA strand, the function returns a dictionary with the counts of each nucleotide.

For example: 
ntcount("AACTGTA") 
returns {"A": 3, "C": 1, "G": 1, "T": 2}
"""
from Antcheck import isDNA

def ntcount(dna):
  a = 0
  c = 0
  g = 0
  t = 0
  if isDNA(dna) == False: return "Error"
  for x in dna: 
    if x == "A": a += 1
    if x == "C": c += 1
    if x == "G": g += 1
    if x == "T": t += 1
  d = {}
  d["A"] = a
  d["C"] = c
  d["G"] = g
  d["T"] = t
  return d
