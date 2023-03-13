'''
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
'''

def pos_neg(a, b, negative):
  if (a<=-1 and b<=-1 and negative==True) or  (a<=-1 and b>=0 and negative==False) or (a>=0 and b<=-1 and negative==False):
    return True
  else:
    return False