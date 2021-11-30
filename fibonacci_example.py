xterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if xterms <= 0:
   print("Please enter a positive integer")
elif xterms == 1:
   print("Fibonacci sequence upto",xterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < xterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

'''
Output Example:

How many terms? 4
Fibonacci sequence:
0
1
1
2
'''