'''

Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
'''

def double_char(str):
  nw = ""
  for i in range(0,len(str),1):
    nw += str[i]*2
  return nw