# Calculate the factorial of a number with if conditionals

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Factorial doesn't exist for negative numbers")

elif num == 0:
   print("Number: 0 Factorial: 1")

else:
   for i in range(1,num + 1):
       factorial = factorial*i

   print("Number:",num,"Factorial:",factorial)

'''
Output Example
Enter a number: 8
Number: 8 Factorial: 40320
'''